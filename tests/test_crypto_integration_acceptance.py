"""Phase 2 integration acceptance checks for crypto collection and reporting."""

from __future__ import annotations

import importlib
from pathlib import Path
import re
import tomllib


ROOT = Path(__file__).parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"


def _project_scripts() -> dict[str, str]:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    return project["project"].get("scripts", {})


def _crypto_script(role: str) -> tuple[str, str]:
    matches = [
        (name, target)
        for name, target in _project_scripts().items()
        if "crypto" in name.lower() and role in name.lower()
    ]
    assert matches, f"missing a crypto {role} console script"
    assert len(matches) == 1, f"ambiguous crypto {role} console scripts: {matches!r}"
    return matches[0]


def _cron_expressions(text: str) -> list[str]:
    return [
        match.strip()
        for match in re.findall(r"cron\s*:\s*['\"]?([^'\"\r\n#]+)", text, re.I)
    ]


def _is_every_three_hours(expression: str) -> bool:
    fields = expression.split()
    return len(fields) == 5 and fields[1] in {"*/3", "0-23/3"}


def _is_weekly(expression: str) -> bool:
    fields = expression.split()
    return (
        len(fields) == 5
        and fields[2] == "*"
        and fields[3] == "*"
        and fields[4] not in {"*", "?"}
    )


def _job_names(text: str) -> list[str]:
    jobs = re.search(r"(?ms)^jobs:\s*$\n(?P<body>.*)", text)
    assert jobs, "workflow must define jobs"
    return re.findall(r"(?m)^  ([A-Za-z0-9_-]+):\s*$", jobs.group("body"))


def _concurrency_group(text: str) -> str:
    match = re.search(r"(?m)^\s{2}group:\s*([^#\r\n]+)", text)
    assert match, "workflow must define a concurrency group"
    return match.group(1).strip().strip("'\"")


def test_crypto_package_exposes_collector_and_weekly_report_cli() -> None:
    for role in ("collect", "report"):
        _, target = _crypto_script(role)
        module_name, separator, attribute = target.partition(":")
        assert separator and module_name.startswith("observatory.crypto")
        assert callable(getattr(importlib.import_module(module_name), attribute))


def test_crypto_collection_workflow_has_the_long_sampling_job_contract() -> None:
    path = WORKFLOWS / "crypto-collect.yaml"
    assert path.is_file(), "Phase 2 requires .github/workflows/crypto-collect.yaml"
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()

    assert "workflow_dispatch:" in lowered
    assert any(_is_every_three_hours(cron) for cron in _cron_expressions(text))
    assert _job_names(text) and len(_job_names(text)) == 1
    assert re.search(r"(?m)^\s+timeout-minutes:\s*350\s*(?:#.*)?$", text)

    collect_name, _ = _crypto_script("collect")
    assert re.search(rf"\buv\s+run\s+{re.escape(collect_name)}\b", text)
    assert (
        re.search(r"--(?:sample-)?interval(?:-minutes)?(?:=|\s+)15\b", lowered)
        or re.search(r"\bsleep\s+(?:900|15m)\b", lowered)
    ), "the job must sample every 15 minutes"
    assert (
        re.search(r"--(?:max-|run-|total-)?(?:minutes|duration)(?:=|\s+)340\b", lowered)
        or re.search(r"\b(?:20400|5h40m|5h40)\b", lowered)
    ), "the job must run for roughly 5 hours 40 minutes"


def test_crypto_collection_workflow_serializes_and_pushes_hourly_with_retry() -> None:
    path = WORKFLOWS / "crypto-collect.yaml"
    assert path.is_file(), "Phase 2 requires .github/workflows/crypto-collect.yaml"
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()

    assert re.search(r"(?m)^\s{2}cancel-in-progress:\s*false\s*(?:#.*)?$", lowered)
    crypto_group = _concurrency_group(text)
    other_groups = {
        _concurrency_group(other.read_text(encoding="utf-8"))
        for other in WORKFLOWS.glob("*.y*ml")
        if other != path and "group:" in other.read_text(encoding="utf-8")
    }
    assert crypto_group not in other_groups

    assert (
        re.search(r"--commit-interval(?:-minutes)?(?:=|\s+)60\b", lowered)
        or re.search(r"\bsleep\s+(?:3600|60m|1h)\b", lowered)
    ), "generated crypto data must be committed/pushed hourly"
    pull = re.search(r"\bgit\s+pull\s+--rebase\b", lowered)
    push = re.search(r"\bgit\s+push\b", lowered)
    assert pull and push and pull.start() < push.start()
    assert re.search(r"\b(?:retry|until|while)\b|\bfor\s+\w+\s+in\b", lowered)


def test_crypto_weekly_report_is_wired_into_a_scheduled_workflow() -> None:
    report_name, _ = _crypto_script("report")
    candidates = []
    for path in WORKFLOWS.glob("*.y*ml"):
        text = path.read_text(encoding="utf-8")
        if re.search(rf"\buv\s+run\s+{re.escape(report_name)}\b", text):
            candidates.append(text)

    assert candidates, "no GitHub workflow invokes the crypto report CLI"
    assert any(
        "workflow_dispatch:" in text.lower()
        and any(_is_weekly(cron) for cron in _cron_expressions(text))
        for text in candidates
    )


def test_hyperliquid_is_documented_as_optional_and_disabled_by_default() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    phase_start = readme.find("phase 2")
    assert phase_start >= 0
    phase_two = readme[phase_start:]
    collect_path = WORKFLOWS / "crypto-collect.yaml"

    assert re.search(r"hyperliquid.{0,160}optional|optional.{0,160}hyperliquid", phase_two, re.S)
    assert re.search(
        r"hyperliquid.{0,200}(?:off|disabled).{0,40}default|"
        r"(?:off|disabled).{0,40}(?:by\s+)?default.{0,200}hyperliquid",
        phase_two,
        re.S,
    )
    assert collect_path.is_file()
    assert "hyperliquid" not in collect_path.read_text(encoding="utf-8").lower()


def test_readme_states_phase_two_source_budget_and_research_only_policy() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    phase_start = readme.find("phase 2")
    assert phase_start >= 0
    phase_two = readme[phase_start:]

    assert "public" in phase_two
    assert re.search(r"key[ -]?less|no (?:api )?keys?|without (?:api )?keys?", phase_two)
    assert re.search(
        r"u\.?s\.?[ -]compatible|united states[ -]compatible|available in the (?:u\.?s\.?|united states)",
        phase_two,
    )
    assert re.search(
        r"annual.{0,120}(?:under|below|less than|<).{0,30}300\s*mb|"
        r"(?:under|below|less than|<).{0,30}300\s*mb.{0,120}annual",
        phase_two,
        re.S,
    )
    assert re.search(r"warn\w*.{0,100}250\s*mb|250\s*mb.{0,100}warn\w*", phase_two, re.S)
    assert re.search(r"no trading|never trade|does not trade|do not trade", phase_two)
    assert re.search(
        r"(?:not|never|do not|does not).{0,40}publish\w*.{0,40}(?:an? )?edge|"
        r"edge.{0,40}(?:not|never|do not|does not).{0,40}publish\w*",
        phase_two,
        re.S,
    )
