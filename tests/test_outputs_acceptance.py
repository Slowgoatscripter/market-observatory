"""Acceptance checks for reproducible artifacts and optional notifications."""

from __future__ import annotations

import importlib
import json
from pathlib import Path
import tomllib


def _reporting():
    return importlib.import_module("observatory.kalshi.checks")


def test_report_and_findings_json_label_every_standard_check_and_phase(tmp_path: Path) -> None:
    kinds = ["calibration", "favorite_longshot", "segmented", "listing_drift"]
    findings = [
        {
            "check": kind,
            "phase": "confirmation" if index % 2 else "discovery",
            "estimate": index / 10,
            "confidence_interval": [-0.1, 0.1],
            "p_value": 0.02 + index / 100,
            "q_value": 0.04 + index / 100,
        }
        for index, kind in enumerate(kinds)
    ]
    report_path = tmp_path / "report.md"
    findings_path = tmp_path / "findings.json"

    _reporting().write_outputs(findings, report_path, findings_path)

    report = report_path.read_text(encoding="utf-8").lower()
    document = json.loads(findings_path.read_text(encoding="utf-8"))
    required_labels = {
        "calibration",
        "favorite-longshot",
        "segmented",
        "listing drift",
        "discovery",
        "confirmation",
        "confidence interval",
        "multiple-testing adjusted",
        "fees",
        "not a trading signal",
    }
    assert required_labels <= {label for label in required_labels if label in report}
    assert document["findings"] == findings


def test_optional_ntfy_digest_never_raises_on_transport_failure() -> None:
    def failing_transport(*args, **kwargs):
        del args, kwargs
        raise OSError("offline")

    assert _reporting().send_ntfy_digest(
        "https://ntfy.invalid/topic", "digest", transport=failing_transport
    ) is False


def test_python_313_uv_pytest_packaging_docs_and_github_workflow() -> None:
    root = Path(__file__).parents[1]
    pyproject = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
    workflow_text = "\n".join(
        path.read_text(encoding="utf-8").lower()
        for path in (root / ".github" / "workflows").glob("*.y*ml")
    )
    readme = (root / "README.md").read_text(encoding="utf-8").lower()

    assert pyproject["project"]["requires-python"] == ">=3.13"
    assert "pytest" in pyproject["dependency-groups"]["dev"]
    assert "uv run pytest" in workflow_text
    assert "schedule:" in workflow_text
    assert "public" in readme and "never trade" in readme
