# Kalshi market observatory

This public-data observer never trades or places orders. These estimates are descriptive research and **not a trading signal**.

## How to read this

Discovery uses markets settled before 2026-04-01; the fixed confirmation window begins at that UTC boundary. Uncertainty is a 95% confidence interval clustered by event. Benjamini-Hochberg adjustment uses the latest discovery run per hypothesis and treats confirmation runs as a separate family.

Fees and returns assume a taker buys at the ask (never the midpoint) and pays the quadratic fee rounded up per order: `ceil-to-cent(0.07 × series fee multiplier × contracts × P × (1-P))`. We retain the series fee type; a missing type is assumed quadratic, any other fee type is excluded, and maker discounts are not assumed.

## Findings

Confirmation waits until the archive is complete.

### Mentions longshot YES — candidate (discovery only)

Tests whether YES contracts in Mentions markets priced from $0.10 through $0.30 one day before close have a negative mean return when bought at the ask after fees.
Result: negative as preregistered; mean return -0.462. Sample: 745 independent events (2930 contracts). Status: candidate (discovery only).
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.00-0.05` used a sample size of 6226 markets across 810 event clusters.
Estimate: -0.012. 95% confidence interval: -0.013 to -0.011. Observed range: -0.040 to 0.990.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.05-0.10` used a sample size of 553 markets across 260 event clusters.
Estimate: -0.059. 95% confidence interval: -0.069 to -0.050. Observed range: -0.090 to 0.950.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.10-0.15` used a sample size of 305 markets across 177 event clusters.
Estimate: -0.070. 95% confidence interval: -0.093 to -0.046. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.15-0.20` used a sample size of 207 markets across 132 event clusters.
Estimate: -0.092. 95% confidence interval: -0.130 to -0.054. Observed range: -0.190 to 0.850.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.20-0.25` used a sample size of 171 markets across 119 event clusters.
Estimate: -0.089. 95% confidence interval: -0.143 to -0.035. Observed range: -0.240 to 0.800.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.25-0.30` used a sample size of 131 markets across 104 event clusters.
Estimate: -0.140. 95% confidence interval: -0.197 to -0.083. Observed range: -0.290 to 0.740.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.30-0.35` used a sample size of 134 markets across 94 event clusters.
Estimate: -0.124. 95% confidence interval: -0.192 to -0.057. Observed range: -0.340 to 0.700.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.35-0.40` used a sample size of 98 markets across 70 event clusters.
Estimate: -0.141. 95% confidence interval: -0.232 to -0.051. Observed range: -0.390 to 0.650.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.004.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.40-0.45` used a sample size of 103 markets across 77 event clusters.
Estimate: -0.086. 95% confidence interval: -0.182 to 0.010. Observed range: -0.440 to 0.600.
Raw p-value: 0.080; multiple-testing adjusted q-value: 0.113.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.45-0.50` used a sample size of 96 markets across 67 event clusters.
Estimate: -0.230. 95% confidence interval: -0.320 to -0.141. Observed range: -0.490 to 0.550.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.50-0.55` used a sample size of 98 markets across 68 event clusters.
Estimate: -0.150. 95% confidence interval: -0.243 to -0.056. Observed range: -0.540 to 0.500.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.55-0.60` used a sample size of 81 markets across 62 event clusters.
Estimate: -0.164. 95% confidence interval: -0.283 to -0.044. Observed range: -0.590 to 0.450.
Raw p-value: 0.007; multiple-testing adjusted q-value: 0.012.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.60-0.65` used a sample size of 81 markets across 59 event clusters.
Estimate: -0.225. 95% confidence interval: -0.333 to -0.117. Observed range: -0.640 to 0.400.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.65-0.70` used a sample size of 69 markets across 50 event clusters.
Estimate: -0.118. 95% confidence interval: -0.238 to 0.001. Observed range: -0.690 to 0.350.
Raw p-value: 0.052; multiple-testing adjusted q-value: 0.074.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.70-0.75` used a sample size of 58 markets across 50 event clusters.
Estimate: -0.116. 95% confidence interval: -0.239 to 0.008. Observed range: -0.740 to 0.300.
Raw p-value: 0.067; multiple-testing adjusted q-value: 0.095.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.75-0.80` used a sample size of 76 markets across 54 event clusters.
Estimate: -0.138. 95% confidence interval: -0.276 to -0.000. Observed range: -0.790 to 0.250.
Raw p-value: 0.049; multiple-testing adjusted q-value: 0.072.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.80-0.85` used a sample size of 71 markets across 55 event clusters.
Estimate: -0.075. 95% confidence interval: -0.177 to 0.028. Observed range: -0.840 to 0.200.
Raw p-value: 0.153; multiple-testing adjusted q-value: 0.206.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.85-0.90` used a sample size of 124 markets across 84 event clusters.
Estimate: -0.059. 95% confidence interval: -0.132 to 0.013. Observed range: -0.890 to 0.150.
Raw p-value: 0.110; multiple-testing adjusted q-value: 0.152.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.90-0.95` used a sample size of 164 markets across 105 event clusters.
Estimate: -0.092. 95% confidence interval: -0.169 to -0.014. Observed range: -0.940 to 0.100.
Raw p-value: 0.020; multiple-testing adjusted q-value: 0.031.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.95-1.00` used a sample size of 6239 markets across 850 event clusters.
Estimate: -0.001. 95% confidence interval: -0.005 to 0.003. Observed range: -1.000 to 0.050.
Raw p-value: 0.575; multiple-testing adjusted q-value: 0.670.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.00-0.05` used a sample size of 6226 markets across 810 event clusters.
Estimate: -0.012. 95% confidence interval: -0.013 to -0.011. Observed range: -0.040 to 0.990.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.05-0.10` used a sample size of 553 markets across 260 event clusters.
Estimate: -0.059. 95% confidence interval: -0.069 to -0.050. Observed range: -0.090 to 0.950.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.10-0.15` used a sample size of 305 markets across 177 event clusters.
Estimate: -0.070. 95% confidence interval: -0.093 to -0.046. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.15-0.20` used a sample size of 207 markets across 132 event clusters.
Estimate: -0.092. 95% confidence interval: -0.130 to -0.054. Observed range: -0.190 to 0.850.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.20-0.25` used a sample size of 171 markets across 119 event clusters.
Estimate: -0.089. 95% confidence interval: -0.143 to -0.035. Observed range: -0.240 to 0.800.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.25-0.30` used a sample size of 131 markets across 104 event clusters.
Estimate: -0.140. 95% confidence interval: -0.197 to -0.083. Observed range: -0.290 to 0.740.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.30-0.35` used a sample size of 134 markets across 94 event clusters.
Estimate: -0.124. 95% confidence interval: -0.192 to -0.057. Observed range: -0.340 to 0.700.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.35-0.40` used a sample size of 98 markets across 70 event clusters.
Estimate: -0.141. 95% confidence interval: -0.232 to -0.051. Observed range: -0.390 to 0.650.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.004.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.40-0.45` used a sample size of 103 markets across 77 event clusters.
Estimate: -0.086. 95% confidence interval: -0.182 to 0.010. Observed range: -0.440 to 0.600.
Raw p-value: 0.080; multiple-testing adjusted q-value: 0.113.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.45-0.50` used a sample size of 96 markets across 67 event clusters.
Estimate: -0.230. 95% confidence interval: -0.320 to -0.141. Observed range: -0.490 to 0.550.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.50-0.55` used a sample size of 98 markets across 68 event clusters.
Estimate: -0.150. 95% confidence interval: -0.243 to -0.056. Observed range: -0.540 to 0.500.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.55-0.60` used a sample size of 81 markets across 62 event clusters.
Estimate: -0.164. 95% confidence interval: -0.283 to -0.044. Observed range: -0.590 to 0.450.
Raw p-value: 0.007; multiple-testing adjusted q-value: 0.012.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.60-0.65` used a sample size of 81 markets across 59 event clusters.
Estimate: -0.225. 95% confidence interval: -0.333 to -0.117. Observed range: -0.640 to 0.400.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.65-0.70` used a sample size of 69 markets across 50 event clusters.
Estimate: -0.118. 95% confidence interval: -0.238 to 0.001. Observed range: -0.690 to 0.350.
Raw p-value: 0.052; multiple-testing adjusted q-value: 0.074.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.70-0.75` used a sample size of 58 markets across 50 event clusters.
Estimate: -0.116. 95% confidence interval: -0.239 to 0.008. Observed range: -0.740 to 0.300.
Raw p-value: 0.067; multiple-testing adjusted q-value: 0.095.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.75-0.80` used a sample size of 76 markets across 54 event clusters.
Estimate: -0.138. 95% confidence interval: -0.276 to -0.000. Observed range: -0.790 to 0.250.
Raw p-value: 0.049; multiple-testing adjusted q-value: 0.072.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.80-0.85` used a sample size of 71 markets across 55 event clusters.
Estimate: -0.075. 95% confidence interval: -0.177 to 0.028. Observed range: -0.840 to 0.200.
Raw p-value: 0.153; multiple-testing adjusted q-value: 0.206.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.85-0.90` used a sample size of 124 markets across 84 event clusters.
Estimate: -0.059. 95% confidence interval: -0.132 to 0.013. Observed range: -0.890 to 0.150.
Raw p-value: 0.110; multiple-testing adjusted q-value: 0.152.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.90-0.95` used a sample size of 164 markets across 105 event clusters.
Estimate: -0.092. 95% confidence interval: -0.169 to -0.014. Observed range: -0.940 to 0.100.
Raw p-value: 0.020; multiple-testing adjusted q-value: 0.031.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.95-1.00` used a sample size of 6239 markets across 850 event clusters.
Estimate: -0.001. 95% confidence interval: -0.005 to 0.003. Observed range: -1.000 to 0.050.
Raw p-value: 0.575; multiple-testing adjusted q-value: 0.670.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.00-0.05` used a sample size of 576 markets across 163 event clusters.
Estimate: -0.011. 95% confidence interval: -0.017 to -0.005. Observed range: -0.040 to 0.990.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.05-0.10` used a sample size of 438 markets across 199 event clusters.
Estimate: -0.030. 95% confidence interval: -0.047 to -0.014. Observed range: -0.090 to 0.950.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.10-0.15` used a sample size of 508 markets across 283 event clusters.
Estimate: -0.047. 95% confidence interval: -0.072 to -0.022. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.15-0.20` used a sample size of 713 markets across 411 event clusters.
Estimate: -0.082. 95% confidence interval: -0.104 to -0.060. Observed range: -0.190 to 0.850.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.20-0.25` used a sample size of 809 markets across 467 event clusters.
Estimate: -0.092. 95% confidence interval: -0.116 to -0.068. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.25-0.30` used a sample size of 757 markets across 446 event clusters.
Estimate: -0.070. 95% confidence interval: -0.099 to -0.040. Observed range: -0.290 to 0.750.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.30-0.35` used a sample size of 781 markets across 474 event clusters.
Estimate: -0.100. 95% confidence interval: -0.129 to -0.071. Observed range: -0.340 to 0.700.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.35-0.40` used a sample size of 752 markets across 473 event clusters.
Estimate: -0.117. 95% confidence interval: -0.149 to -0.085. Observed range: -0.390 to 0.650.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.40-0.45` used a sample size of 687 markets across 464 event clusters.
Estimate: -0.096. 95% confidence interval: -0.134 to -0.058. Observed range: -0.440 to 0.600.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.45-0.50` used a sample size of 667 markets across 454 event clusters.
Estimate: -0.140. 95% confidence interval: -0.176 to -0.105. Observed range: -0.490 to 0.550.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.50-0.55` used a sample size of 680 markets across 437 event clusters.
Estimate: -0.118. 95% confidence interval: -0.156 to -0.081. Observed range: -0.540 to 0.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.55-0.60` used a sample size of 727 markets across 449 event clusters.
Estimate: -0.090. 95% confidence interval: -0.128 to -0.052. Observed range: -0.590 to 0.450.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.60-0.65` used a sample size of 811 markets across 496 event clusters.
Estimate: -0.131. 95% confidence interval: -0.168 to -0.095. Observed range: -0.640 to 0.400.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.65-0.70` used a sample size of 833 markets across 507 event clusters.
Estimate: -0.122. 95% confidence interval: -0.160 to -0.084. Observed range: -0.690 to 0.350.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.70-0.75` used a sample size of 778 markets across 464 event clusters.
Estimate: -0.141. 95% confidence interval: -0.180 to -0.102. Observed range: -0.740 to 0.300.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.75-0.80` used a sample size of 778 markets across 486 event clusters.
Estimate: -0.115. 95% confidence interval: -0.152 to -0.078. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.80-0.85` used a sample size of 744 markets across 475 event clusters.
Estimate: -0.103. 95% confidence interval: -0.137 to -0.068. Observed range: -0.840 to 0.200.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.85-0.90` used a sample size of 1026 markets across 498 event clusters.
Estimate: -0.095. 95% confidence interval: -0.127 to -0.062. Observed range: -0.890 to 0.150.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.90-0.95` used a sample size of 1082 markets across 503 event clusters.
Estimate: -0.106. 95% confidence interval: -0.144 to -0.067. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.95-1.00` used a sample size of 1509 markets across 457 event clusters.
Estimate: -0.061. 95% confidence interval: -0.091 to -0.031. Observed range: -1.000 to 0.050.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.00-0.05` used a sample size of 576 markets across 163 event clusters.
Estimate: -0.011. 95% confidence interval: -0.017 to -0.005. Observed range: -0.040 to 0.990.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.05-0.10` used a sample size of 438 markets across 199 event clusters.
Estimate: -0.030. 95% confidence interval: -0.047 to -0.014. Observed range: -0.090 to 0.950.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.10-0.15` used a sample size of 508 markets across 283 event clusters.
Estimate: -0.047. 95% confidence interval: -0.072 to -0.022. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.15-0.20` used a sample size of 713 markets across 411 event clusters.
Estimate: -0.082. 95% confidence interval: -0.104 to -0.060. Observed range: -0.190 to 0.850.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.20-0.25` used a sample size of 809 markets across 467 event clusters.
Estimate: -0.092. 95% confidence interval: -0.116 to -0.068. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.25-0.30` used a sample size of 757 markets across 446 event clusters.
Estimate: -0.070. 95% confidence interval: -0.099 to -0.040. Observed range: -0.290 to 0.750.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.30-0.35` used a sample size of 781 markets across 474 event clusters.
Estimate: -0.100. 95% confidence interval: -0.129 to -0.071. Observed range: -0.340 to 0.700.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.35-0.40` used a sample size of 752 markets across 473 event clusters.
Estimate: -0.117. 95% confidence interval: -0.149 to -0.085. Observed range: -0.390 to 0.650.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.40-0.45` used a sample size of 687 markets across 464 event clusters.
Estimate: -0.096. 95% confidence interval: -0.134 to -0.058. Observed range: -0.440 to 0.600.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.45-0.50` used a sample size of 667 markets across 454 event clusters.
Estimate: -0.140. 95% confidence interval: -0.176 to -0.105. Observed range: -0.490 to 0.550.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.50-0.55` used a sample size of 680 markets across 437 event clusters.
Estimate: -0.118. 95% confidence interval: -0.156 to -0.081. Observed range: -0.540 to 0.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.55-0.60` used a sample size of 727 markets across 449 event clusters.
Estimate: -0.090. 95% confidence interval: -0.128 to -0.052. Observed range: -0.590 to 0.450.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.60-0.65` used a sample size of 811 markets across 496 event clusters.
Estimate: -0.131. 95% confidence interval: -0.168 to -0.095. Observed range: -0.640 to 0.400.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.65-0.70` used a sample size of 833 markets across 507 event clusters.
Estimate: -0.122. 95% confidence interval: -0.160 to -0.084. Observed range: -0.690 to 0.350.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.70-0.75` used a sample size of 778 markets across 464 event clusters.
Estimate: -0.141. 95% confidence interval: -0.180 to -0.102. Observed range: -0.740 to 0.300.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.75-0.80` used a sample size of 778 markets across 486 event clusters.
Estimate: -0.115. 95% confidence interval: -0.152 to -0.078. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.80-0.85` used a sample size of 744 markets across 475 event clusters.
Estimate: -0.103. 95% confidence interval: -0.137 to -0.068. Observed range: -0.840 to 0.200.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.85-0.90` used a sample size of 1026 markets across 498 event clusters.
Estimate: -0.095. 95% confidence interval: -0.127 to -0.062. Observed range: -0.890 to 0.150.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.90-0.95` used a sample size of 1082 markets across 503 event clusters.
Estimate: -0.106. 95% confidence interval: -0.144 to -0.067. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.95-1.00` used a sample size of 1509 markets across 457 event clusters.
Estimate: -0.061. 95% confidence interval: -0.091 to -0.031. Observed range: -1.000 to 0.050.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.00-0.05` used a sample size of 22 markets across 11 event clusters.
Estimate: -0.028. 95% confidence interval: not available to not available. Observed range: -0.040 to -0.010.
Not tested: only 11 independent events (needs 30).

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.05-0.10` used a sample size of 70 markets across 45 event clusters.
Estimate: -0.059. 95% confidence interval: -0.088 to -0.031. Observed range: -0.090 to 0.920.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.10-0.15` used a sample size of 126 markets across 60 event clusters.
Estimate: -0.088. 95% confidence interval: -0.118 to -0.058. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.15-0.20` used a sample size of 184 markets across 99 event clusters.
Estimate: -0.064. 95% confidence interval: -0.112 to -0.016. Observed range: -0.190 to 0.850.
Raw p-value: 0.010; multiple-testing adjusted q-value: 0.015.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.20-0.25` used a sample size of 162 markets across 93 event clusters.
Estimate: -0.102. 95% confidence interval: -0.156 to -0.047. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.25-0.30` used a sample size of 152 markets across 102 event clusters.
Estimate: -0.053. 95% confidence interval: -0.132 to 0.027. Observed range: -0.290 to 0.750.
Raw p-value: 0.193; multiple-testing adjusted q-value: 0.253.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.30-0.35` used a sample size of 144 markets across 99 event clusters.
Estimate: -0.076. 95% confidence interval: -0.145 to -0.008. Observed range: -0.340 to 0.700.
Raw p-value: 0.029; multiple-testing adjusted q-value: 0.044.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.35-0.40` used a sample size of 128 markets across 93 event clusters.
Estimate: -0.144. 95% confidence interval: -0.214 to -0.074. Observed range: -0.390 to 0.650.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.40-0.45` used a sample size of 144 markets across 98 event clusters.
Estimate: -0.128. 95% confidence interval: -0.206 to -0.050. Observed range: -0.440 to 0.600.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.45-0.50` used a sample size of 163 markets across 115 event clusters.
Estimate: -0.120. 95% confidence interval: -0.203 to -0.037. Observed range: -0.490 to 0.550.
Raw p-value: 0.005; multiple-testing adjusted q-value: 0.007.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.50-0.55` used a sample size of 116 markets across 79 event clusters.
Estimate: -0.165. 95% confidence interval: -0.259 to -0.072. Observed range: -0.540 to 0.500.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.55-0.60` used a sample size of 147 markets across 84 event clusters.
Estimate: -0.120. 95% confidence interval: -0.201 to -0.038. Observed range: -0.590 to 0.450.
Raw p-value: 0.004; multiple-testing adjusted q-value: 0.007.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.60-0.65` used a sample size of 173 markets across 98 event clusters.
Estimate: -0.106. 95% confidence interval: -0.182 to -0.030. Observed range: -0.640 to 0.400.
Raw p-value: 0.006; multiple-testing adjusted q-value: 0.011.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.65-0.70` used a sample size of 183 markets across 109 event clusters.
Estimate: -0.122. 95% confidence interval: -0.199 to -0.046. Observed range: -0.690 to 0.350.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.70-0.75` used a sample size of 174 markets across 118 event clusters.
Estimate: -0.134. 95% confidence interval: -0.210 to -0.058. Observed range: -0.740 to 0.300.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.75-0.80` used a sample size of 194 markets across 116 event clusters.
Estimate: -0.209. 95% confidence interval: -0.291 to -0.127. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.80-0.85` used a sample size of 158 markets across 84 event clusters.
Estimate: -0.167. 95% confidence interval: -0.271 to -0.063. Observed range: -0.840 to 0.200.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.85-0.90` used a sample size of 147 markets across 84 event clusters.
Estimate: -0.239. 95% confidence interval: -0.344 to -0.135. Observed range: -0.890 to 0.150.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.90-0.95` used a sample size of 166 markets across 87 event clusters.
Estimate: -0.216. 95% confidence interval: -0.316 to -0.117. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.95-1.00` used a sample size of 144 markets across 64 event clusters.
Estimate: -0.155. 95% confidence interval: -0.308 to -0.002. Observed range: -1.000 to 0.050.
Raw p-value: 0.047; multiple-testing adjusted q-value: 0.068.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.00-0.05` used a sample size of 22 markets across 11 event clusters.
Estimate: -0.028. 95% confidence interval: not available to not available. Observed range: -0.040 to -0.010.
Not tested: only 11 independent events (needs 30).

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.05-0.10` used a sample size of 70 markets across 45 event clusters.
Estimate: -0.059. 95% confidence interval: -0.088 to -0.031. Observed range: -0.090 to 0.920.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.10-0.15` used a sample size of 126 markets across 60 event clusters.
Estimate: -0.088. 95% confidence interval: -0.118 to -0.058. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.15-0.20` used a sample size of 184 markets across 99 event clusters.
Estimate: -0.064. 95% confidence interval: -0.112 to -0.016. Observed range: -0.190 to 0.850.
Raw p-value: 0.010; multiple-testing adjusted q-value: 0.015.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.20-0.25` used a sample size of 162 markets across 93 event clusters.
Estimate: -0.102. 95% confidence interval: -0.156 to -0.047. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.25-0.30` used a sample size of 152 markets across 102 event clusters.
Estimate: -0.053. 95% confidence interval: -0.132 to 0.027. Observed range: -0.290 to 0.750.
Raw p-value: 0.193; multiple-testing adjusted q-value: 0.253.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.30-0.35` used a sample size of 144 markets across 99 event clusters.
Estimate: -0.076. 95% confidence interval: -0.145 to -0.008. Observed range: -0.340 to 0.700.
Raw p-value: 0.029; multiple-testing adjusted q-value: 0.044.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.35-0.40` used a sample size of 128 markets across 93 event clusters.
Estimate: -0.144. 95% confidence interval: -0.214 to -0.074. Observed range: -0.390 to 0.650.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.40-0.45` used a sample size of 144 markets across 98 event clusters.
Estimate: -0.128. 95% confidence interval: -0.206 to -0.050. Observed range: -0.440 to 0.600.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.45-0.50` used a sample size of 163 markets across 115 event clusters.
Estimate: -0.120. 95% confidence interval: -0.203 to -0.037. Observed range: -0.490 to 0.550.
Raw p-value: 0.005; multiple-testing adjusted q-value: 0.007.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.50-0.55` used a sample size of 116 markets across 79 event clusters.
Estimate: -0.165. 95% confidence interval: -0.259 to -0.072. Observed range: -0.540 to 0.500.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.55-0.60` used a sample size of 147 markets across 84 event clusters.
Estimate: -0.120. 95% confidence interval: -0.201 to -0.038. Observed range: -0.590 to 0.450.
Raw p-value: 0.004; multiple-testing adjusted q-value: 0.007.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.60-0.65` used a sample size of 173 markets across 98 event clusters.
Estimate: -0.106. 95% confidence interval: -0.182 to -0.030. Observed range: -0.640 to 0.400.
Raw p-value: 0.006; multiple-testing adjusted q-value: 0.011.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.65-0.70` used a sample size of 183 markets across 109 event clusters.
Estimate: -0.122. 95% confidence interval: -0.199 to -0.046. Observed range: -0.690 to 0.350.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.70-0.75` used a sample size of 174 markets across 118 event clusters.
Estimate: -0.134. 95% confidence interval: -0.210 to -0.058. Observed range: -0.740 to 0.300.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.75-0.80` used a sample size of 194 markets across 116 event clusters.
Estimate: -0.209. 95% confidence interval: -0.291 to -0.127. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.80-0.85` used a sample size of 158 markets across 84 event clusters.
Estimate: -0.167. 95% confidence interval: -0.271 to -0.063. Observed range: -0.840 to 0.200.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.85-0.90` used a sample size of 147 markets across 84 event clusters.
Estimate: -0.239. 95% confidence interval: -0.344 to -0.135. Observed range: -0.890 to 0.150.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.90-0.95` used a sample size of 166 markets across 87 event clusters.
Estimate: -0.216. 95% confidence interval: -0.316 to -0.117. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.95-1.00` used a sample size of 144 markets across 64 event clusters.
Estimate: -0.155. 95% confidence interval: -0.308 to -0.002. Observed range: -1.000 to 0.050.
Raw p-value: 0.047; multiple-testing adjusted q-value: 0.068.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.00-0.05:no` used a sample size of 294 markets across 138 event clusters.
Estimate: 0.003. 95% confidence interval: 0.002 to 0.004. Observed range: 0.000 to 0.020.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.00-0.05:yes` used a sample size of 5726 markets across 744 event clusters.
Estimate: -0.983. 95% confidence interval: -1.007 to -0.958. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.05-0.10:no` used a sample size of 265 markets across 142 event clusters.
Estimate: 0.003. 95% confidence interval: -0.015 to 0.021. Observed range: -1.000 to 0.075.
Raw p-value: 0.718; multiple-testing adjusted q-value: 0.799.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.05-0.10:yes` used a sample size of 572 markets across 245 event clusters.
Estimate: -0.879. 95% confidence interval: -0.987 to -0.772. Observed range: -1.000 to 13.286.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.10-0.15:no` used a sample size of 213 markets across 111 event clusters.
Estimate: 0.022. 95% confidence interval: -0.008 to 0.052. Observed range: -1.000 to 0.136.
Raw p-value: 0.157; multiple-testing adjusted q-value: 0.208.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.10-0.15:yes` used a sample size of 291 markets across 149 event clusters.
Estimate: -0.790. 95% confidence interval: -0.937 to -0.643. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.15-0.20:no` used a sample size of 168 markets across 105 event clusters.
Estimate: 0.008. 95% confidence interval: -0.042 to 0.058. Observed range: -1.000 to 0.190.
Raw p-value: 0.745; multiple-testing adjusted q-value: 0.815.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.15-0.20:yes` used a sample size of 226 markets across 140 event clusters.
Estimate: -0.661. 95% confidence interval: -0.853 to -0.469. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.20-0.25:no` used a sample size of 133 markets across 85 event clusters.
Estimate: -0.029. 95% confidence interval: -0.110 to 0.052. Observed range: -1.000 to 0.250.
Raw p-value: 0.479; multiple-testing adjusted q-value: 0.576.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.20-0.25:yes` used a sample size of 175 markets across 121 event clusters.
Estimate: -0.494. 95% confidence interval: -0.722 to -0.266. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.25-0.30:no` used a sample size of 138 markets across 98 event clusters.
Estimate: -0.005. 95% confidence interval: -0.080 to 0.070. Observed range: -1.000 to 0.351.
Raw p-value: 0.891; multiple-testing adjusted q-value: 0.924.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.25-0.30:yes` used a sample size of 167 markets across 121 event clusters.
Estimate: -0.573. 95% confidence interval: -0.748 to -0.398. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.30-0.35:no` used a sample size of 113 markets across 76 event clusters.
Estimate: 0.001. 95% confidence interval: -0.107 to 0.110. Observed range: -1.000 to 0.449.
Raw p-value: 0.979; multiple-testing adjusted q-value: 0.999.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.30-0.35:yes` used a sample size of 151 markets across 99 event clusters.
Estimate: -0.552. 95% confidence interval: -0.740 to -0.365. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.35-0.40:no` used a sample size of 84 markets across 62 event clusters.
Estimate: 0.043. 95% confidence interval: -0.087 to 0.172. Observed range: -1.000 to 0.562.
Raw p-value: 0.517; multiple-testing adjusted q-value: 0.614.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.35-0.40:yes` used a sample size of 107 markets across 78 event clusters.
Estimate: -0.569. 95% confidence interval: -0.766 to -0.373. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.40-0.45:no` used a sample size of 89 markets across 68 event clusters.
Estimate: -0.017. 95% confidence interval: -0.152 to 0.119. Observed range: -1.000 to 0.695.
Raw p-value: 0.808; multiple-testing adjusted q-value: 0.857.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.40-0.45:yes` used a sample size of 100 markets across 76 event clusters.
Estimate: -0.434. 95% confidence interval: -0.635 to -0.232. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.45-0.50:no` used a sample size of 93 markets across 69 event clusters.
Estimate: 0.051. 95% confidence interval: -0.107 to 0.210. Observed range: -1.000 to 0.818.
Raw p-value: 0.526; multiple-testing adjusted q-value: 0.621.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.45-0.50:yes` used a sample size of 114 markets across 82 event clusters.
Estimate: -0.541. 95% confidence interval: -0.714 to -0.369. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.50-0.55:no` used a sample size of 77 markets across 53 event clusters.
Estimate: -0.036. 95% confidence interval: -0.213 to 0.141. Observed range: -1.000 to 1.041.
Raw p-value: 0.690; multiple-testing adjusted q-value: 0.781.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.50-0.55:yes` used a sample size of 92 markets across 63 event clusters.
Estimate: -0.421. 95% confidence interval: -0.601 to -0.240. Observed range: -1.000 to 0.923.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.55-0.60:no` used a sample size of 81 markets across 60 event clusters.
Estimate: -0.040. 95% confidence interval: -0.261 to 0.181. Observed range: -1.000 to 1.273.
Raw p-value: 0.723; multiple-testing adjusted q-value: 0.800.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.55-0.60:yes` used a sample size of 90 markets across 68 event clusters.
Estimate: -0.303. 95% confidence interval: -0.488 to -0.118. Observed range: -1.000 to 0.754.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.60-0.65:no` used a sample size of 65 markets across 48 event clusters.
Estimate: 0.228. 95% confidence interval: 0.011 to 0.445. Observed range: -1.000 to 1.564.
Raw p-value: 0.040; multiple-testing adjusted q-value: 0.058.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.60-0.65:yes` used a sample size of 70 markets across 52 event clusters.
Estimate: -0.485. 95% confidence interval: -0.652 to -0.318. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.65-0.70:no` used a sample size of 70 markets across 51 event clusters.
Estimate: 0.051. 95% confidence interval: -0.215 to 0.317. Observed range: -1.000 to 1.778.
Raw p-value: 0.708; multiple-testing adjusted q-value: 0.792.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.65-0.70:yes` used a sample size of 72 markets across 53 event clusters.
Estimate: -0.375. 95% confidence interval: -0.559 to -0.191. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.70-0.75:no` used a sample size of 71 markets across 53 event clusters.
Estimate: -0.020. 95% confidence interval: -0.360 to 0.321. Observed range: -1.000 to 2.333.
Raw p-value: 0.910; multiple-testing adjusted q-value: 0.939.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.70-0.75:yes` used a sample size of 75 markets across 56 event clusters.
Estimate: -0.261. 95% confidence interval: -0.435 to -0.086. Observed range: -1.000 to 0.389.
Raw p-value: 0.003; multiple-testing adjusted q-value: 0.006.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.75-0.80:no` used a sample size of 66 markets across 49 event clusters.
Estimate: -0.092. 95% confidence interval: -0.532 to 0.348. Observed range: -1.000 to 3.167.
Raw p-value: 0.682; multiple-testing adjusted q-value: 0.776.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.75-0.80:yes` used a sample size of 79 markets across 56 event clusters.
Estimate: -0.325. 95% confidence interval: -0.510 to -0.140. Observed range: -1.000 to 0.299.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.80-0.85:no` used a sample size of 70 markets across 50 event clusters.
Estimate: -0.380. 95% confidence interval: -0.690 to -0.070. Observed range: -1.000 to 3.762.
Raw p-value: 0.016; multiple-testing adjusted q-value: 0.025.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.80-0.85:yes` used a sample size of 77 markets across 56 event clusters.
Estimate: -0.223. 95% confidence interval: -0.376 to -0.070. Observed range: -1.000 to 0.220.
Raw p-value: 0.004; multiple-testing adjusted q-value: 0.007.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.85-0.90:no` used a sample size of 108 markets across 63 event clusters.
Estimate: -0.208. 95% confidence interval: -0.521 to 0.104. Observed range: -1.000 to 6.143.
Raw p-value: 0.190; multiple-testing adjusted q-value: 0.252.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.85-0.90:yes` used a sample size of 115 markets across 70 event clusters.
Estimate: -0.204. 95% confidence interval: -0.296 to -0.111. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.90-0.95:no` used a sample size of 115 markets across 69 event clusters.
Estimate: -0.300. 95% confidence interval: -0.705 to 0.105. Observed range: -1.000 to 10.111.
Raw p-value: 0.146; multiple-testing adjusted q-value: 0.200.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.90-0.95:yes` used a sample size of 126 markets across 76 event clusters.
Estimate: -0.198. 95% confidence interval: -0.310 to -0.086. Observed range: -1.000 to 0.099.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.95-1.00:no` used a sample size of 6024 markets across 821 event clusters.
Estimate: -0.979. 95% confidence interval: -0.998 to -0.960. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.95-1.00:yes` used a sample size of 245 markets across 136 event clusters.
Estimate: -0.184. 95% confidence interval: -0.262 to -0.105. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.00-0.05:no` used a sample size of 294 markets across 138 event clusters.
Estimate: 0.003. 95% confidence interval: 0.002 to 0.004. Observed range: 0.000 to 0.020.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.00-0.05:yes` used a sample size of 5726 markets across 744 event clusters.
Estimate: -0.983. 95% confidence interval: -1.007 to -0.958. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.05-0.10:no` used a sample size of 265 markets across 142 event clusters.
Estimate: 0.003. 95% confidence interval: -0.015 to 0.021. Observed range: -1.000 to 0.075.
Raw p-value: 0.718; multiple-testing adjusted q-value: 0.799.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.05-0.10:yes` used a sample size of 572 markets across 245 event clusters.
Estimate: -0.879. 95% confidence interval: -0.987 to -0.772. Observed range: -1.000 to 13.286.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.10-0.15:no` used a sample size of 213 markets across 111 event clusters.
Estimate: 0.022. 95% confidence interval: -0.008 to 0.052. Observed range: -1.000 to 0.136.
Raw p-value: 0.157; multiple-testing adjusted q-value: 0.208.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.10-0.15:yes` used a sample size of 291 markets across 149 event clusters.
Estimate: -0.790. 95% confidence interval: -0.937 to -0.643. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.15-0.20:no` used a sample size of 168 markets across 105 event clusters.
Estimate: 0.008. 95% confidence interval: -0.042 to 0.058. Observed range: -1.000 to 0.190.
Raw p-value: 0.745; multiple-testing adjusted q-value: 0.815.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.15-0.20:yes` used a sample size of 226 markets across 140 event clusters.
Estimate: -0.661. 95% confidence interval: -0.853 to -0.469. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.20-0.25:no` used a sample size of 133 markets across 85 event clusters.
Estimate: -0.029. 95% confidence interval: -0.110 to 0.052. Observed range: -1.000 to 0.250.
Raw p-value: 0.479; multiple-testing adjusted q-value: 0.576.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.20-0.25:yes` used a sample size of 175 markets across 121 event clusters.
Estimate: -0.494. 95% confidence interval: -0.722 to -0.266. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.25-0.30:no` used a sample size of 138 markets across 98 event clusters.
Estimate: -0.005. 95% confidence interval: -0.080 to 0.070. Observed range: -1.000 to 0.351.
Raw p-value: 0.891; multiple-testing adjusted q-value: 0.924.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.25-0.30:yes` used a sample size of 167 markets across 121 event clusters.
Estimate: -0.573. 95% confidence interval: -0.748 to -0.398. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.30-0.35:no` used a sample size of 113 markets across 76 event clusters.
Estimate: 0.001. 95% confidence interval: -0.107 to 0.110. Observed range: -1.000 to 0.449.
Raw p-value: 0.979; multiple-testing adjusted q-value: 0.999.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.30-0.35:yes` used a sample size of 151 markets across 99 event clusters.
Estimate: -0.552. 95% confidence interval: -0.740 to -0.365. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.35-0.40:no` used a sample size of 84 markets across 62 event clusters.
Estimate: 0.043. 95% confidence interval: -0.087 to 0.172. Observed range: -1.000 to 0.562.
Raw p-value: 0.517; multiple-testing adjusted q-value: 0.614.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.35-0.40:yes` used a sample size of 107 markets across 78 event clusters.
Estimate: -0.569. 95% confidence interval: -0.766 to -0.373. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.40-0.45:no` used a sample size of 89 markets across 68 event clusters.
Estimate: -0.017. 95% confidence interval: -0.152 to 0.119. Observed range: -1.000 to 0.695.
Raw p-value: 0.808; multiple-testing adjusted q-value: 0.857.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.40-0.45:yes` used a sample size of 100 markets across 76 event clusters.
Estimate: -0.434. 95% confidence interval: -0.635 to -0.232. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.45-0.50:no` used a sample size of 93 markets across 69 event clusters.
Estimate: 0.051. 95% confidence interval: -0.107 to 0.210. Observed range: -1.000 to 0.818.
Raw p-value: 0.526; multiple-testing adjusted q-value: 0.621.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.45-0.50:yes` used a sample size of 114 markets across 82 event clusters.
Estimate: -0.541. 95% confidence interval: -0.714 to -0.369. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.50-0.55:no` used a sample size of 77 markets across 53 event clusters.
Estimate: -0.036. 95% confidence interval: -0.213 to 0.141. Observed range: -1.000 to 1.041.
Raw p-value: 0.690; multiple-testing adjusted q-value: 0.781.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.50-0.55:yes` used a sample size of 92 markets across 63 event clusters.
Estimate: -0.421. 95% confidence interval: -0.601 to -0.240. Observed range: -1.000 to 0.923.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.55-0.60:no` used a sample size of 81 markets across 60 event clusters.
Estimate: -0.040. 95% confidence interval: -0.261 to 0.181. Observed range: -1.000 to 1.273.
Raw p-value: 0.723; multiple-testing adjusted q-value: 0.800.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.55-0.60:yes` used a sample size of 90 markets across 68 event clusters.
Estimate: -0.303. 95% confidence interval: -0.488 to -0.118. Observed range: -1.000 to 0.754.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.60-0.65:no` used a sample size of 65 markets across 48 event clusters.
Estimate: 0.228. 95% confidence interval: 0.011 to 0.445. Observed range: -1.000 to 1.564.
Raw p-value: 0.040; multiple-testing adjusted q-value: 0.058.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.60-0.65:yes` used a sample size of 70 markets across 52 event clusters.
Estimate: -0.485. 95% confidence interval: -0.652 to -0.318. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.65-0.70:no` used a sample size of 70 markets across 51 event clusters.
Estimate: 0.051. 95% confidence interval: -0.215 to 0.317. Observed range: -1.000 to 1.778.
Raw p-value: 0.708; multiple-testing adjusted q-value: 0.792.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.65-0.70:yes` used a sample size of 72 markets across 53 event clusters.
Estimate: -0.375. 95% confidence interval: -0.559 to -0.191. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.70-0.75:no` used a sample size of 71 markets across 53 event clusters.
Estimate: -0.020. 95% confidence interval: -0.360 to 0.321. Observed range: -1.000 to 2.333.
Raw p-value: 0.910; multiple-testing adjusted q-value: 0.939.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.70-0.75:yes` used a sample size of 75 markets across 56 event clusters.
Estimate: -0.261. 95% confidence interval: -0.435 to -0.086. Observed range: -1.000 to 0.389.
Raw p-value: 0.003; multiple-testing adjusted q-value: 0.006.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.75-0.80:no` used a sample size of 66 markets across 49 event clusters.
Estimate: -0.092. 95% confidence interval: -0.532 to 0.348. Observed range: -1.000 to 3.167.
Raw p-value: 0.682; multiple-testing adjusted q-value: 0.776.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.75-0.80:yes` used a sample size of 79 markets across 56 event clusters.
Estimate: -0.325. 95% confidence interval: -0.510 to -0.140. Observed range: -1.000 to 0.299.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.80-0.85:no` used a sample size of 70 markets across 50 event clusters.
Estimate: -0.380. 95% confidence interval: -0.690 to -0.070. Observed range: -1.000 to 3.762.
Raw p-value: 0.016; multiple-testing adjusted q-value: 0.025.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.80-0.85:yes` used a sample size of 77 markets across 56 event clusters.
Estimate: -0.223. 95% confidence interval: -0.376 to -0.070. Observed range: -1.000 to 0.220.
Raw p-value: 0.004; multiple-testing adjusted q-value: 0.007.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.85-0.90:no` used a sample size of 108 markets across 63 event clusters.
Estimate: -0.208. 95% confidence interval: -0.521 to 0.104. Observed range: -1.000 to 6.143.
Raw p-value: 0.190; multiple-testing adjusted q-value: 0.252.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.85-0.90:yes` used a sample size of 115 markets across 70 event clusters.
Estimate: -0.204. 95% confidence interval: -0.296 to -0.111. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.90-0.95:no` used a sample size of 115 markets across 69 event clusters.
Estimate: -0.300. 95% confidence interval: -0.705 to 0.105. Observed range: -1.000 to 10.111.
Raw p-value: 0.146; multiple-testing adjusted q-value: 0.200.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.90-0.95:yes` used a sample size of 126 markets across 76 event clusters.
Estimate: -0.198. 95% confidence interval: -0.310 to -0.086. Observed range: -1.000 to 0.099.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.95-1.00:no` used a sample size of 6024 markets across 821 event clusters.
Estimate: -0.979. 95% confidence interval: -0.998 to -0.960. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.95-1.00:yes` used a sample size of 245 markets across 136 event clusters.
Estimate: -0.184. 95% confidence interval: -0.262 to -0.105. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.00-0.05:no` used a sample size of 84 markets across 46 event clusters.
Estimate: 0.009. 95% confidence interval: 0.007 to 0.011. Observed range: 0.000 to 0.020.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.00-0.05:yes` used a sample size of 528 markets across 141 event clusters.
Estimate: -1.000. 95% confidence interval: -1.000 to -1.000. Observed range: -1.000 to -1.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.05-0.10:no` used a sample size of 314 markets across 153 event clusters.
Estimate: -0.002. 95% confidence interval: -0.022 to 0.018. Observed range: -1.000 to 0.075.
Raw p-value: 0.828; multiple-testing adjusted q-value: 0.864.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.05-0.10:yes` used a sample size of 410 markets across 177 event clusters.
Estimate: -0.671. 95% confidence interval: -0.847 to -0.494. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.10-0.15:no` used a sample size of 453 markets across 254 event clusters.
Estimate: 0.001. 95% confidence interval: -0.025 to 0.026. Observed range: -1.000 to 0.136.
Raw p-value: 0.966; multiple-testing adjusted q-value: 0.992.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.10-0.15:yes` used a sample size of 481 markets across 268 event clusters.
Estimate: -0.531. 95% confidence interval: -0.707 to -0.355. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.15-0.20:no` used a sample size of 694 markets across 390 event clusters.
Estimate: 0.027. 95% confidence interval: 0.003 to 0.052. Observed range: -1.000 to 0.190.
Raw p-value: 0.030; multiple-testing adjusted q-value: 0.044.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.15-0.20:yes` used a sample size of 710 markets across 398 event clusters.
Estimate: -0.528. 95% confidence interval: -0.645 to -0.411. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.20-0.25:no` used a sample size of 770 markets across 454 event clusters.
Estimate: 0.031. 95% confidence interval: 0.003 to 0.059. Observed range: -1.000 to 0.266.
Raw p-value: 0.032; multiple-testing adjusted q-value: 0.048.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.20-0.25:yes` used a sample size of 793 markets across 468 event clusters.
Estimate: -0.509. 95% confidence interval: -0.607 to -0.410. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.25-0.30:no` used a sample size of 732 markets across 428 event clusters.
Estimate: -0.015. 95% confidence interval: -0.052 to 0.022. Observed range: -1.000 to 0.351.
Raw p-value: 0.427; multiple-testing adjusted q-value: 0.524.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.25-0.30:yes` used a sample size of 758 markets across 440 event clusters.
Estimate: -0.311. 95% confidence interval: -0.412 to -0.211. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.30-0.35:no` used a sample size of 750 markets across 460 event clusters.
Estimate: 0.033. 95% confidence interval: -0.006 to 0.071. Observed range: -1.000 to 0.449.
Raw p-value: 0.093; multiple-testing adjusted q-value: 0.130.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.30-0.35:yes` used a sample size of 768 markets across 472 event clusters.
Estimate: -0.404. 95% confidence interval: -0.488 to -0.320. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.35-0.40:no` used a sample size of 749 markets across 466 event clusters.
Estimate: 0.033. 95% confidence interval: -0.012 to 0.078. Observed range: -1.000 to 0.562.
Raw p-value: 0.151; multiple-testing adjusted q-value: 0.205.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.35-0.40:yes` used a sample size of 762 markets across 472 event clusters.
Estimate: -0.378. 95% confidence interval: -0.461 to -0.295. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.40-0.45:no` used a sample size of 654 markets across 445 event clusters.
Estimate: 0.007. 95% confidence interval: -0.049 to 0.063. Observed range: -1.000 to 0.695.
Raw p-value: 0.814; multiple-testing adjusted q-value: 0.858.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.40-0.45:yes` used a sample size of 666 markets across 451 event clusters.
Estimate: -0.304. 95% confidence interval: -0.388 to -0.219. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.45-0.50:no` used a sample size of 631 markets across 429 event clusters.
Estimate: 0.037. 95% confidence interval: -0.021 to 0.094. Observed range: -1.000 to 0.852.
Raw p-value: 0.211; multiple-testing adjusted q-value: 0.276.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.45-0.50:yes` used a sample size of 645 markets across 437 event clusters.
Estimate: -0.343. 95% confidence interval: -0.416 to -0.270. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.50-0.55:no` used a sample size of 636 markets across 407 event clusters.
Estimate: -0.009. 95% confidence interval: -0.073 to 0.055. Observed range: -1.000 to 1.041.
Raw p-value: 0.781; multiple-testing adjusted q-value: 0.835.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.50-0.55:yes` used a sample size of 651 markets across 416 event clusters.
Estimate: -0.275. 95% confidence interval: -0.344 to -0.206. Observed range: -1.000 to 0.923.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.55-0.60:no` used a sample size of 700 markets across 437 event clusters.
Estimate: -0.034. 95% confidence interval: -0.110 to 0.041. Observed range: -1.000 to 1.273.
Raw p-value: 0.374; multiple-testing adjusted q-value: 0.467.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.55-0.60:yes` used a sample size of 703 markets across 440 event clusters.
Estimate: -0.186. 95% confidence interval: -0.252 to -0.119. Observed range: -1.000 to 0.754.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.60-0.65:no` used a sample size of 777 markets across 480 event clusters.
Estimate: 0.096. 95% confidence interval: 0.016 to 0.176. Observed range: -1.000 to 1.564.
Raw p-value: 0.018; multiple-testing adjusted q-value: 0.028.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.60-0.65:yes` used a sample size of 781 markets across 483 event clusters.
Estimate: -0.280. 95% confidence interval: -0.339 to -0.222. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.65-0.70:no` used a sample size of 859 markets across 507 event clusters.
Estimate: 0.022. 95% confidence interval: -0.061 to 0.104. Observed range: -1.000 to 1.941.
Raw p-value: 0.608; multiple-testing adjusted q-value: 0.701.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.65-0.70:yes` used a sample size of 869 markets across 514 event clusters.
Estimate: -0.233. 95% confidence interval: -0.287 to -0.179. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.70-0.75:no` used a sample size of 776 markets across 463 event clusters.
Estimate: 0.015. 95% confidence interval: -0.087 to 0.117. Observed range: -1.000 to 2.448.
Raw p-value: 0.775; multiple-testing adjusted q-value: 0.834.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.70-0.75:yes` used a sample size of 782 markets across 469 event clusters.
Estimate: -0.210. 95% confidence interval: -0.263 to -0.156. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.75-0.80:no` used a sample size of 780 markets across 480 event clusters.
Estimate: -0.074. 95% confidence interval: -0.177 to 0.028. Observed range: -1.000 to 3.167.
Raw p-value: 0.156; multiple-testing adjusted q-value: 0.208.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.75-0.80:yes` used a sample size of 788 markets across 486 event clusters.
Estimate: -0.190. 95% confidence interval: -0.236 to -0.144. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.80-0.85:no` used a sample size of 761 markets across 475 event clusters.
Estimate: -0.115. 95% confidence interval: -0.237 to 0.007. Observed range: -1.000 to 4.556.
Raw p-value: 0.064; multiple-testing adjusted q-value: 0.091.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.80-0.85:yes` used a sample size of 768 markets across 481 event clusters.
Estimate: -0.153. 95% confidence interval: -0.196 to -0.110. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.85-0.90:no` used a sample size of 1027 markets across 487 event clusters.
Estimate: -0.340. 95% confidence interval: -0.435 to -0.244. Observed range: -1.000 to 6.692.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.85-0.90:yes` used a sample size of 1045 markets across 488 event clusters.
Estimate: -0.126. 95% confidence interval: -0.163 to -0.089. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.90-0.95:no` used a sample size of 1061 markets across 501 event clusters.
Estimate: -0.245. 95% confidence interval: -0.395 to -0.094. Observed range: -1.000 to 11.500.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.003.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.90-0.95:yes` used a sample size of 1083 markets across 504 event clusters.
Estimate: -0.137. 95% confidence interval: -0.179 to -0.095. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.95-1.00:no` used a sample size of 1605 markets across 486 event clusters.
Estimate: -0.687. 95% confidence interval: -0.805 to -0.569. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.95-1.00:yes` used a sample size of 993 markets across 413 event clusters.
Estimate: -0.106. 95% confidence interval: -0.152 to -0.060. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.00-0.05:no` used a sample size of 84 markets across 46 event clusters.
Estimate: 0.009. 95% confidence interval: 0.007 to 0.011. Observed range: 0.000 to 0.020.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.00-0.05:yes` used a sample size of 528 markets across 141 event clusters.
Estimate: -1.000. 95% confidence interval: -1.000 to -1.000. Observed range: -1.000 to -1.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.05-0.10:no` used a sample size of 314 markets across 153 event clusters.
Estimate: -0.002. 95% confidence interval: -0.022 to 0.018. Observed range: -1.000 to 0.075.
Raw p-value: 0.828; multiple-testing adjusted q-value: 0.864.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.05-0.10:yes` used a sample size of 410 markets across 177 event clusters.
Estimate: -0.671. 95% confidence interval: -0.847 to -0.494. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.10-0.15:no` used a sample size of 453 markets across 254 event clusters.
Estimate: 0.001. 95% confidence interval: -0.025 to 0.026. Observed range: -1.000 to 0.136.
Raw p-value: 0.966; multiple-testing adjusted q-value: 0.992.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.10-0.15:yes` used a sample size of 481 markets across 268 event clusters.
Estimate: -0.531. 95% confidence interval: -0.707 to -0.355. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.15-0.20:no` used a sample size of 694 markets across 390 event clusters.
Estimate: 0.027. 95% confidence interval: 0.003 to 0.052. Observed range: -1.000 to 0.190.
Raw p-value: 0.030; multiple-testing adjusted q-value: 0.044.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.15-0.20:yes` used a sample size of 710 markets across 398 event clusters.
Estimate: -0.528. 95% confidence interval: -0.645 to -0.411. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.20-0.25:no` used a sample size of 770 markets across 454 event clusters.
Estimate: 0.031. 95% confidence interval: 0.003 to 0.059. Observed range: -1.000 to 0.266.
Raw p-value: 0.032; multiple-testing adjusted q-value: 0.048.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.20-0.25:yes` used a sample size of 793 markets across 468 event clusters.
Estimate: -0.509. 95% confidence interval: -0.607 to -0.410. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.25-0.30:no` used a sample size of 732 markets across 428 event clusters.
Estimate: -0.015. 95% confidence interval: -0.052 to 0.022. Observed range: -1.000 to 0.351.
Raw p-value: 0.427; multiple-testing adjusted q-value: 0.524.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.25-0.30:yes` used a sample size of 758 markets across 440 event clusters.
Estimate: -0.311. 95% confidence interval: -0.412 to -0.211. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.30-0.35:no` used a sample size of 750 markets across 460 event clusters.
Estimate: 0.033. 95% confidence interval: -0.006 to 0.071. Observed range: -1.000 to 0.449.
Raw p-value: 0.093; multiple-testing adjusted q-value: 0.130.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.30-0.35:yes` used a sample size of 768 markets across 472 event clusters.
Estimate: -0.404. 95% confidence interval: -0.488 to -0.320. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.35-0.40:no` used a sample size of 749 markets across 466 event clusters.
Estimate: 0.033. 95% confidence interval: -0.012 to 0.078. Observed range: -1.000 to 0.562.
Raw p-value: 0.151; multiple-testing adjusted q-value: 0.205.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.35-0.40:yes` used a sample size of 762 markets across 472 event clusters.
Estimate: -0.378. 95% confidence interval: -0.461 to -0.295. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.40-0.45:no` used a sample size of 654 markets across 445 event clusters.
Estimate: 0.007. 95% confidence interval: -0.049 to 0.063. Observed range: -1.000 to 0.695.
Raw p-value: 0.814; multiple-testing adjusted q-value: 0.858.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.40-0.45:yes` used a sample size of 666 markets across 451 event clusters.
Estimate: -0.304. 95% confidence interval: -0.388 to -0.219. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.45-0.50:no` used a sample size of 631 markets across 429 event clusters.
Estimate: 0.037. 95% confidence interval: -0.021 to 0.094. Observed range: -1.000 to 0.852.
Raw p-value: 0.211; multiple-testing adjusted q-value: 0.276.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.45-0.50:yes` used a sample size of 645 markets across 437 event clusters.
Estimate: -0.343. 95% confidence interval: -0.416 to -0.270. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.50-0.55:no` used a sample size of 636 markets across 407 event clusters.
Estimate: -0.009. 95% confidence interval: -0.073 to 0.055. Observed range: -1.000 to 1.041.
Raw p-value: 0.781; multiple-testing adjusted q-value: 0.835.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.50-0.55:yes` used a sample size of 651 markets across 416 event clusters.
Estimate: -0.275. 95% confidence interval: -0.344 to -0.206. Observed range: -1.000 to 0.923.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.55-0.60:no` used a sample size of 700 markets across 437 event clusters.
Estimate: -0.034. 95% confidence interval: -0.110 to 0.041. Observed range: -1.000 to 1.273.
Raw p-value: 0.374; multiple-testing adjusted q-value: 0.467.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.55-0.60:yes` used a sample size of 703 markets across 440 event clusters.
Estimate: -0.186. 95% confidence interval: -0.252 to -0.119. Observed range: -1.000 to 0.754.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.60-0.65:no` used a sample size of 777 markets across 480 event clusters.
Estimate: 0.096. 95% confidence interval: 0.016 to 0.176. Observed range: -1.000 to 1.564.
Raw p-value: 0.018; multiple-testing adjusted q-value: 0.028.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.60-0.65:yes` used a sample size of 781 markets across 483 event clusters.
Estimate: -0.280. 95% confidence interval: -0.339 to -0.222. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.65-0.70:no` used a sample size of 859 markets across 507 event clusters.
Estimate: 0.022. 95% confidence interval: -0.061 to 0.104. Observed range: -1.000 to 1.941.
Raw p-value: 0.608; multiple-testing adjusted q-value: 0.701.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.65-0.70:yes` used a sample size of 869 markets across 514 event clusters.
Estimate: -0.233. 95% confidence interval: -0.287 to -0.179. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.70-0.75:no` used a sample size of 776 markets across 463 event clusters.
Estimate: 0.015. 95% confidence interval: -0.087 to 0.117. Observed range: -1.000 to 2.448.
Raw p-value: 0.775; multiple-testing adjusted q-value: 0.834.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.70-0.75:yes` used a sample size of 782 markets across 469 event clusters.
Estimate: -0.210. 95% confidence interval: -0.263 to -0.156. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.75-0.80:no` used a sample size of 780 markets across 480 event clusters.
Estimate: -0.074. 95% confidence interval: -0.177 to 0.028. Observed range: -1.000 to 3.167.
Raw p-value: 0.156; multiple-testing adjusted q-value: 0.208.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.75-0.80:yes` used a sample size of 788 markets across 486 event clusters.
Estimate: -0.190. 95% confidence interval: -0.236 to -0.144. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.80-0.85:no` used a sample size of 761 markets across 475 event clusters.
Estimate: -0.115. 95% confidence interval: -0.237 to 0.007. Observed range: -1.000 to 4.556.
Raw p-value: 0.064; multiple-testing adjusted q-value: 0.091.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.80-0.85:yes` used a sample size of 768 markets across 481 event clusters.
Estimate: -0.153. 95% confidence interval: -0.196 to -0.110. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.85-0.90:no` used a sample size of 1027 markets across 487 event clusters.
Estimate: -0.340. 95% confidence interval: -0.435 to -0.244. Observed range: -1.000 to 6.692.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.85-0.90:yes` used a sample size of 1045 markets across 488 event clusters.
Estimate: -0.126. 95% confidence interval: -0.163 to -0.089. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.90-0.95:no` used a sample size of 1061 markets across 501 event clusters.
Estimate: -0.245. 95% confidence interval: -0.395 to -0.094. Observed range: -1.000 to 11.500.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.003.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.90-0.95:yes` used a sample size of 1083 markets across 504 event clusters.
Estimate: -0.137. 95% confidence interval: -0.179 to -0.095. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.95-1.00:no` used a sample size of 1605 markets across 486 event clusters.
Estimate: -0.687. 95% confidence interval: -0.805 to -0.569. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.95-1.00:yes` used a sample size of 993 markets across 413 event clusters.
Estimate: -0.106. 95% confidence interval: -0.152 to -0.060. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.00-0.05:no` used a sample size of 13 markets across 9 event clusters.
Estimate: 0.011. 95% confidence interval: not available to not available. Observed range: 0.000 to 0.020.
Not tested: only 9 independent events (needs 30).

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.00-0.05:yes` used a sample size of 22 markets across 11 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 11 independent events (needs 30).

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.05-0.10:no` used a sample size of 59 markets across 39 event clusters.
Estimate: 0.015. 95% confidence interval: -0.021 to 0.050. Observed range: -1.000 to 0.075.
Raw p-value: 0.417; multiple-testing adjusted q-value: 0.515.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.05-0.10:yes` used a sample size of 66 markets across 44 event clusters.
Estimate: -0.848. 95% confidence interval: -1.149 to -0.548. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.10-0.15:no` used a sample size of 119 markets across 59 event clusters.
Estimate: 0.020. 95% confidence interval: -0.014 to 0.054. Observed range: -1.000 to 0.136.
Raw p-value: 0.253; multiple-testing adjusted q-value: 0.326.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.10-0.15:yes` used a sample size of 122 markets across 59 event clusters.
Estimate: -0.714. 95% confidence interval: -0.984 to -0.445. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.15-0.20:no` used a sample size of 183 markets across 93 event clusters.
Estimate: -0.009. 95% confidence interval: -0.066 to 0.048. Observed range: -1.000 to 0.190.
Raw p-value: 0.752; multiple-testing adjusted q-value: 0.818.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.15-0.20:yes` used a sample size of 183 markets across 93 event clusters.
Estimate: -0.426. 95% confidence interval: -0.683 to -0.170. Observed range: -1.000 to 5.250.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.20-0.25:no` used a sample size of 146 markets across 91 event clusters.
Estimate: 0.037. 95% confidence interval: -0.027 to 0.102. Observed range: -1.000 to 0.266.
Raw p-value: 0.258; multiple-testing adjusted q-value: 0.330.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.20-0.25:yes` used a sample size of 146 markets across 91 event clusters.
Estimate: -0.530. 95% confidence interval: -0.770 to -0.290. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.25-0.30:no` used a sample size of 145 markets across 103 event clusters.
Estimate: -0.027. 95% confidence interval: -0.119 to 0.065. Observed range: -1.000 to 0.351.
Raw p-value: 0.566; multiple-testing adjusted q-value: 0.664.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.25-0.30:yes` used a sample size of 145 markets across 103 event clusters.
Estimate: -0.318. 95% confidence interval: -0.576 to -0.059. Observed range: -1.000 to 2.704.
Raw p-value: 0.016; multiple-testing adjusted q-value: 0.025.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.30-0.35:no` used a sample size of 144 markets across 98 event clusters.
Estimate: -0.024. 95% confidence interval: -0.113 to 0.065. Observed range: -1.000 to 0.449.
Raw p-value: 0.600; multiple-testing adjusted q-value: 0.696.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.30-0.35:yes` used a sample size of 144 markets across 98 event clusters.
Estimate: -0.247. 95% confidence interval: -0.448 to -0.046. Observed range: -1.000 to 2.125.
Raw p-value: 0.016; multiple-testing adjusted q-value: 0.025.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.35-0.40:no` used a sample size of 137 markets across 98 event clusters.
Estimate: 0.053. 95% confidence interval: -0.042 to 0.148. Observed range: -1.000 to 0.562.
Raw p-value: 0.275; multiple-testing adjusted q-value: 0.349.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.35-0.40:yes` used a sample size of 137 markets across 98 event clusters.
Estimate: -0.442. 95% confidence interval: -0.620 to -0.263. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.40-0.45:no` used a sample size of 142 markets across 96 event clusters.
Estimate: 0.058. 95% confidence interval: -0.055 to 0.171. Observed range: -1.000 to 0.695.
Raw p-value: 0.314; multiple-testing adjusted q-value: 0.396.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.40-0.45:yes` used a sample size of 142 markets across 96 event clusters.
Estimate: -0.391. 95% confidence interval: -0.566 to -0.215. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.45-0.50:no` used a sample size of 159 markets across 112 event clusters.
Estimate: 0.022. 95% confidence interval: -0.108 to 0.152. Observed range: -1.000 to 0.852.
Raw p-value: 0.742; multiple-testing adjusted q-value: 0.815.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.45-0.50:yes` used a sample size of 161 markets across 114 event clusters.
Estimate: -0.302. 95% confidence interval: -0.470 to -0.134. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.50-0.55:no` used a sample size of 110 markets across 76 event clusters.
Estimate: 0.062. 95% confidence interval: -0.107 to 0.230. Observed range: -1.000 to 1.041.
Raw p-value: 0.472; multiple-testing adjusted q-value: 0.571.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.50-0.55:yes` used a sample size of 111 markets across 77 event clusters.
Estimate: -0.295. 95% confidence interval: -0.470 to -0.121. Observed range: -1.000 to 0.923.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.55-0.60:no` used a sample size of 149 markets across 79 event clusters.
Estimate: 0.060. 95% confidence interval: -0.092 to 0.212. Observed range: -1.000 to 1.273.
Raw p-value: 0.441; multiple-testing adjusted q-value: 0.537.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.55-0.60:yes` used a sample size of 149 markets across 79 event clusters.
Estimate: -0.271. 95% confidence interval: -0.413 to -0.129. Observed range: -1.000 to 0.754.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.60-0.65:no` used a sample size of 170 markets across 103 event clusters.
Estimate: 0.031. 95% confidence interval: -0.127 to 0.189. Observed range: -1.000 to 1.564.
Raw p-value: 0.701; multiple-testing adjusted q-value: 0.789.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.60-0.65:yes` used a sample size of 170 markets across 103 event clusters.
Estimate: -0.230. 95% confidence interval: -0.353 to -0.108. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.65-0.70:no` used a sample size of 185 markets across 110 event clusters.
Estimate: 0.021. 95% confidence interval: -0.158 to 0.199. Observed range: -1.000 to 1.857.
Raw p-value: 0.819; multiple-testing adjusted q-value: 0.859.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.65-0.70:yes` used a sample size of 185 markets across 110 event clusters.
Estimate: -0.217. 95% confidence interval: -0.328 to -0.105. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.70-0.75:no` used a sample size of 176 markets across 117 event clusters.
Estimate: -0.001. 95% confidence interval: -0.189 to 0.186. Observed range: -1.000 to 2.333.
Raw p-value: 0.988; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.70-0.75:yes` used a sample size of 176 markets across 117 event clusters.
Estimate: -0.188. 95% confidence interval: -0.288 to -0.087. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.75-0.80:no` used a sample size of 196 markets across 119 event clusters.
Estimate: 0.247. 95% confidence interval: 0.013 to 0.480. Observed range: -1.000 to 3.000.
Raw p-value: 0.038; multiple-testing adjusted q-value: 0.057.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.75-0.80:yes` used a sample size of 198 markets across 121 event clusters.
Estimate: -0.298. 95% confidence interval: -0.399 to -0.197. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.80-0.85:no` used a sample size of 158 markets across 83 event clusters.
Estimate: 0.042. 95% confidence interval: -0.246 to 0.329. Observed range: -1.000 to 4.000.
Raw p-value: 0.776; multiple-testing adjusted q-value: 0.834.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.80-0.85:yes` used a sample size of 159 markets across 84 event clusters.
Estimate: -0.263. 95% confidence interval: -0.382 to -0.145. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.85-0.90:no` used a sample size of 155 markets across 83 event clusters.
Estimate: 0.151. 95% confidence interval: -0.213 to 0.515. Observed range: -1.000 to 6.143.
Raw p-value: 0.416; multiple-testing adjusted q-value: 0.515.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.85-0.90:yes` used a sample size of 156 markets across 84 event clusters.
Estimate: -0.279. 95% confidence interval: -0.401 to -0.158. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.90-0.95:no` used a sample size of 162 markets across 91 event clusters.
Estimate: -0.074. 95% confidence interval: -0.424 to 0.276. Observed range: -1.000 to 10.111.
Raw p-value: 0.680; multiple-testing adjusted q-value: 0.776.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.90-0.95:yes` used a sample size of 174 markets across 91 event clusters.
Estimate: -0.251. 95% confidence interval: -0.359 to -0.142. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.95-1.00:no` used a sample size of 142 markets across 67 event clusters.
Estimate: -0.304. 95% confidence interval: -0.825 to 0.217. Observed range: -1.000 to 19.000.
Raw p-value: 0.253; multiple-testing adjusted q-value: 0.326.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.95-1.00:yes` used a sample size of 138 markets across 64 event clusters.
Estimate: -0.178. 95% confidence interval: -0.329 to -0.028. Observed range: -1.000 to 0.042.
Raw p-value: 0.020; multiple-testing adjusted q-value: 0.031.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.00-0.05:no` used a sample size of 13 markets across 9 event clusters.
Estimate: 0.011. 95% confidence interval: not available to not available. Observed range: 0.000 to 0.020.
Not tested: only 9 independent events (needs 30).

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.00-0.05:yes` used a sample size of 22 markets across 11 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 11 independent events (needs 30).

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.05-0.10:no` used a sample size of 59 markets across 39 event clusters.
Estimate: 0.015. 95% confidence interval: -0.021 to 0.050. Observed range: -1.000 to 0.075.
Raw p-value: 0.417; multiple-testing adjusted q-value: 0.515.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.05-0.10:yes` used a sample size of 66 markets across 44 event clusters.
Estimate: -0.848. 95% confidence interval: -1.149 to -0.548. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.10-0.15:no` used a sample size of 119 markets across 59 event clusters.
Estimate: 0.020. 95% confidence interval: -0.014 to 0.054. Observed range: -1.000 to 0.136.
Raw p-value: 0.253; multiple-testing adjusted q-value: 0.326.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.10-0.15:yes` used a sample size of 122 markets across 59 event clusters.
Estimate: -0.714. 95% confidence interval: -0.984 to -0.445. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.15-0.20:no` used a sample size of 183 markets across 93 event clusters.
Estimate: -0.009. 95% confidence interval: -0.066 to 0.048. Observed range: -1.000 to 0.190.
Raw p-value: 0.752; multiple-testing adjusted q-value: 0.818.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.15-0.20:yes` used a sample size of 183 markets across 93 event clusters.
Estimate: -0.426. 95% confidence interval: -0.683 to -0.170. Observed range: -1.000 to 5.250.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.20-0.25:no` used a sample size of 146 markets across 91 event clusters.
Estimate: 0.037. 95% confidence interval: -0.027 to 0.102. Observed range: -1.000 to 0.266.
Raw p-value: 0.258; multiple-testing adjusted q-value: 0.330.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.20-0.25:yes` used a sample size of 146 markets across 91 event clusters.
Estimate: -0.530. 95% confidence interval: -0.770 to -0.290. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.25-0.30:no` used a sample size of 145 markets across 103 event clusters.
Estimate: -0.027. 95% confidence interval: -0.119 to 0.065. Observed range: -1.000 to 0.351.
Raw p-value: 0.566; multiple-testing adjusted q-value: 0.664.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.25-0.30:yes` used a sample size of 145 markets across 103 event clusters.
Estimate: -0.318. 95% confidence interval: -0.576 to -0.059. Observed range: -1.000 to 2.704.
Raw p-value: 0.016; multiple-testing adjusted q-value: 0.025.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.30-0.35:no` used a sample size of 144 markets across 98 event clusters.
Estimate: -0.024. 95% confidence interval: -0.113 to 0.065. Observed range: -1.000 to 0.449.
Raw p-value: 0.600; multiple-testing adjusted q-value: 0.696.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.30-0.35:yes` used a sample size of 144 markets across 98 event clusters.
Estimate: -0.247. 95% confidence interval: -0.448 to -0.046. Observed range: -1.000 to 2.125.
Raw p-value: 0.016; multiple-testing adjusted q-value: 0.025.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.35-0.40:no` used a sample size of 137 markets across 98 event clusters.
Estimate: 0.053. 95% confidence interval: -0.042 to 0.148. Observed range: -1.000 to 0.562.
Raw p-value: 0.275; multiple-testing adjusted q-value: 0.349.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.35-0.40:yes` used a sample size of 137 markets across 98 event clusters.
Estimate: -0.442. 95% confidence interval: -0.620 to -0.263. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.40-0.45:no` used a sample size of 142 markets across 96 event clusters.
Estimate: 0.058. 95% confidence interval: -0.055 to 0.171. Observed range: -1.000 to 0.695.
Raw p-value: 0.314; multiple-testing adjusted q-value: 0.396.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.40-0.45:yes` used a sample size of 142 markets across 96 event clusters.
Estimate: -0.391. 95% confidence interval: -0.566 to -0.215. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.45-0.50:no` used a sample size of 159 markets across 112 event clusters.
Estimate: 0.022. 95% confidence interval: -0.108 to 0.152. Observed range: -1.000 to 0.852.
Raw p-value: 0.742; multiple-testing adjusted q-value: 0.815.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.45-0.50:yes` used a sample size of 161 markets across 114 event clusters.
Estimate: -0.302. 95% confidence interval: -0.470 to -0.134. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.50-0.55:no` used a sample size of 110 markets across 76 event clusters.
Estimate: 0.062. 95% confidence interval: -0.107 to 0.230. Observed range: -1.000 to 1.041.
Raw p-value: 0.472; multiple-testing adjusted q-value: 0.571.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.50-0.55:yes` used a sample size of 111 markets across 77 event clusters.
Estimate: -0.295. 95% confidence interval: -0.470 to -0.121. Observed range: -1.000 to 0.923.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.55-0.60:no` used a sample size of 149 markets across 79 event clusters.
Estimate: 0.060. 95% confidence interval: -0.092 to 0.212. Observed range: -1.000 to 1.273.
Raw p-value: 0.441; multiple-testing adjusted q-value: 0.537.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.55-0.60:yes` used a sample size of 149 markets across 79 event clusters.
Estimate: -0.271. 95% confidence interval: -0.413 to -0.129. Observed range: -1.000 to 0.754.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.60-0.65:no` used a sample size of 170 markets across 103 event clusters.
Estimate: 0.031. 95% confidence interval: -0.127 to 0.189. Observed range: -1.000 to 1.564.
Raw p-value: 0.701; multiple-testing adjusted q-value: 0.789.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.60-0.65:yes` used a sample size of 170 markets across 103 event clusters.
Estimate: -0.230. 95% confidence interval: -0.353 to -0.108. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.65-0.70:no` used a sample size of 185 markets across 110 event clusters.
Estimate: 0.021. 95% confidence interval: -0.158 to 0.199. Observed range: -1.000 to 1.857.
Raw p-value: 0.819; multiple-testing adjusted q-value: 0.859.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.65-0.70:yes` used a sample size of 185 markets across 110 event clusters.
Estimate: -0.217. 95% confidence interval: -0.328 to -0.105. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.70-0.75:no` used a sample size of 176 markets across 117 event clusters.
Estimate: -0.001. 95% confidence interval: -0.189 to 0.186. Observed range: -1.000 to 2.333.
Raw p-value: 0.988; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.70-0.75:yes` used a sample size of 176 markets across 117 event clusters.
Estimate: -0.188. 95% confidence interval: -0.288 to -0.087. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.75-0.80:no` used a sample size of 196 markets across 119 event clusters.
Estimate: 0.247. 95% confidence interval: 0.013 to 0.480. Observed range: -1.000 to 3.000.
Raw p-value: 0.038; multiple-testing adjusted q-value: 0.057.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.75-0.80:yes` used a sample size of 198 markets across 121 event clusters.
Estimate: -0.298. 95% confidence interval: -0.399 to -0.197. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.80-0.85:no` used a sample size of 158 markets across 83 event clusters.
Estimate: 0.042. 95% confidence interval: -0.246 to 0.329. Observed range: -1.000 to 4.000.
Raw p-value: 0.776; multiple-testing adjusted q-value: 0.834.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.80-0.85:yes` used a sample size of 159 markets across 84 event clusters.
Estimate: -0.263. 95% confidence interval: -0.382 to -0.145. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.85-0.90:no` used a sample size of 155 markets across 83 event clusters.
Estimate: 0.151. 95% confidence interval: -0.213 to 0.515. Observed range: -1.000 to 6.143.
Raw p-value: 0.416; multiple-testing adjusted q-value: 0.515.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.85-0.90:yes` used a sample size of 156 markets across 84 event clusters.
Estimate: -0.279. 95% confidence interval: -0.401 to -0.158. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.90-0.95:no` used a sample size of 162 markets across 91 event clusters.
Estimate: -0.074. 95% confidence interval: -0.424 to 0.276. Observed range: -1.000 to 10.111.
Raw p-value: 0.680; multiple-testing adjusted q-value: 0.776.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.90-0.95:yes` used a sample size of 174 markets across 91 event clusters.
Estimate: -0.251. 95% confidence interval: -0.359 to -0.142. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.95-1.00:no` used a sample size of 142 markets across 67 event clusters.
Estimate: -0.304. 95% confidence interval: -0.825 to 0.217. Observed range: -1.000 to 19.000.
Raw p-value: 0.253; multiple-testing adjusted q-value: 0.326.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.95-1.00:yes` used a sample size of 138 markets across 64 event clusters.
Estimate: -0.178. 95% confidence interval: -0.329 to -0.028. Observed range: -1.000 to 0.042.
Raw p-value: 0.020; multiple-testing adjusted q-value: 0.031.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:1h:no` used a sample size of 8337 markets across 862 event clusters.
Estimate: -0.716. 95% confidence interval: -0.752 to -0.680. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:1h:yes` used a sample size of 8670 markets across 882 event clusters.
Estimate: -0.833. 95% confidence interval: -0.864 to -0.802. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:1h:no` used a sample size of 1165 markets across 101 event clusters.
Estimate: -0.534. 95% confidence interval: -0.648 to -0.420. Observed range: -1.000 to 19.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:1h:yes` used a sample size of 1260 markets across 103 event clusters.
Estimate: -0.755. 95% confidence interval: -0.840 to -0.669. Observed range: -1.000 to 10.111.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:1h:no` used a sample size of 7172 markets across 761 event clusters.
Estimate: -0.745. 95% confidence interval: -0.781 to -0.709. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:1h:yes` used a sample size of 7410 markets across 779 event clusters.
Estimate: -0.846. 95% confidence interval: -0.879 to -0.814. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:1h:1h:no` used a sample size of 8337 markets across 862 event clusters.
Estimate: -0.716. 95% confidence interval: -0.752 to -0.680. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:1h:1h:yes` used a sample size of 8670 markets across 882 event clusters.
Estimate: -0.833. 95% confidence interval: -0.864 to -0.802. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:1d:no` used a sample size of 14813 markets across 936 event clusters.
Estimate: -0.113. 95% confidence interval: -0.145 to -0.080. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:1d:yes` used a sample size of 14984 markets across 939 event clusters.
Estimate: -0.310. 95% confidence interval: -0.334 to -0.286. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:1d:no` used a sample size of 1777 markets across 101 event clusters.
Estimate: -0.063. 95% confidence interval: -0.144 to 0.017. Observed range: -1.000 to 15.667.
Raw p-value: 0.123; multiple-testing adjusted q-value: 0.170.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:1d:yes` used a sample size of 1846 markets across 103 event clusters.
Estimate: -0.394. 95% confidence interval: -0.452 to -0.336. Observed range: -1.000 to 10.111.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:1d:no` used a sample size of 13036 markets across 835 event clusters.
Estimate: -0.120. 95% confidence interval: -0.155 to -0.084. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:1d:yes` used a sample size of 13138 markets across 836 event clusters.
Estimate: -0.298. 95% confidence interval: -0.324 to -0.272. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:1d:1d:no` used a sample size of 14813 markets across 936 event clusters.
Estimate: -0.113. 95% confidence interval: -0.145 to -0.080. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:1d:1d:yes` used a sample size of 14984 markets across 939 event clusters.
Estimate: -0.310. 95% confidence interval: -0.334 to -0.286. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:7d:no` used a sample size of 2850 markets across 221 event clusters.
Estimate: 0.023. 95% confidence interval: -0.047 to 0.093. Observed range: -1.000 to 19.000.
Raw p-value: 0.513; multiple-testing adjusted q-value: 0.613.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:7d:yes` used a sample size of 2884 markets across 221 event clusters.
Estimate: -0.335. 95% confidence interval: -0.388 to -0.281. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:7d:no` used a sample size of 645 markets across 30 event clusters.
Estimate: 0.068. 95% confidence interval: -0.075 to 0.210. Observed range: -1.000 to 10.111.
Raw p-value: 0.353; multiple-testing adjusted q-value: 0.444.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:7d:yes` used a sample size of 647 markets across 30 event clusters.
Estimate: -0.355. 95% confidence interval: -0.456 to -0.255. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:7d:no` used a sample size of 2205 markets across 191 event clusters.
Estimate: 0.010. 95% confidence interval: -0.070 to 0.091. Observed range: -1.000 to 19.000.
Raw p-value: 0.800; multiple-testing adjusted q-value: 0.853.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:7d:yes` used a sample size of 2237 markets across 191 event clusters.
Estimate: -0.329. 95% confidence interval: -0.391 to -0.266. Observed range: -1.000 to 7.333.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:7d:7d:no` used a sample size of 2850 markets across 221 event clusters.
Estimate: 0.023. 95% confidence interval: -0.047 to 0.093. Observed range: -1.000 to 19.000.
Raw p-value: 0.513; multiple-testing adjusted q-value: 0.613.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:7d:7d:yes` used a sample size of 2884 markets across 221 event clusters.
Estimate: -0.335. 95% confidence interval: -0.388 to -0.281. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Listing drift — candidate (discovery only)

Hypothesis `listing_drift:brier_1h_vs_24h` used a sample size of 14618 markets across 931 event clusters.
Estimate: 0.129. 95% confidence interval: 0.118 to 0.141. Observed range: -0.970 to 1.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.
