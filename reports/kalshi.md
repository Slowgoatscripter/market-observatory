# Kalshi market observatory

This public-data observer never trades or places orders. These estimates are descriptive research and **not a trading signal**.

## How to read this

Discovery uses markets settled before 2026-04-01; the fixed confirmation window begins at that UTC boundary. Uncertainty is a 95% confidence interval clustered by event. Benjamini-Hochberg adjustment uses the latest discovery run per hypothesis and treats confirmation runs as a separate family.

Fees and returns assume a taker buys at the ask (never the midpoint) and pays the quadratic fee rounded up per order: `ceil-to-cent(0.07 × series fee multiplier × contracts × P × (1-P))`. We retain the series fee type; a missing type is assumed quadratic, any other fee type is excluded, and maker discounts are not assumed.

## Findings

Confirmation waits until the archive is complete.

### Mentions longshot YES — candidate (discovery only)

Tests whether YES contracts in Mentions markets priced from $0.10 through $0.30 one day before close have a negative mean return when bought at the ask after fees.
Result: negative as preregistered; mean return -0.447. Sample: 924 independent events (3254 contracts). Status: candidate (discovery only).
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.00-0.05` used a sample size of 9671 markets across 1632 event clusters.
Estimate: -0.013. 95% confidence interval: -0.014 to -0.012. Observed range: -0.040 to 0.990.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.05-0.10` used a sample size of 1245 markets across 551 event clusters.
Estimate: -0.058. 95% confidence interval: -0.064 to -0.052. Observed range: -0.090 to 0.950.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.10-0.15` used a sample size of 499 markets across 321 event clusters.
Estimate: -0.076. 95% confidence interval: -0.093 to -0.059. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.15-0.20` used a sample size of 313 markets across 211 event clusters.
Estimate: -0.103. 95% confidence interval: -0.131 to -0.074. Observed range: -0.190 to 0.850.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.20-0.25` used a sample size of 263 markets across 186 event clusters.
Estimate: -0.083. 95% confidence interval: -0.129 to -0.038. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.25-0.30` used a sample size of 204 markets across 163 event clusters.
Estimate: -0.122. 95% confidence interval: -0.172 to -0.072. Observed range: -0.290 to 0.750.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.30-0.35` used a sample size of 190 markets across 141 event clusters.
Estimate: -0.129. 95% confidence interval: -0.185 to -0.073. Observed range: -0.340 to 0.700.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.35-0.40` used a sample size of 164 markets across 125 event clusters.
Estimate: -0.099. 95% confidence interval: -0.175 to -0.023. Observed range: -0.390 to 0.650.
Raw p-value: 0.011; multiple-testing adjusted q-value: 0.018.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.40-0.45` used a sample size of 168 markets across 129 event clusters.
Estimate: -0.109. 95% confidence interval: -0.185 to -0.033. Observed range: -0.440 to 0.600.
Raw p-value: 0.005; multiple-testing adjusted q-value: 0.009.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.45-0.50` used a sample size of 176 markets across 135 event clusters.
Estimate: -0.225. 95% confidence interval: -0.292 to -0.158. Observed range: -0.490 to 0.550.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.50-0.55` used a sample size of 161 markets across 108 event clusters.
Estimate: -0.167. 95% confidence interval: -0.255 to -0.079. Observed range: -0.540 to 0.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.55-0.60` used a sample size of 142 markets across 112 event clusters.
Estimate: -0.141. 95% confidence interval: -0.230 to -0.051. Observed range: -0.590 to 0.450.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.004.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.60-0.65` used a sample size of 147 markets across 107 event clusters.
Estimate: -0.234. 95% confidence interval: -0.341 to -0.126. Observed range: -0.640 to 0.400.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.65-0.70` used a sample size of 132 markets across 100 event clusters.
Estimate: -0.244. 95% confidence interval: -0.338 to -0.151. Observed range: -0.690 to 0.350.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.70-0.75` used a sample size of 121 markets across 91 event clusters.
Estimate: -0.229. 95% confidence interval: -0.343 to -0.115. Observed range: -0.740 to 0.300.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.75-0.80` used a sample size of 202 markets across 131 event clusters.
Estimate: -0.409. 95% confidence interval: -0.492 to -0.327. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.80-0.85` used a sample size of 154 markets across 114 event clusters.
Estimate: -0.256. 95% confidence interval: -0.353 to -0.159. Observed range: -0.840 to 0.200.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.85-0.90` used a sample size of 212 markets across 138 event clusters.
Estimate: -0.163. 95% confidence interval: -0.268 to -0.059. Observed range: -0.890 to 0.150.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.004.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.90-0.95` used a sample size of 336 markets across 213 event clusters.
Estimate: -0.215. 95% confidence interval: -0.301 to -0.129. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1h:0.95-1.00` used a sample size of 10744 markets across 1857 event clusters.
Estimate: -0.074. 95% confidence interval: -0.095 to -0.052. Observed range: -1.000 to 0.050.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.00-0.05` used a sample size of 7389 markets across 1006 event clusters.
Estimate: -0.012. 95% confidence interval: -0.012 to -0.011. Observed range: -0.040 to 0.990.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.05-0.10` used a sample size of 625 markets across 301 event clusters.
Estimate: -0.061. 95% confidence interval: -0.069 to -0.052. Observed range: -0.090 to 0.950.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.10-0.15` used a sample size of 331 markets across 194 event clusters.
Estimate: -0.073. 95% confidence interval: -0.095 to -0.052. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.15-0.20` used a sample size of 235 markets across 151 event clusters.
Estimate: -0.093. 95% confidence interval: -0.129 to -0.058. Observed range: -0.190 to 0.850.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.20-0.25` used a sample size of 184 markets across 126 event clusters.
Estimate: -0.092. 95% confidence interval: -0.144 to -0.041. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.25-0.30` used a sample size of 144 markets across 113 event clusters.
Estimate: -0.131. 95% confidence interval: -0.186 to -0.075. Observed range: -0.290 to 0.740.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.30-0.35` used a sample size of 142 markets across 101 event clusters.
Estimate: -0.121. 95% confidence interval: -0.187 to -0.055. Observed range: -0.340 to 0.700.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.35-0.40` used a sample size of 107 markets across 77 event clusters.
Estimate: -0.133. 95% confidence interval: -0.223 to -0.042. Observed range: -0.390 to 0.650.
Raw p-value: 0.004; multiple-testing adjusted q-value: 0.007.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.40-0.45` used a sample size of 110 markets across 83 event clusters.
Estimate: -0.107. 95% confidence interval: -0.198 to -0.015. Observed range: -0.440 to 0.600.
Raw p-value: 0.022; multiple-testing adjusted q-value: 0.037.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.45-0.50` used a sample size of 108 markets across 78 event clusters.
Estimate: -0.249. 95% confidence interval: -0.330 to -0.167. Observed range: -0.490 to 0.550.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.50-0.55` used a sample size of 104 markets across 74 event clusters.
Estimate: -0.133. 95% confidence interval: -0.225 to -0.041. Observed range: -0.540 to 0.500.
Raw p-value: 0.005; multiple-testing adjusted q-value: 0.008.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.55-0.60` used a sample size of 87 markets across 68 event clusters.
Estimate: -0.169. 95% confidence interval: -0.283 to -0.055. Observed range: -0.590 to 0.450.
Raw p-value: 0.004; multiple-testing adjusted q-value: 0.007.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.60-0.65` used a sample size of 91 markets across 66 event clusters.
Estimate: -0.204. 95% confidence interval: -0.309 to -0.098. Observed range: -0.640 to 0.400.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.65-0.70` used a sample size of 75 markets across 56 event clusters.
Estimate: -0.149. 95% confidence interval: -0.263 to -0.036. Observed range: -0.690 to 0.350.
Raw p-value: 0.010; multiple-testing adjusted q-value: 0.017.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.70-0.75` used a sample size of 62 markets across 53 event clusters.
Estimate: -0.123. 95% confidence interval: -0.241 to -0.005. Observed range: -0.740 to 0.300.
Raw p-value: 0.041; multiple-testing adjusted q-value: 0.064.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.75-0.80` used a sample size of 82 markets across 59 event clusters.
Estimate: -0.161. 95% confidence interval: -0.291 to -0.030. Observed range: -0.790 to 0.250.
Raw p-value: 0.016; multiple-testing adjusted q-value: 0.027.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.80-0.85` used a sample size of 76 markets across 60 event clusters.
Estimate: -0.097. 95% confidence interval: -0.200 to 0.005. Observed range: -0.840 to 0.200.
Raw p-value: 0.063; multiple-testing adjusted q-value: 0.098.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.85-0.90` used a sample size of 138 markets across 92 event clusters.
Estimate: -0.114. 95% confidence interval: -0.208 to -0.020. Observed range: -0.890 to 0.150.
Raw p-value: 0.018; multiple-testing adjusted q-value: 0.029.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.90-0.95` used a sample size of 192 markets across 125 event clusters.
Estimate: -0.113. 95% confidence interval: -0.194 to -0.033. Observed range: -0.940 to 0.100.
Raw p-value: 0.006; multiple-testing adjusted q-value: 0.010.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1h:0.95-1.00` used a sample size of 8056 markets across 1052 event clusters.
Estimate: -0.001. 95% confidence interval: -0.004 to 0.003. Observed range: -1.000 to 0.050.
Raw p-value: 0.634; multiple-testing adjusted q-value: 0.800.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.00-0.05` used a sample size of 1825 markets across 587 event clusters.
Estimate: -0.013. 95% confidence interval: -0.016 to -0.010. Observed range: -0.040 to 0.990.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.05-0.10` used a sample size of 1199 markets across 545 event clusters.
Estimate: -0.034. 95% confidence interval: -0.045 to -0.023. Observed range: -0.090 to 0.950.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.10-0.15` used a sample size of 836 markets across 527 event clusters.
Estimate: -0.041. 95% confidence interval: -0.061 to -0.022. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.15-0.20` used a sample size of 922 markets across 587 event clusters.
Estimate: -0.068. 95% confidence interval: -0.088 to -0.048. Observed range: -0.190 to 0.850.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.20-0.25` used a sample size of 1038 markets across 641 event clusters.
Estimate: -0.088. 95% confidence interval: -0.109 to -0.066. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.25-0.30` used a sample size of 956 markets across 613 event clusters.
Estimate: -0.066. 95% confidence interval: -0.092 to -0.040. Observed range: -0.290 to 0.750.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.30-0.35` used a sample size of 1009 markets across 653 event clusters.
Estimate: -0.097. 95% confidence interval: -0.122 to -0.071. Observed range: -0.340 to 0.700.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.35-0.40` used a sample size of 963 markets across 642 event clusters.
Estimate: -0.109. 95% confidence interval: -0.138 to -0.081. Observed range: -0.390 to 0.650.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.40-0.45` used a sample size of 895 markets across 615 event clusters.
Estimate: -0.084. 95% confidence interval: -0.117 to -0.050. Observed range: -0.440 to 0.600.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.45-0.50` used a sample size of 896 markets across 630 event clusters.
Estimate: -0.117. 95% confidence interval: -0.149 to -0.086. Observed range: -0.490 to 0.550.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.50-0.55` used a sample size of 940 markets across 611 event clusters.
Estimate: -0.127. 95% confidence interval: -0.160 to -0.093. Observed range: -0.540 to 0.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.55-0.60` used a sample size of 938 markets across 599 event clusters.
Estimate: -0.091. 95% confidence interval: -0.126 to -0.057. Observed range: -0.590 to 0.450.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.60-0.65` used a sample size of 1033 markets across 653 event clusters.
Estimate: -0.106. 95% confidence interval: -0.138 to -0.073. Observed range: -0.640 to 0.400.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.65-0.70` used a sample size of 1134 markets across 703 event clusters.
Estimate: -0.111. 95% confidence interval: -0.142 to -0.079. Observed range: -0.690 to 0.350.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.70-0.75` used a sample size of 1052 markets across 644 event clusters.
Estimate: -0.138. 95% confidence interval: -0.172 to -0.104. Observed range: -0.740 to 0.300.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.75-0.80` used a sample size of 1170 markets across 718 event clusters.
Estimate: -0.124. 95% confidence interval: -0.156 to -0.092. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.80-0.85` used a sample size of 1188 markets across 693 event clusters.
Estimate: -0.143. 95% confidence interval: -0.175 to -0.110. Observed range: -0.840 to 0.200.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.85-0.90` used a sample size of 1355 markets across 709 event clusters.
Estimate: -0.100. 95% confidence interval: -0.127 to -0.072. Observed range: -0.890 to 0.150.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.90-0.95` used a sample size of 1579 markets across 766 event clusters.
Estimate: -0.098. 95% confidence interval: -0.127 to -0.069. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:1d:0.95-1.00` used a sample size of 2832 markets across 969 event clusters.
Estimate: -0.169. 95% confidence interval: -0.205 to -0.133. Observed range: -1.000 to 0.050.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.00-0.05` used a sample size of 599 markets across 186 event clusters.
Estimate: -0.011. 95% confidence interval: -0.017 to -0.005. Observed range: -0.040 to 0.990.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.05-0.10` used a sample size of 455 markets across 213 event clusters.
Estimate: -0.028. 95% confidence interval: -0.045 to -0.011. Observed range: -0.090 to 0.950.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.10-0.15` used a sample size of 573 markets across 344 event clusters.
Estimate: -0.047. 95% confidence interval: -0.070 to -0.024. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.15-0.20` used a sample size of 786 markets across 473 event clusters.
Estimate: -0.075. 95% confidence interval: -0.096 to -0.053. Observed range: -0.190 to 0.850.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.20-0.25` used a sample size of 889 markets across 535 event clusters.
Estimate: -0.091. 95% confidence interval: -0.114 to -0.069. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.25-0.30` used a sample size of 852 markets across 521 event clusters.
Estimate: -0.070. 95% confidence interval: -0.097 to -0.042. Observed range: -0.290 to 0.750.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.30-0.35` used a sample size of 897 markets across 562 event clusters.
Estimate: -0.099. 95% confidence interval: -0.126 to -0.072. Observed range: -0.340 to 0.700.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.35-0.40` used a sample size of 874 markets across 566 event clusters.
Estimate: -0.115. 95% confidence interval: -0.145 to -0.085. Observed range: -0.390 to 0.650.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.40-0.45` used a sample size of 830 markets across 558 event clusters.
Estimate: -0.091. 95% confidence interval: -0.126 to -0.057. Observed range: -0.440 to 0.600.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.45-0.50` used a sample size of 820 markets across 566 event clusters.
Estimate: -0.119. 95% confidence interval: -0.152 to -0.086. Observed range: -0.490 to 0.550.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.50-0.55` used a sample size of 867 markets across 554 event clusters.
Estimate: -0.129. 95% confidence interval: -0.164 to -0.095. Observed range: -0.540 to 0.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.55-0.60` used a sample size of 877 markets across 551 event clusters.
Estimate: -0.081. 95% confidence interval: -0.116 to -0.046. Observed range: -0.590 to 0.450.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.60-0.65` used a sample size of 985 markets across 607 event clusters.
Estimate: -0.113. 95% confidence interval: -0.146 to -0.080. Observed range: -0.640 to 0.400.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.65-0.70` used a sample size of 1069 markets across 641 event clusters.
Estimate: -0.104. 95% confidence interval: -0.136 to -0.071. Observed range: -0.690 to 0.350.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.70-0.75` used a sample size of 978 markets across 588 event clusters.
Estimate: -0.125. 95% confidence interval: -0.160 to -0.090. Observed range: -0.740 to 0.300.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.75-0.80` used a sample size of 1010 markets across 623 event clusters.
Estimate: -0.095. 95% confidence interval: -0.127 to -0.064. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.80-0.85` used a sample size of 1079 markets across 618 event clusters.
Estimate: -0.120. 95% confidence interval: -0.152 to -0.087. Observed range: -0.840 to 0.200.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.85-0.90` used a sample size of 1284 markets across 643 event clusters.
Estimate: -0.098. 95% confidence interval: -0.126 to -0.069. Observed range: -0.890 to 0.150.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.90-0.95` used a sample size of 1436 markets across 660 event clusters.
Estimate: -0.091. 95% confidence interval: -0.122 to -0.060. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:1d:0.95-1.00` used a sample size of 1733 markets across 597 event clusters.
Estimate: -0.055. 95% confidence interval: -0.081 to -0.028. Observed range: -1.000 to 0.050.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.00-0.05` used a sample size of 605 markets across 191 event clusters.
Estimate: -0.018. 95% confidence interval: -0.023 to -0.013. Observed range: -0.040 to 0.970.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.05-0.10` used a sample size of 346 markets across 180 event clusters.
Estimate: -0.030. 95% confidence interval: -0.053 to -0.008. Observed range: -0.090 to 0.950.
Raw p-value: 0.008; multiple-testing adjusted q-value: 0.014.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.10-0.15` used a sample size of 250 markets across 139 event clusters.
Estimate: -0.054. 95% confidence interval: -0.084 to -0.023. Observed range: -0.140 to 0.900.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.15-0.20` used a sample size of 242 markets across 146 event clusters.
Estimate: -0.063. 95% confidence interval: -0.105 to -0.021. Observed range: -0.190 to 0.850.
Raw p-value: 0.003; multiple-testing adjusted q-value: 0.006.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.20-0.25` used a sample size of 226 markets across 141 event clusters.
Estimate: -0.100. 95% confidence interval: -0.145 to -0.055. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.25-0.30` used a sample size of 193 markets across 133 event clusters.
Estimate: -0.057. 95% confidence interval: -0.125 to 0.011. Observed range: -0.290 to 0.750.
Raw p-value: 0.100; multiple-testing adjusted q-value: 0.154.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.30-0.35` used a sample size of 169 markets across 122 event clusters.
Estimate: -0.058. 95% confidence interval: -0.123 to 0.006. Observed range: -0.340 to 0.700.
Raw p-value: 0.076; multiple-testing adjusted q-value: 0.117.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.35-0.40` used a sample size of 169 markets across 125 event clusters.
Estimate: -0.128. 95% confidence interval: -0.196 to -0.059. Observed range: -0.390 to 0.650.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.40-0.45` used a sample size of 172 markets across 126 event clusters.
Estimate: -0.117. 95% confidence interval: -0.189 to -0.046. Observed range: -0.440 to 0.600.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.45-0.50` used a sample size of 188 markets across 136 event clusters.
Estimate: -0.108. 95% confidence interval: -0.185 to -0.031. Observed range: -0.490 to 0.550.
Raw p-value: 0.006; multiple-testing adjusted q-value: 0.011.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.50-0.55` used a sample size of 157 markets across 107 event clusters.
Estimate: -0.110. 95% confidence interval: -0.208 to -0.013. Observed range: -0.540 to 0.500.
Raw p-value: 0.027; multiple-testing adjusted q-value: 0.043.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.55-0.60` used a sample size of 185 markets across 116 event clusters.
Estimate: -0.071. 95% confidence interval: -0.147 to 0.004. Observed range: -0.590 to 0.450.
Raw p-value: 0.064; multiple-testing adjusted q-value: 0.100.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.60-0.65` used a sample size of 212 markets across 126 event clusters.
Estimate: -0.120. 95% confidence interval: -0.190 to -0.051. Observed range: -0.640 to 0.400.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.65-0.70` used a sample size of 227 markets across 145 event clusters.
Estimate: -0.131. 95% confidence interval: -0.202 to -0.061. Observed range: -0.690 to 0.350.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.70-0.75` used a sample size of 211 markets across 145 event clusters.
Estimate: -0.132. 95% confidence interval: -0.202 to -0.062. Observed range: -0.740 to 0.300.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.75-0.80` used a sample size of 234 markets across 151 event clusters.
Estimate: -0.203. 95% confidence interval: -0.276 to -0.130. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.80-0.85` used a sample size of 200 markets across 116 event clusters.
Estimate: -0.139. 95% confidence interval: -0.226 to -0.052. Observed range: -0.840 to 0.200.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.85-0.90` used a sample size of 195 markets across 125 event clusters.
Estimate: -0.205. 95% confidence interval: -0.291 to -0.119. Observed range: -0.890 to 0.150.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.90-0.95` used a sample size of 250 markets across 138 event clusters.
Estimate: -0.173. 95% confidence interval: -0.251 to -0.095. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:7d:0.95-1.00` used a sample size of 405 markets across 186 event clusters.
Estimate: -0.111. 95% confidence interval: -0.180 to -0.043. Observed range: -1.000 to 0.050.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.003.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.00-0.05` used a sample size of 22 markets across 11 event clusters.
Estimate: -0.028. 95% confidence interval: not available to not available. Observed range: -0.040 to -0.010.
Not tested: only 11 independent events (needs 30).

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.05-0.10` used a sample size of 70 markets across 45 event clusters.
Estimate: -0.059. 95% confidence interval: -0.088 to -0.031. Observed range: -0.090 to 0.920.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.10-0.15` used a sample size of 128 markets across 62 event clusters.
Estimate: -0.089. 95% confidence interval: -0.118 to -0.059. Observed range: -0.140 to 0.900.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.15-0.20` used a sample size of 192 markets across 102 event clusters.
Estimate: -0.068. 95% confidence interval: -0.114 to -0.021. Observed range: -0.190 to 0.850.
Raw p-value: 0.004; multiple-testing adjusted q-value: 0.008.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.20-0.25` used a sample size of 170 markets across 97 event clusters.
Estimate: -0.107. 95% confidence interval: -0.160 to -0.055. Observed range: -0.240 to 0.800.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.25-0.30` used a sample size of 158 markets across 106 event clusters.
Estimate: -0.055. 95% confidence interval: -0.132 to 0.022. Observed range: -0.290 to 0.750.
Raw p-value: 0.164; multiple-testing adjusted q-value: 0.241.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.30-0.35` used a sample size of 147 markets across 102 event clusters.
Estimate: -0.074. 95% confidence interval: -0.142 to -0.006. Observed range: -0.340 to 0.700.
Raw p-value: 0.032; multiple-testing adjusted q-value: 0.051.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.35-0.40` used a sample size of 136 markets across 97 event clusters.
Estimate: -0.157. 95% confidence interval: -0.224 to -0.091. Observed range: -0.390 to 0.650.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.40-0.45` used a sample size of 150 markets across 104 event clusters.
Estimate: -0.133. 95% confidence interval: -0.208 to -0.057. Observed range: -0.440 to 0.600.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.45-0.50` used a sample size of 169 markets across 120 event clusters.
Estimate: -0.120. 95% confidence interval: -0.201 to -0.040. Observed range: -0.490 to 0.550.
Raw p-value: 0.003; multiple-testing adjusted q-value: 0.006.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.50-0.55` used a sample size of 122 markets across 84 event clusters.
Estimate: -0.158. 95% confidence interval: -0.249 to -0.066. Observed range: -0.540 to 0.500.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.55-0.60` used a sample size of 153 markets across 88 event clusters.
Estimate: -0.111. 95% confidence interval: -0.192 to -0.030. Observed range: -0.590 to 0.450.
Raw p-value: 0.007; multiple-testing adjusted q-value: 0.012.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.60-0.65` used a sample size of 183 markets across 104 event clusters.
Estimate: -0.112. 95% confidence interval: -0.185 to -0.039. Observed range: -0.640 to 0.400.
Raw p-value: 0.003; multiple-testing adjusted q-value: 0.005.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.65-0.70` used a sample size of 192 markets across 116 event clusters.
Estimate: -0.117. 95% confidence interval: -0.191 to -0.042. Observed range: -0.690 to 0.350.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.004.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.70-0.75` used a sample size of 181 markets across 121 event clusters.
Estimate: -0.134. 95% confidence interval: -0.209 to -0.060. Observed range: -0.740 to 0.300.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.75-0.80` used a sample size of 202 markets across 123 event clusters.
Estimate: -0.202. 95% confidence interval: -0.282 to -0.123. Observed range: -0.790 to 0.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.80-0.85` used a sample size of 162 markets across 86 event clusters.
Estimate: -0.159. 95% confidence interval: -0.261 to -0.056. Observed range: -0.840 to 0.200.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.004.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.85-0.90` used a sample size of 151 markets across 87 event clusters.
Estimate: -0.229. 95% confidence interval: -0.332 to -0.126. Observed range: -0.890 to 0.150.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.90-0.95` used a sample size of 180 markets across 94 event clusters.
Estimate: -0.193. 95% confidence interval: -0.289 to -0.098. Observed range: -0.940 to 0.100.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Calibration — candidate (discovery only)

Hypothesis `calibration:mentions:7d:0.95-1.00` used a sample size of 159 markets across 71 event clusters.
Estimate: -0.137. 95% confidence interval: -0.278 to 0.003. Observed range: -1.000 to 0.050.
Raw p-value: 0.056; multiple-testing adjusted q-value: 0.087.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.00-0.05:no` used a sample size of 567 markets across 231 event clusters.
Estimate: 0.003. 95% confidence interval: 0.002 to 0.004. Observed range: 0.000 to 0.020.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.00-0.05:yes` used a sample size of 8955 markets across 1499 event clusters.
Estimate: -0.989. 95% confidence interval: -1.004 to -0.973. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.05-0.10:no` used a sample size of 430 markets across 250 event clusters.
Estimate: -0.004. 95% confidence interval: -0.020 to 0.012. Observed range: -1.000 to 0.075.
Raw p-value: 0.620; multiple-testing adjusted q-value: 0.788.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.05-0.10:yes` used a sample size of 1275 markets across 536 event clusters.
Estimate: -0.898. 95% confidence interval: -0.968 to -0.827. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.10-0.15:no` used a sample size of 297 markets across 183 event clusters.
Estimate: 0.016. 95% confidence interval: -0.009 to 0.041. Observed range: -1.000 to 0.136.
Raw p-value: 0.203; multiple-testing adjusted q-value: 0.292.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.10-0.15:yes` used a sample size of 504 markets across 307 event clusters.
Estimate: -0.820. 95% confidence interval: -0.922 to -0.718. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.15-0.20:no` used a sample size of 215 markets across 145 event clusters.
Estimate: -0.006. 95% confidence interval: -0.051 to 0.039. Observed range: -1.000 to 0.190.
Raw p-value: 0.795; multiple-testing adjusted q-value: 0.978.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.15-0.20:yes` used a sample size of 327 markets across 216 event clusters.
Estimate: -0.664. 95% confidence interval: -0.819 to -0.509. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.20-0.25:no` used a sample size of 174 markets across 121 event clusters.
Estimate: -0.029. 95% confidence interval: -0.098 to 0.039. Observed range: -1.000 to 0.250.
Raw p-value: 0.402; multiple-testing adjusted q-value: 0.542.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.20-0.25:yes` used a sample size of 260 markets across 184 event clusters.
Estimate: -0.565. 95% confidence interval: -0.741 to -0.388. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.25-0.30:no` used a sample size of 183 markets across 136 event clusters.
Estimate: -0.024. 95% confidence interval: -0.092 to 0.044. Observed range: -1.000 to 0.351.
Raw p-value: 0.486; multiple-testing adjusted q-value: 0.643.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.25-0.30:yes` used a sample size of 245 markets across 185 event clusters.
Estimate: -0.555. 95% confidence interval: -0.709 to -0.401. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.30-0.35:no` used a sample size of 147 markets across 108 event clusters.
Estimate: -0.001. 95% confidence interval: -0.092 to 0.089. Observed range: -1.000 to 0.449.
Raw p-value: 0.975; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.30-0.35:yes` used a sample size of 203 markets across 144 event clusters.
Estimate: -0.597. 95% confidence interval: -0.749 to -0.445. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.35-0.40:no` used a sample size of 128 markets across 102 event clusters.
Estimate: -0.076. 95% confidence interval: -0.192 to 0.041. Observed range: -1.000 to 0.562.
Raw p-value: 0.203; multiple-testing adjusted q-value: 0.292.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.35-0.40:yes` used a sample size of 172 markets across 134 event clusters.
Estimate: -0.416. 95% confidence interval: -0.590 to -0.243. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.40-0.45:no` used a sample size of 123 markets across 100 event clusters.
Estimate: -0.084. 95% confidence interval: -0.206 to 0.038. Observed range: -1.000 to 0.695.
Raw p-value: 0.178; multiple-testing adjusted q-value: 0.259.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.40-0.45:yes` used a sample size of 160 markets across 127 event clusters.
Estimate: -0.431. 95% confidence interval: -0.596 to -0.265. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.45-0.50:no` used a sample size of 137 markets across 109 event clusters.
Estimate: 0.011. 95% confidence interval: -0.115 to 0.138. Observed range: -1.000 to 0.818.
Raw p-value: 0.860; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.45-0.50:yes` used a sample size of 188 markets across 148 event clusters.
Estimate: -0.568. 95% confidence interval: -0.699 to -0.438. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.50-0.55:no` used a sample size of 98 markets across 72 event clusters.
Estimate: -0.009. 95% confidence interval: -0.163 to 0.144. Observed range: -1.000 to 1.041.
Raw p-value: 0.904; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.50-0.55:yes` used a sample size of 152 markets across 100 event clusters.
Estimate: -0.589. 95% confidence interval: -0.733 to -0.445. Observed range: -1.000 to 0.923.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.55-0.60:no` used a sample size of 115 markets across 92 event clusters.
Estimate: -0.146. 95% confidence interval: -0.327 to 0.035. Observed range: -1.000 to 1.273.
Raw p-value: 0.113; multiple-testing adjusted q-value: 0.172.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.55-0.60:yes` used a sample size of 138 markets across 108 event clusters.
Estimate: -0.287. 95% confidence interval: -0.437 to -0.138. Observed range: -1.000 to 0.754.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.60-0.65:no` used a sample size of 102 markets across 81 event clusters.
Estimate: 0.101. 95% confidence interval: -0.085 to 0.286. Observed range: -1.000 to 1.564.
Raw p-value: 0.286; multiple-testing adjusted q-value: 0.406.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.60-0.65:yes` used a sample size of 129 markets across 95 event clusters.
Estimate: -0.490. 95% confidence interval: -0.651 to -0.330. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.65-0.70:no` used a sample size of 110 markets across 86 event clusters.
Estimate: 0.059. 95% confidence interval: -0.147 to 0.265. Observed range: -1.000 to 1.778.
Raw p-value: 0.575; multiple-testing adjusted q-value: 0.745.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.65-0.70:yes` used a sample size of 139 markets across 104 event clusters.
Estimate: -0.509. 95% confidence interval: -0.638 to -0.381. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.70-0.75:no` used a sample size of 105 markets across 85 event clusters.
Estimate: -0.069. 95% confidence interval: -0.339 to 0.201. Observed range: -1.000 to 2.448.
Raw p-value: 0.617; multiple-testing adjusted q-value: 0.786.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.70-0.75:yes` used a sample size of 137 markets across 98 event clusters.
Estimate: -0.360. 95% confidence interval: -0.503 to -0.217. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.75-0.80:no` used a sample size of 109 markets across 86 event clusters.
Estimate: -0.199. 95% confidence interval: -0.488 to 0.090. Observed range: -1.000 to 3.167.
Raw p-value: 0.176; multiple-testing adjusted q-value: 0.258.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.75-0.80:yes` used a sample size of 215 markets across 135 event clusters.
Estimate: -0.599. 95% confidence interval: -0.698 to -0.500. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.80-0.85:no` used a sample size of 110 markets across 86 event clusters.
Estimate: -0.282. 95% confidence interval: -0.539 to -0.025. Observed range: -1.000 to 3.762.
Raw p-value: 0.031; multiple-testing adjusted q-value: 0.050.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.80-0.85:yes` used a sample size of 153 markets across 108 event clusters.
Estimate: -0.413. 95% confidence interval: -0.537 to -0.290. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.85-0.90:no` used a sample size of 167 markets across 106 event clusters.
Estimate: -0.256. 95% confidence interval: -0.487 to -0.025. Observed range: -1.000 to 6.143.
Raw p-value: 0.030; multiple-testing adjusted q-value: 0.048.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.85-0.90:yes` used a sample size of 208 markets across 122 event clusters.
Estimate: -0.298. 95% confidence interval: -0.395 to -0.202. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.90-0.95:no` used a sample size of 223 markets across 134 event clusters.
Estimate: -0.302. 95% confidence interval: -0.578 to -0.026. Observed range: -1.000 to 11.500.
Raw p-value: 0.032; multiple-testing adjusted q-value: 0.051.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.90-0.95:yes` used a sample size of 288 markets across 162 event clusters.
Estimate: -0.380. 95% confidence interval: -0.493 to -0.268. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.95-1.00:no` used a sample size of 9609 markets across 1660 event clusters.
Estimate: -0.974. 95% confidence interval: -0.989 to -0.959. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1h:0.95-1.00:yes` used a sample size of 1408 markets across 543 event clusters.
Estimate: -0.515. 95% confidence interval: -0.624 to -0.405. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.00-0.05:no` used a sample size of 355 markets across 165 event clusters.
Estimate: 0.003. 95% confidence interval: 0.002 to 0.004. Observed range: 0.000 to 0.020.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.00-0.05:yes` used a sample size of 6763 markets across 921 event clusters.
Estimate: -0.985. 95% confidence interval: -1.006 to -0.965. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.05-0.10:no` used a sample size of 310 markets across 168 event clusters.
Estimate: 0.004. 95% confidence interval: -0.011 to 0.019. Observed range: -1.000 to 0.075.
Raw p-value: 0.615; multiple-testing adjusted q-value: 0.785.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.05-0.10:yes` used a sample size of 657 markets across 289 event clusters.
Estimate: -0.895. 95% confidence interval: -0.989 to -0.801. Observed range: -1.000 to 13.286.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.10-0.15:no` used a sample size of 233 markets across 127 event clusters.
Estimate: 0.021. 95% confidence interval: -0.006 to 0.048. Observed range: -1.000 to 0.136.
Raw p-value: 0.132; multiple-testing adjusted q-value: 0.198.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.10-0.15:yes` used a sample size of 323 markets across 171 event clusters.
Estimate: -0.811. 95% confidence interval: -0.943 to -0.679. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.15-0.20:no` used a sample size of 181 markets across 115 event clusters.
Estimate: 0.005. 95% confidence interval: -0.042 to 0.053. Observed range: -1.000 to 0.190.
Raw p-value: 0.828; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.15-0.20:yes` used a sample size of 252 markets across 159 event clusters.
Estimate: -0.673. 95% confidence interval: -0.850 to -0.495. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.20-0.25:no` used a sample size of 143 markets across 92 event clusters.
Estimate: -0.025. 95% confidence interval: -0.103 to 0.052. Observed range: -1.000 to 0.250.
Raw p-value: 0.521; multiple-testing adjusted q-value: 0.686.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.20-0.25:yes` used a sample size of 188 markets across 131 event clusters.
Estimate: -0.508. 95% confidence interval: -0.725 to -0.291. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.25-0.30:no` used a sample size of 150 markets across 105 event clusters.
Estimate: -0.004. 95% confidence interval: -0.074 to 0.066. Observed range: -1.000 to 0.351.
Raw p-value: 0.913; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.25-0.30:yes` used a sample size of 183 markets across 132 event clusters.
Estimate: -0.592. 95% confidence interval: -0.755 to -0.430. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.30-0.35:no` used a sample size of 120 markets across 82 event clusters.
Estimate: 0.004. 95% confidence interval: -0.098 to 0.106. Observed range: -1.000 to 0.449.
Raw p-value: 0.936; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.30-0.35:yes` used a sample size of 159 markets across 106 event clusters.
Estimate: -0.575. 95% confidence interval: -0.753 to -0.397. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.35-0.40:no` used a sample size of 92 markets across 68 event clusters.
Estimate: -0.002. 95% confidence interval: -0.132 to 0.128. Observed range: -1.000 to 0.562.
Raw p-value: 0.975; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.35-0.40:yes` used a sample size of 116 markets across 85 event clusters.
Estimate: -0.512. 95% confidence interval: -0.714 to -0.310. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.40-0.45:no` used a sample size of 95 markets across 73 event clusters.
Estimate: -0.001. 95% confidence interval: -0.130 to 0.128. Observed range: -1.000 to 0.695.
Raw p-value: 0.990; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.40-0.45:yes` used a sample size of 108 markets across 83 event clusters.
Estimate: -0.476. 95% confidence interval: -0.665 to -0.287. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.45-0.50:no` used a sample size of 102 markets across 77 event clusters.
Estimate: 0.067. 95% confidence interval: -0.080 to 0.214. Observed range: -1.000 to 0.818.
Raw p-value: 0.374; multiple-testing adjusted q-value: 0.510.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.45-0.50:yes` used a sample size of 126 markets across 93 event clusters.
Estimate: -0.585. 95% confidence interval: -0.744 to -0.426. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.50-0.55:no` used a sample size of 81 markets across 56 event clusters.
Estimate: -0.031. 95% confidence interval: -0.203 to 0.141. Observed range: -1.000 to 1.041.
Raw p-value: 0.723; multiple-testing adjusted q-value: 0.903.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.50-0.55:yes` used a sample size of 97 markets across 67 event clusters.
Estimate: -0.431. 95% confidence interval: -0.607 to -0.256. Observed range: -1.000 to 0.923.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.55-0.60:no` used a sample size of 84 markets across 63 event clusters.
Estimate: -0.062. 95% confidence interval: -0.278 to 0.153. Observed range: -1.000 to 1.273.
Raw p-value: 0.571; multiple-testing adjusted q-value: 0.743.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.55-0.60:yes` used a sample size of 93 markets across 71 event clusters.
Estimate: -0.289. 95% confidence interval: -0.471 to -0.107. Observed range: -1.000 to 0.754.
Raw p-value: 0.002; multiple-testing adjusted q-value: 0.003.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.60-0.65:no` used a sample size of 71 markets across 52 event clusters.
Estimate: 0.168. 95% confidence interval: -0.044 to 0.380. Observed range: -1.000 to 1.564.
Raw p-value: 0.120; multiple-testing adjusted q-value: 0.182.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.60-0.65:yes` used a sample size of 77 markets across 57 event clusters.
Estimate: -0.472. 95% confidence interval: -0.637 to -0.306. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.65-0.70:no` used a sample size of 78 markets across 57 event clusters.
Estimate: 0.089. 95% confidence interval: -0.158 to 0.336. Observed range: -1.000 to 1.778.
Raw p-value: 0.482; multiple-testing adjusted q-value: 0.640.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.65-0.70:yes` used a sample size of 80 markets across 59 event clusters.
Estimate: -0.419. 95% confidence interval: -0.591 to -0.248. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.70-0.75:no` used a sample size of 76 markets across 57 event clusters.
Estimate: 0.013. 95% confidence interval: -0.311 to 0.337. Observed range: -1.000 to 2.448.
Raw p-value: 0.936; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.70-0.75:yes` used a sample size of 80 markets across 60 event clusters.
Estimate: -0.274. 95% confidence interval: -0.440 to -0.108. Observed range: -1.000 to 0.389.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.75-0.80:no` used a sample size of 71 markets across 52 event clusters.
Estimate: -0.052. 95% confidence interval: -0.469 to 0.365. Observed range: -1.000 to 3.167.
Raw p-value: 0.807; multiple-testing adjusted q-value: 0.991.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.75-0.80:yes` used a sample size of 85 markets across 60 event clusters.
Estimate: -0.357. 95% confidence interval: -0.531 to -0.183. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.80-0.85:no` used a sample size of 73 markets across 52 event clusters.
Estimate: -0.348. 95% confidence interval: -0.652 to -0.045. Observed range: -1.000 to 3.762.
Raw p-value: 0.024; multiple-testing adjusted q-value: 0.040.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.80-0.85:yes` used a sample size of 80 markets across 58 event clusters.
Estimate: -0.252. 95% confidence interval: -0.407 to -0.097. Observed range: -1.000 to 0.220.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.003.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.85-0.90:no` used a sample size of 120 markets across 70 event clusters.
Estimate: -0.162. 95% confidence interval: -0.456 to 0.131. Observed range: -1.000 to 6.143.
Raw p-value: 0.278; multiple-testing adjusted q-value: 0.396.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.85-0.90:yes` used a sample size of 128 markets across 78 event clusters.
Estimate: -0.258. 95% confidence interval: -0.364 to -0.152. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.90-0.95:no` used a sample size of 129 markets across 74 event clusters.
Estimate: -0.242. 95% confidence interval: -0.634 to 0.150. Observed range: -1.000 to 10.111.
Raw p-value: 0.227; multiple-testing adjusted q-value: 0.325.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.90-0.95:yes` used a sample size of 142 markets across 83 event clusters.
Estimate: -0.251. 95% confidence interval: -0.377 to -0.125. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.95-1.00:no` used a sample size of 7690 markets across 1007 event clusters.
Estimate: -0.984. 95% confidence interval: -0.998 to -0.969. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1h:0.95-1.00:yes` used a sample size of 299 markets across 165 event clusters.
Estimate: -0.159. 95% confidence interval: -0.226 to -0.093. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.00-0.05:no` used a sample size of 301 markets across 188 event clusters.
Estimate: -0.006. 95% confidence interval: -0.019 to 0.007. Observed range: -1.000 to 0.020.
Raw p-value: 0.332; multiple-testing adjusted q-value: 0.465.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.00-0.05:yes` used a sample size of 1747 markets across 550 event clusters.
Estimate: -0.948. 95% confidence interval: -0.999 to -0.898. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.05-0.10:no` used a sample size of 577 markets across 338 event clusters.
Estimate: -0.020. 95% confidence interval: -0.039 to -0.001. Observed range: -1.000 to 0.075.
Raw p-value: 0.042; multiple-testing adjusted q-value: 0.066.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.05-0.10:yes` used a sample size of 1167 markets across 519 event clusters.
Estimate: -0.622. 95% confidence interval: -0.755 to -0.489. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.10-0.15:no` used a sample size of 694 markets across 450 event clusters.
Estimate: -0.011. 95% confidence interval: -0.032 to 0.011. Observed range: -1.000 to 0.136.
Raw p-value: 0.320; multiple-testing adjusted q-value: 0.451.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.10-0.15:yes` used a sample size of 803 markets across 506 event clusters.
Estimate: -0.491. 95% confidence interval: -0.628 to -0.353. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.15-0.20:no` used a sample size of 902 markets across 563 event clusters.
Estimate: 0.003. 95% confidence interval: -0.020 to 0.027. Observed range: -1.000 to 0.190.
Raw p-value: 0.782; multiple-testing adjusted q-value: 0.965.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.15-0.20:yes` used a sample size of 927 markets across 577 event clusters.
Estimate: -0.421. 95% confidence interval: -0.533 to -0.310. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.20-0.25:no` used a sample size of 974 markets across 620 event clusters.
Estimate: 0.020. 95% confidence interval: -0.005 to 0.046. Observed range: -1.000 to 0.266.
Raw p-value: 0.123; multiple-testing adjusted q-value: 0.186.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.20-0.25:yes` used a sample size of 1019 markets across 640 event clusters.
Estimate: -0.487. 95% confidence interval: -0.575 to -0.399. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.25-0.30:no` used a sample size of 910 markets across 575 event clusters.
Estimate: -0.022. 95% confidence interval: -0.055 to 0.011. Observed range: -1.000 to 0.351.
Raw p-value: 0.194; multiple-testing adjusted q-value: 0.282.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.25-0.30:yes` used a sample size of 949 markets across 596 event clusters.
Estimate: -0.300. 95% confidence interval: -0.390 to -0.211. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.30-0.35:no` used a sample size of 948 markets across 621 event clusters.
Estimate: 0.024. 95% confidence interval: -0.011 to 0.058. Observed range: -1.000 to 0.449.
Raw p-value: 0.178; multiple-testing adjusted q-value: 0.259.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.30-0.35:yes` used a sample size of 985 markets across 642 event clusters.
Estimate: -0.392. 95% confidence interval: -0.467 to -0.317. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.35-0.40:no` used a sample size of 971 markets across 640 event clusters.
Estimate: 0.026. 95% confidence interval: -0.014 to 0.066. Observed range: -1.000 to 0.562.
Raw p-value: 0.205; multiple-testing adjusted q-value: 0.295.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.35-0.40:yes` used a sample size of 995 markets across 653 event clusters.
Estimate: -0.360. 95% confidence interval: -0.432 to -0.288. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.40-0.45:no` used a sample size of 843 markets across 588 event clusters.
Estimate: -0.015. 95% confidence interval: -0.065 to 0.035. Observed range: -1.000 to 0.695.
Raw p-value: 0.560; multiple-testing adjusted q-value: 0.732.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.40-0.45:yes` used a sample size of 863 markets across 599 event clusters.
Estimate: -0.272. 95% confidence interval: -0.346 to -0.197. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.45-0.50:no` used a sample size of 859 markets across 602 event clusters.
Estimate: 0.005. 95% confidence interval: -0.046 to 0.055. Observed range: -1.000 to 0.852.
Raw p-value: 0.856; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.45-0.50:yes` used a sample size of 882 markets across 616 event clusters.
Estimate: -0.300. 95% confidence interval: -0.363 to -0.236. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.50-0.55:no` used a sample size of 879 markets across 567 event clusters.
Estimate: -0.027. 95% confidence interval: -0.081 to 0.028. Observed range: -1.000 to 1.041.
Raw p-value: 0.336; multiple-testing adjusted q-value: 0.468.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.50-0.55:yes` used a sample size of 905 markets across 583 event clusters.
Estimate: -0.292. 95% confidence interval: -0.354 to -0.230. Observed range: -1.000 to 0.923.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.55-0.60:no` used a sample size of 896 markets across 587 event clusters.
Estimate: -0.030. 95% confidence interval: -0.097 to 0.036. Observed range: -1.000 to 1.273.
Raw p-value: 0.373; multiple-testing adjusted q-value: 0.510.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.55-0.60:yes` used a sample size of 905 markets across 593 event clusters.
Estimate: -0.194. 95% confidence interval: -0.254 to -0.135. Observed range: -1.000 to 0.754.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.60-0.65:no` used a sample size of 991 markets across 632 event clusters.
Estimate: 0.028. 95% confidence interval: -0.043 to 0.098. Observed range: -1.000 to 1.564.
Raw p-value: 0.441; multiple-testing adjusted q-value: 0.590.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.60-0.65:yes` used a sample size of 998 markets across 638 event clusters.
Estimate: -0.228. 95% confidence interval: -0.280 to -0.177. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.65-0.70:no` used a sample size of 1150 markets across 691 event clusters.
Estimate: 0.003. 95% confidence interval: -0.067 to 0.073. Observed range: -1.000 to 1.941.
Raw p-value: 0.929; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.65-0.70:yes` used a sample size of 1167 markets across 704 event clusters.
Estimate: -0.219. 95% confidence interval: -0.264 to -0.174. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.70-0.75:no` used a sample size of 1028 markets across 640 event clusters.
Estimate: -0.006. 95% confidence interval: -0.093 to 0.082. Observed range: -1.000 to 2.448.
Raw p-value: 0.895; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.70-0.75:yes` used a sample size of 1058 markets across 656 event clusters.
Estimate: -0.208. 95% confidence interval: -0.254 to -0.162. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.75-0.80:no` used a sample size of 1095 markets across 696 event clusters.
Estimate: -0.118. 95% confidence interval: -0.203 to -0.033. Observed range: -1.000 to 3.167.
Raw p-value: 0.006; multiple-testing adjusted q-value: 0.011.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.75-0.80:yes` used a sample size of 1163 markets across 710 event clusters.
Estimate: -0.207. 95% confidence interval: -0.247 to -0.167. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.80-0.85:no` used a sample size of 1173 markets across 685 event clusters.
Estimate: -0.141. 95% confidence interval: -0.235 to -0.048. Observed range: -1.000 to 4.556.
Raw p-value: 0.003; multiple-testing adjusted q-value: 0.005.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.80-0.85:yes` used a sample size of 1221 markets across 701 event clusters.
Estimate: -0.187. 95% confidence interval: -0.225 to -0.149. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.85-0.90:no` used a sample size of 1350 markets across 692 event clusters.
Estimate: -0.296. 95% confidence interval: -0.384 to -0.209. Observed range: -1.000 to 6.692.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.85-0.90:yes` used a sample size of 1370 markets across 695 event clusters.
Estimate: -0.132. 95% confidence interval: -0.163 to -0.100. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.90-0.95:no` used a sample size of 1535 markets across 754 event clusters.
Estimate: -0.313. 95% confidence interval: -0.429 to -0.197. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.90-0.95:yes` used a sample size of 1578 markets across 770 event clusters.
Estimate: -0.133. 95% confidence interval: -0.165 to -0.101. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.95-1.00:no` used a sample size of 2618 markets across 979 event clusters.
Estimate: -0.653. 95% confidence interval: -0.752 to -0.553. Observed range: -1.000 to 32.333.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:1d:0.95-1.00:yes` used a sample size of 1883 markets across 847 event clusters.
Estimate: -0.233. 95% confidence interval: -0.280 to -0.187. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.00-0.05:no` used a sample size of 88 markets across 50 event clusters.
Estimate: 0.009. 95% confidence interval: 0.007 to 0.010. Observed range: 0.000 to 0.020.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.00-0.05:yes` used a sample size of 551 markets across 164 event clusters.
Estimate: -1.000. 95% confidence interval: -1.000 to -1.000. Observed range: -1.000 to -1.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.05-0.10:no` used a sample size of 330 markets across 168 event clusters.
Estimate: -0.006. 95% confidence interval: -0.027 to 0.014. Observed range: -1.000 to 0.075.
Raw p-value: 0.554; multiple-testing adjusted q-value: 0.726.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.05-0.10:yes` used a sample size of 426 markets across 192 event clusters.
Estimate: -0.636. 95% confidence interval: -0.817 to -0.455. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.10-0.15:no` used a sample size of 511 markets across 308 event clusters.
Estimate: 0.001. 95% confidence interval: -0.023 to 0.025. Observed range: -1.000 to 0.136.
Raw p-value: 0.930; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.10-0.15:yes` used a sample size of 539 markets across 322 event clusters.
Estimate: -0.530. 95% confidence interval: -0.694 to -0.366. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.15-0.20:no` used a sample size of 771 markets across 457 event clusters.
Estimate: 0.019. 95% confidence interval: -0.005 to 0.043. Observed range: -1.000 to 0.190.
Raw p-value: 0.122; multiple-testing adjusted q-value: 0.185.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.15-0.20:yes` used a sample size of 787 markets across 465 event clusters.
Estimate: -0.486. 95% confidence interval: -0.601 to -0.370. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.20-0.25:no` used a sample size of 851 markets across 522 event clusters.
Estimate: 0.027. 95% confidence interval: -0.000 to 0.054. Observed range: -1.000 to 0.266.
Raw p-value: 0.051; multiple-testing adjusted q-value: 0.080.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.20-0.25:yes` used a sample size of 874 markets across 536 event clusters.
Estimate: -0.498. 95% confidence interval: -0.592 to -0.404. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.25-0.30:no` used a sample size of 820 markets across 495 event clusters.
Estimate: -0.016. 95% confidence interval: -0.051 to 0.018. Observed range: -1.000 to 0.351.
Raw p-value: 0.350; multiple-testing adjusted q-value: 0.483.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.25-0.30:yes` used a sample size of 846 markets across 507 event clusters.
Estimate: -0.305. 95% confidence interval: -0.400 to -0.210. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.30-0.35:no` used a sample size of 860 markets across 541 event clusters.
Estimate: 0.031. 95% confidence interval: -0.005 to 0.067. Observed range: -1.000 to 0.449.
Raw p-value: 0.089; multiple-testing adjusted q-value: 0.137.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.30-0.35:yes` used a sample size of 878 markets across 553 event clusters.
Estimate: -0.399. 95% confidence interval: -0.477 to -0.321. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.35-0.40:no` used a sample size of 879 markets across 562 event clusters.
Estimate: 0.038. 95% confidence interval: -0.004 to 0.080. Observed range: -1.000 to 0.562.
Raw p-value: 0.075; multiple-testing adjusted q-value: 0.116.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.35-0.40:yes` used a sample size of 892 markets across 568 event clusters.
Estimate: -0.382. 95% confidence interval: -0.458 to -0.306. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.40-0.45:no` used a sample size of 781 markets across 533 event clusters.
Estimate: -0.001. 95% confidence interval: -0.052 to 0.051. Observed range: -1.000 to 0.695.
Raw p-value: 0.975; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.40-0.45:yes` used a sample size of 793 markets across 539 event clusters.
Estimate: -0.285. 95% confidence interval: -0.362 to -0.207. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.45-0.50:no` used a sample size of 797 markets across 549 event clusters.
Estimate: 0.010. 95% confidence interval: -0.043 to 0.062. Observed range: -1.000 to 0.852.
Raw p-value: 0.716; multiple-testing adjusted q-value: 0.896.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.45-0.50:yes` used a sample size of 811 markets across 557 event clusters.
Estimate: -0.301. 95% confidence interval: -0.368 to -0.234. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.50-0.55:no` used a sample size of 816 markets across 520 event clusters.
Estimate: -0.013. 95% confidence interval: -0.069 to 0.042. Observed range: -1.000 to 1.041.
Raw p-value: 0.633; multiple-testing adjusted q-value: 0.800.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.50-0.55:yes` used a sample size of 831 markets across 529 event clusters.
Estimate: -0.301. 95% confidence interval: -0.364 to -0.237. Observed range: -1.000 to 0.923.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.55-0.60:no` used a sample size of 841 markets across 540 event clusters.
Estimate: -0.050. 95% confidence interval: -0.119 to 0.018. Observed range: -1.000 to 1.273.
Raw p-value: 0.151; multiple-testing adjusted q-value: 0.223.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.55-0.60:yes` used a sample size of 844 markets across 543 event clusters.
Estimate: -0.171. 95% confidence interval: -0.231 to -0.110. Observed range: -1.000 to 0.754.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.60-0.65:no` used a sample size of 943 markets across 588 event clusters.
Estimate: 0.054. 95% confidence interval: -0.019 to 0.126. Observed range: -1.000 to 1.564.
Raw p-value: 0.146; multiple-testing adjusted q-value: 0.216.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.60-0.65:yes` used a sample size of 947 markets across 591 event clusters.
Estimate: -0.245. 95% confidence interval: -0.298 to -0.192. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.65-0.70:no` used a sample size of 1093 markets across 637 event clusters.
Estimate: -0.005. 95% confidence interval: -0.077 to 0.066. Observed range: -1.000 to 1.941.
Raw p-value: 0.884; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.65-0.70:yes` used a sample size of 1103 markets across 644 event clusters.
Estimate: -0.208. 95% confidence interval: -0.255 to -0.162. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.70-0.75:no` used a sample size of 973 markets across 588 event clusters.
Estimate: -0.004. 95% confidence interval: -0.095 to 0.086. Observed range: -1.000 to 2.448.
Raw p-value: 0.927; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.70-0.75:yes` used a sample size of 979 markets across 594 event clusters.
Estimate: -0.192. 95% confidence interval: -0.239 to -0.145. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.75-0.80:no` used a sample size of 1001 markets across 613 event clusters.
Estimate: -0.098. 95% confidence interval: -0.188 to -0.008. Observed range: -1.000 to 3.167.
Raw p-value: 0.033; multiple-testing adjusted q-value: 0.052.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.75-0.80:yes` used a sample size of 1009 markets across 619 event clusters.
Estimate: -0.171. 95% confidence interval: -0.211 to -0.131. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.80-0.85:no` used a sample size of 1104 markets across 621 event clusters.
Estimate: -0.138. 95% confidence interval: -0.235 to -0.041. Observed range: -1.000 to 4.556.
Raw p-value: 0.005; multiple-testing adjusted q-value: 0.009.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.80-0.85:yes` used a sample size of 1111 markets across 627 event clusters.
Estimate: -0.159. 95% confidence interval: -0.198 to -0.121. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.85-0.90:no` used a sample size of 1276 markets across 624 event clusters.
Estimate: -0.301. 95% confidence interval: -0.390 to -0.211. Observed range: -1.000 to 6.692.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.85-0.90:yes` used a sample size of 1294 markets across 625 event clusters.
Estimate: -0.131. 95% confidence interval: -0.164 to -0.098. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.90-0.95:no` used a sample size of 1422 markets across 665 event clusters.
Estimate: -0.299. 95% confidence interval: -0.421 to -0.177. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.90-0.95:yes` used a sample size of 1444 markets across 668 event clusters.
Estimate: -0.124. 95% confidence interval: -0.158 to -0.091. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.95-1.00:no` used a sample size of 1874 markets across 656 event clusters.
Estimate: -0.638. 95% confidence interval: -0.760 to -0.516. Observed range: -1.000 to 32.333.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:1d:0.95-1.00:yes` used a sample size of 1244 markets across 583 event clusters.
Estimate: -0.088. 95% confidence interval: -0.126 to -0.051. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.00-0.05:no` used a sample size of 146 markets across 89 event clusters.
Estimate: -0.010. 95% confidence interval: -0.029 to 0.010. Observed range: -1.000 to 0.020.
Raw p-value: 0.331; multiple-testing adjusted q-value: 0.465.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.00-0.05:yes` used a sample size of 596 markets across 188 event clusters.
Estimate: -0.924. 95% confidence interval: -1.031 to -0.818. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.05-0.10:no` used a sample size of 207 markets across 129 event clusters.
Estimate: -0.025. 95% confidence interval: -0.058 to 0.008. Observed range: -1.000 to 0.075.
Raw p-value: 0.139; multiple-testing adjusted q-value: 0.208.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.05-0.10:yes` used a sample size of 344 markets across 179 event clusters.
Estimate: -0.556. 95% confidence interval: -0.825 to -0.287. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.10-0.15:no` used a sample size of 204 markets across 125 event clusters.
Estimate: -0.018. 95% confidence interval: -0.055 to 0.019. Observed range: -1.000 to 0.136.
Raw p-value: 0.346; multiple-testing adjusted q-value: 0.480.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.10-0.15:yes` used a sample size of 243 markets across 137 event clusters.
Estimate: -0.468. 95% confidence interval: -0.721 to -0.214. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.15-0.20:no` used a sample size of 247 markets across 145 event clusters.
Estimate: 0.001. 95% confidence interval: -0.044 to 0.047. Observed range: -1.000 to 0.190.
Raw p-value: 0.949; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.15-0.20:yes` used a sample size of 249 markets across 146 event clusters.
Estimate: -0.466. 95% confidence interval: -0.676 to -0.255. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.20-0.25:no` used a sample size of 204 markets across 133 event clusters.
Estimate: 0.023. 95% confidence interval: -0.031 to 0.077. Observed range: -1.000 to 0.266.
Raw p-value: 0.406; multiple-testing adjusted q-value: 0.547.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.20-0.25:yes` used a sample size of 206 markets across 135 event clusters.
Estimate: -0.505. 95% confidence interval: -0.704 to -0.307. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.25-0.30:no` used a sample size of 182 markets across 129 event clusters.
Estimate: -0.031. 95% confidence interval: -0.112 to 0.050. Observed range: -1.000 to 0.351.
Raw p-value: 0.459; multiple-testing adjusted q-value: 0.612.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.25-0.30:yes` used a sample size of 187 markets across 134 event clusters.
Estimate: -0.322. 95% confidence interval: -0.545 to -0.099. Observed range: -1.000 to 2.704.
Raw p-value: 0.005; multiple-testing adjusted q-value: 0.008.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.30-0.35:no` used a sample size of 171 markets across 123 event clusters.
Estimate: -0.041. 95% confidence interval: -0.124 to 0.042. Observed range: -1.000 to 0.449.
Raw p-value: 0.333; multiple-testing adjusted q-value: 0.466.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.30-0.35:yes` used a sample size of 171 markets across 123 event clusters.
Estimate: -0.208. 95% confidence interval: -0.396 to -0.020. Observed range: -1.000 to 2.125.
Raw p-value: 0.030; multiple-testing adjusted q-value: 0.049.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.35-0.40:no` used a sample size of 178 markets across 130 event clusters.
Estimate: 0.040. 95% confidence interval: -0.052 to 0.132. Observed range: -1.000 to 0.562.
Raw p-value: 0.397; multiple-testing adjusted q-value: 0.538.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.35-0.40:yes` used a sample size of 178 markets across 130 event clusters.
Estimate: -0.411. 95% confidence interval: -0.584 to -0.238. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.40-0.45:no` used a sample size of 172 markets across 126 event clusters.
Estimate: 0.027. 95% confidence interval: -0.077 to 0.132. Observed range: -1.000 to 0.695.
Raw p-value: 0.610; multiple-testing adjusted q-value: 0.783.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.40-0.45:yes` used a sample size of 172 markets across 126 event clusters.
Estimate: -0.338. 95% confidence interval: -0.500 to -0.176. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.45-0.50:no` used a sample size of 180 markets across 130 event clusters.
Estimate: -0.008. 95% confidence interval: -0.132 to 0.116. Observed range: -1.000 to 0.852.
Raw p-value: 0.902; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.45-0.50:yes` used a sample size of 183 markets across 133 event clusters.
Estimate: -0.264. 95% confidence interval: -0.424 to -0.104. Observed range: -1.000 to 1.128.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.002.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.50-0.55:no` used a sample size of 150 markets across 102 event clusters.
Estimate: -0.013. 95% confidence interval: -0.178 to 0.151. Observed range: -1.000 to 1.041.
Raw p-value: 0.875; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.50-0.55:yes` used a sample size of 151 markets across 103 event clusters.
Estimate: -0.221. 95% confidence interval: -0.403 to -0.039. Observed range: -1.000 to 0.923.
Raw p-value: 0.017; multiple-testing adjusted q-value: 0.029.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.55-0.60:no` used a sample size of 187 markets across 111 event clusters.
Estimate: -0.038. 95% confidence interval: -0.180 to 0.105. Observed range: -1.000 to 1.273.
Raw p-value: 0.604; multiple-testing adjusted q-value: 0.778.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.55-0.60:yes` used a sample size of 187 markets across 111 event clusters.
Estimate: -0.185. 95% confidence interval: -0.317 to -0.053. Observed range: -1.000 to 0.754.
Raw p-value: 0.006; multiple-testing adjusted q-value: 0.010.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.60-0.65:no` used a sample size of 210 markets across 131 event clusters.
Estimate: 0.044. 95% confidence interval: -0.098 to 0.185. Observed range: -1.000 to 1.564.
Raw p-value: 0.543; multiple-testing adjusted q-value: 0.713.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.60-0.65:yes` used a sample size of 210 markets across 131 event clusters.
Estimate: -0.251. 95% confidence interval: -0.363 to -0.139. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.65-0.70:no` used a sample size of 228 markets across 147 event clusters.
Estimate: 0.027. 95% confidence interval: -0.135 to 0.189. Observed range: -1.000 to 1.941.
Raw p-value: 0.745; multiple-testing adjusted q-value: 0.925.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.65-0.70:yes` used a sample size of 229 markets across 147 event clusters.
Estimate: -0.228. 95% confidence interval: -0.329 to -0.127. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.70-0.75:no` used a sample size of 209 markets across 142 event clusters.
Estimate: -0.048. 95% confidence interval: -0.217 to 0.121. Observed range: -1.000 to 2.333.
Raw p-value: 0.576; multiple-testing adjusted q-value: 0.745.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.70-0.75:yes` used a sample size of 211 markets across 143 event clusters.
Estimate: -0.175. 95% confidence interval: -0.267 to -0.083. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.75-0.80:no` used a sample size of 232 markets across 153 event clusters.
Estimate: 0.235. 95% confidence interval: 0.024 to 0.446. Observed range: -1.000 to 3.000.
Raw p-value: 0.029; multiple-testing adjusted q-value: 0.047.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.75-0.80:yes` used a sample size of 241 markets across 159 event clusters.
Estimate: -0.298. 95% confidence interval: -0.387 to -0.208. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.80-0.85:no` used a sample size of 199 markets across 114 event clusters.
Estimate: -0.041. 95% confidence interval: -0.286 to 0.205. Observed range: -1.000 to 4.000.
Raw p-value: 0.745; multiple-testing adjusted q-value: 0.925.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.80-0.85:yes` used a sample size of 203 markets across 117 event clusters.
Estimate: -0.234. 95% confidence interval: -0.335 to -0.133. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.85-0.90:no` used a sample size of 198 markets across 121 event clusters.
Estimate: 0.005. 95% confidence interval: -0.298 to 0.308. Observed range: -1.000 to 6.143.
Raw p-value: 0.974; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.85-0.90:yes` used a sample size of 200 markets across 123 event clusters.
Estimate: -0.233. 95% confidence interval: -0.335 to -0.131. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.90-0.95:no` used a sample size of 239 markets across 140 event clusters.
Estimate: -0.141. 95% confidence interval: -0.432 to 0.150. Observed range: -1.000 to 10.111.
Raw p-value: 0.342; multiple-testing adjusted q-value: 0.476.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.90-0.95:yes` used a sample size of 252 markets across 141 event clusters.
Estimate: -0.214. 95% confidence interval: -0.300 to -0.128. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.95-1.00:no` used a sample size of 390 markets across 185 event clusters.
Estimate: -0.700. 95% confidence interval: -0.896 to -0.505. Observed range: -1.000 to 19.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:7d:0.95-1.00:yes` used a sample size of 320 markets across 160 event clusters.
Estimate: -0.155. 95% confidence interval: -0.236 to -0.073. Observed range: -1.000 to 0.042.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

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
Raw p-value: 0.417; multiple-testing adjusted q-value: 0.560.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.05-0.10:yes` used a sample size of 66 markets across 44 event clusters.
Estimate: -0.848. 95% confidence interval: -1.149 to -0.548. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.10-0.15:no` used a sample size of 121 markets across 61 event clusters.
Estimate: 0.020. 95% confidence interval: -0.013 to 0.054. Observed range: -1.000 to 0.136.
Raw p-value: 0.231; multiple-testing adjusted q-value: 0.330.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.10-0.15:yes` used a sample size of 124 markets across 61 event clusters.
Estimate: -0.719. 95% confidence interval: -0.984 to -0.454. Observed range: -1.000 to 8.091.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.15-0.20:no` used a sample size of 191 markets across 96 event clusters.
Estimate: -0.006. 95% confidence interval: -0.060 to 0.049. Observed range: -1.000 to 0.190.
Raw p-value: 0.831; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.15-0.20:yes` used a sample size of 191 markets across 96 event clusters.
Estimate: -0.450. 95% confidence interval: -0.698 to -0.203. Observed range: -1.000 to 5.250.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.20-0.25:no` used a sample size of 154 markets across 95 event clusters.
Estimate: 0.043. 95% confidence interval: -0.019 to 0.104. Observed range: -1.000 to 0.266.
Raw p-value: 0.176; multiple-testing adjusted q-value: 0.258.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.20-0.25:yes` used a sample size of 154 markets across 95 event clusters.
Estimate: -0.554. 95% confidence interval: -0.783 to -0.326. Observed range: -1.000 to 3.545.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.25-0.30:no` used a sample size of 151 markets across 107 event clusters.
Estimate: -0.025. 95% confidence interval: -0.115 to 0.064. Observed range: -1.000 to 0.351.
Raw p-value: 0.581; multiple-testing adjusted q-value: 0.750.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.25-0.30:yes` used a sample size of 151 markets across 107 event clusters.
Estimate: -0.323. 95% confidence interval: -0.573 to -0.072. Observed range: -1.000 to 2.704.
Raw p-value: 0.012; multiple-testing adjusted q-value: 0.019.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.30-0.35:no` used a sample size of 147 markets across 101 event clusters.
Estimate: -0.026. 95% confidence interval: -0.115 to 0.062. Observed range: -1.000 to 0.449.
Raw p-value: 0.562; multiple-testing adjusted q-value: 0.732.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.30-0.35:yes` used a sample size of 147 markets across 101 event clusters.
Estimate: -0.242. 95% confidence interval: -0.441 to -0.043. Observed range: -1.000 to 2.125.
Raw p-value: 0.017; multiple-testing adjusted q-value: 0.029.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.35-0.40:no` used a sample size of 145 markets across 102 event clusters.
Estimate: 0.071. 95% confidence interval: -0.021 to 0.163. Observed range: -1.000 to 0.562.
Raw p-value: 0.129; multiple-testing adjusted q-value: 0.194.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.35-0.40:yes` used a sample size of 145 markets across 102 event clusters.
Estimate: -0.472. 95% confidence interval: -0.644 to -0.301. Observed range: -1.000 to 1.703.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.40-0.45:no` used a sample size of 148 markets across 102 event clusters.
Estimate: 0.066. 95% confidence interval: -0.044 to 0.176. Observed range: -1.000 to 0.695.
Raw p-value: 0.240; multiple-testing adjusted q-value: 0.343.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.40-0.45:yes` used a sample size of 148 markets across 102 event clusters.
Estimate: -0.399. 95% confidence interval: -0.570 to -0.228. Observed range: -1.000 to 1.381.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.45-0.50:no` used a sample size of 163 markets across 116 event clusters.
Estimate: 0.027. 95% confidence interval: -0.101 to 0.155. Observed range: -1.000 to 0.852.
Raw p-value: 0.683; multiple-testing adjusted q-value: 0.859.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.45-0.50:yes` used a sample size of 165 markets across 118 event clusters.
Estimate: -0.307. 95% confidence interval: -0.472 to -0.141. Observed range: -1.000 to 1.128.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.50-0.55:no` used a sample size of 116 markets across 80 event clusters.
Estimate: 0.070. 95% confidence interval: -0.093 to 0.234. Observed range: -1.000 to 1.041.
Raw p-value: 0.398; multiple-testing adjusted q-value: 0.539.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.50-0.55:yes` used a sample size of 117 markets across 81 event clusters.
Estimate: -0.300. 95% confidence interval: -0.469 to -0.131. Observed range: -1.000 to 0.923.
Raw p-value: 0.001; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.55-0.60:no` used a sample size of 156 markets across 84 event clusters.
Estimate: 0.037. 95% confidence interval: -0.115 to 0.188. Observed range: -1.000 to 1.273.
Raw p-value: 0.634; multiple-testing adjusted q-value: 0.800.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.55-0.60:yes` used a sample size of 156 markets across 84 event clusters.
Estimate: -0.250. 95% confidence interval: -0.391 to -0.110. Observed range: -1.000 to 0.754.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.001.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.60-0.65:no` used a sample size of 180 markets across 109 event clusters.
Estimate: 0.039. 95% confidence interval: -0.113 to 0.191. Observed range: -1.000 to 1.564.
Raw p-value: 0.614; multiple-testing adjusted q-value: 0.785.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.60-0.65:yes` used a sample size of 180 markets across 109 event clusters.
Estimate: -0.239. 95% confidence interval: -0.357 to -0.121. Observed range: -1.000 to 0.613.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.65-0.70:no` used a sample size of 195 markets across 118 event clusters.
Estimate: -0.002. 95% confidence interval: -0.174 to 0.171. Observed range: -1.000 to 1.857.
Raw p-value: 0.985; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.65-0.70:yes` used a sample size of 195 markets across 118 event clusters.
Estimate: -0.205. 95% confidence interval: -0.313 to -0.097. Observed range: -1.000 to 0.493.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.70-0.75:no` used a sample size of 183 markets across 120 event clusters.
Estimate: 0.004. 95% confidence interval: -0.179 to 0.187. Observed range: -1.000 to 2.333.
Raw p-value: 0.969; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.70-0.75:yes` used a sample size of 183 markets across 120 event clusters.
Estimate: -0.189. 95% confidence interval: -0.287 to -0.091. Observed range: -1.000 to 0.389.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.75-0.80:no` used a sample size of 204 markets across 126 event clusters.
Estimate: 0.230. 95% confidence interval: 0.004 to 0.456. Observed range: -1.000 to 3.000.
Raw p-value: 0.046; multiple-testing adjusted q-value: 0.073.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.75-0.80:yes` used a sample size of 206 markets across 128 event clusters.
Estimate: -0.289. 95% confidence interval: -0.387 to -0.191. Observed range: -1.000 to 0.299.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.80-0.85:no` used a sample size of 162 markets across 85 event clusters.
Estimate: 0.016. 95% confidence interval: -0.267 to 0.299. Observed range: -1.000 to 4.000.
Raw p-value: 0.912; multiple-testing adjusted q-value: 1.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.80-0.85:yes` used a sample size of 163 markets across 86 event clusters.
Estimate: -0.252. 95% confidence interval: -0.369 to -0.135. Observed range: -1.000 to 0.220.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.85-0.90:no` used a sample size of 159 markets across 86 event clusters.
Estimate: 0.122. 95% confidence interval: -0.234 to 0.478. Observed range: -1.000 to 6.143.
Raw p-value: 0.502; multiple-testing adjusted q-value: 0.663.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.85-0.90:yes` used a sample size of 160 markets across 87 event clusters.
Estimate: -0.269. 95% confidence interval: -0.388 to -0.149. Observed range: -1.000 to 0.163.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.90-0.95:no` used a sample size of 176 markets across 98 event clusters.
Estimate: -0.147. 95% confidence interval: -0.474 to 0.179. Observed range: -1.000 to 10.111.
Raw p-value: 0.376; multiple-testing adjusted q-value: 0.511.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.90-0.95:yes` used a sample size of 188 markets across 98 event clusters.
Estimate: -0.226. 95% confidence interval: -0.330 to -0.122. Observed range: -1.000 to 0.099.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.95-1.00:no` used a sample size of 157 markets across 74 event clusters.
Estimate: -0.371. 95% confidence interval: -0.843 to 0.102. Observed range: -1.000 to 19.000.
Raw p-value: 0.124; multiple-testing adjusted q-value: 0.187.

### Favorite-longshot — candidate (discovery only)

Hypothesis `favorite_longshot:mentions:7d:0.95-1.00:yes` used a sample size of 152 markets across 71 event clusters.
Estimate: -0.160. 95% confidence interval: -0.299 to -0.021. Observed range: -1.000 to 0.042.
Raw p-value: 0.024; multiple-testing adjusted q-value: 0.040.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Climate and Weather:1h:no` used a sample size of 102 markets across 72 event clusters.
Estimate: -0.940. 95% confidence interval: -0.992 to -0.888. Observed range: -1.000 to 0.053.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Climate and Weather:1h:yes` used a sample size of 483 markets across 199 event clusters.
Estimate: -0.983. 95% confidence interval: -0.994 to -0.972. Observed range: -1.000 to 0.010.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Commodities:1h:no` used a sample size of 61 markets across 4 event clusters.
Estimate: -0.950. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.020.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Commodities:1h:yes` used a sample size of 16 markets across 4 event clusters.
Estimate: -0.321. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.587.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Companies:1h:no` used a sample size of 2 markets across 2 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 2 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Companies:1h:yes` used a sample size of 9 markets across 5 event clusters.
Estimate: -0.773. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.042.
Not tested: only 5 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Crypto:1h:no` used a sample size of 100 markets across 11 event clusters.
Estimate: -0.935. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.222.
Not tested: only 11 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Crypto:1h:yes` used a sample size of 140 markets across 19 event clusters.
Estimate: -0.731. 95% confidence interval: not available to not available. Observed range: -1.000 to 2.704.
Not tested: only 19 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Economics:1h:no` used a sample size of 164 markets across 50 event clusters.
Estimate: -0.223. 95% confidence interval: -0.689 to 0.244. Observed range: -1.000 to 24.000.
Raw p-value: 0.350; multiple-testing adjusted q-value: 0.483.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Economics:1h:yes` used a sample size of 180 markets across 49 event clusters.
Estimate: -0.724. 95% confidence interval: -0.805 to -0.644. Observed range: -1.000 to 1.439.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Elections:1h:no` used a sample size of 38 markets across 35 event clusters.
Estimate: -0.894. 95% confidence interval: -1.010 to -0.779. Observed range: -1.000 to 0.010.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Elections:1h:yes` used a sample size of 164 markets across 50 event clusters.
Estimate: -0.975. 95% confidence interval: -1.000 to -0.951. Observed range: -1.000 to 0.020.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Entertainment:1h:no` used a sample size of 800 markets across 389 event clusters.
Estimate: -0.616. 95% confidence interval: -0.687 to -0.546. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Entertainment:1h:yes` used a sample size of 2187 markets across 408 event clusters.
Estimate: -0.899. 95% confidence interval: -0.918 to -0.881. Observed range: -1.000 to 6.692.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Financials:1h:no` used a sample size of 951 markets across 47 event clusters.
Estimate: -0.765. 95% confidence interval: -0.912 to -0.619. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Financials:1h:yes` used a sample size of 951 markets across 60 event clusters.
Estimate: -0.784. 95% confidence interval: -0.918 to -0.650. Observed range: -1.000 to 2.333.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Health:1h:no` used a sample size of 6 markets across 2 event clusters.
Estimate: 0.099. 95% confidence interval: not available to not available. Observed range: 0.000 to 0.351.
Not tested: only 2 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Health:1h:yes` used a sample size of 13 markets across 5 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 5 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:1h:no` used a sample size of 10254 markets across 1049 event clusters.
Estimate: -0.743. 95% confidence interval: -0.774 to -0.712. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:1h:yes` used a sample size of 10036 markets across 1069 event clusters.
Estimate: -0.846. 95% confidence interval: -0.873 to -0.819. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Politics:1h:no` used a sample size of 199 markets across 67 event clusters.
Estimate: -0.890. 95% confidence interval: -0.958 to -0.822. Observed range: -1.000 to 0.429.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Politics:1h:yes` used a sample size of 342 markets across 108 event clusters.
Estimate: -0.876. 95% confidence interval: -0.930 to -0.822. Observed range: -1.000 to 3.167.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Science and Technology:1h:no` used a sample size of 8 markets across 4 event clusters.
Estimate: -0.747. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.020.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Science and Technology:1h:yes` used a sample size of 28 markets across 14 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 14 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Social:1h:no` used a sample size of 1 markets across 1 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 1 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Social:1h:yes` used a sample size of 2 markets across 2 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 2 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Sports:1h:no` used a sample size of 428 markets across 90 event clusters.
Estimate: -0.409. 95% confidence interval: -0.522 to -0.297. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Sports:1h:yes` used a sample size of 649 markets across 96 event clusters.
Estimate: -0.313. 95% confidence interval: -0.462 to -0.164. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Transportation:1h:no` used a sample size of 31 markets across 31 event clusters.
Estimate: -1.000. 95% confidence interval: -1.000 to -1.000. Observed range: -1.000 to -1.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Transportation:1h:yes` used a sample size of 49 markets across 48 event clusters.
Estimate: -0.979. 95% confidence interval: -1.020 to -0.938. Observed range: -1.000 to 0.031.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:World:1h:no` used a sample size of 4 markets across 4 event clusters.
Estimate: -0.495. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.020.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:World:1h:yes` used a sample size of 7 markets across 7 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 7 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:annual:1h:no` used a sample size of 159 markets across 56 event clusters.
Estimate: -0.579. 95% confidence interval: -0.730 to -0.429. Observed range: -1.000 to 1.941.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:annual:1h:yes` used a sample size of 447 markets across 68 event clusters.
Estimate: -0.825. 95% confidence interval: -0.892 to -0.758. Observed range: -1.000 to 6.692.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:1h:no` used a sample size of 1949 markets across 311 event clusters.
Estimate: -0.532. 95% confidence interval: -0.609 to -0.454. Observed range: -1.000 to 19.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:1h:yes` used a sample size of 2514 markets across 371 event clusters.
Estimate: -0.674. 95% confidence interval: -0.738 to -0.611. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:daily:1h:no` used a sample size of 446 markets across 346 event clusters.
Estimate: -0.704. 95% confidence interval: -0.783 to -0.625. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:daily:1h:yes` used a sample size of 1643 markets across 497 event clusters.
Estimate: -0.931. 95% confidence interval: -0.943 to -0.920. Observed range: -1.000 to 1.564.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:hourly:1h:no` used a sample size of 913 markets across 17 event clusters.
Estimate: -0.808. 95% confidence interval: not available to not available. Observed range: -1.000 to 3.167.
Not tested: only 17 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:hourly:1h:yes` used a sample size of 895 markets across 17 event clusters.
Estimate: -0.808. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.493.
Not tested: only 17 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:monthly:1h:no` used a sample size of 217 markets across 43 event clusters.
Estimate: -0.460. 95% confidence interval: -0.862 to -0.058. Observed range: -1.000 to 24.000.
Raw p-value: 0.025; multiple-testing adjusted q-value: 0.041.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:monthly:1h:yes` used a sample size of 230 markets across 43 event clusters.
Estimate: -0.708. 95% confidence interval: -0.851 to -0.565. Observed range: -1.000 to 2.704.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:1h:no` used a sample size of 9418 markets across 1066 event clusters.
Estimate: -0.769. 95% confidence interval: -0.798 to -0.739. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:1h:yes` used a sample size of 9480 markets across 1127 event clusters.
Estimate: -0.862. 95% confidence interval: -0.889 to -0.836. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:weekly:1h:no` used a sample size of 47 markets across 19 event clusters.
Estimate: -0.726. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.128.
Not tested: only 19 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:weekly:1h:yes` used a sample size of 47 markets across 20 event clusters.
Estimate: -0.615. 95% confidence interval: not available to not available. Observed range: -1.000 to 5.250.
Not tested: only 20 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:1h:1h:no` used a sample size of 13149 markets across 1858 event clusters.
Estimate: -0.726. 95% confidence interval: -0.754 to -0.699. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:1h:1h:yes` used a sample size of 15256 markets across 2143 event clusters.
Estimate: -0.831. 95% confidence interval: -0.853 to -0.809. Observed range: -1.000 to 49.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Climate and Weather:1d:no` used a sample size of 372 markets across 73 event clusters.
Estimate: -0.145. 95% confidence interval: -0.206 to -0.084. Observed range: -1.000 to 1.083.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Climate and Weather:1d:yes` used a sample size of 411 markets across 74 event clusters.
Estimate: -0.477. 95% confidence interval: -0.571 to -0.382. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Commodities:1d:no` used a sample size of 65 markets across 5 event clusters.
Estimate: -0.900. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.190.
Not tested: only 5 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Commodities:1d:yes` used a sample size of 42 markets across 5 event clusters.
Estimate: 0.095. 95% confidence interval: not available to not available. Observed range: -1.000 to 2.125.
Not tested: only 5 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Companies:1d:no` used a sample size of 2 markets across 2 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 2 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Companies:1d:yes` used a sample size of 10 markets across 5 event clusters.
Estimate: -0.758. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.408.
Not tested: only 5 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Crypto:1d:no` used a sample size of 124 markets across 12 event clusters.
Estimate: -0.690. 95% confidence interval: not available to not available. Observed range: -1.000 to 2.226.
Not tested: only 12 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Crypto:1d:yes` used a sample size of 157 markets across 18 event clusters.
Estimate: -0.391. 95% confidence interval: not available to not available. Observed range: -1.000 to 13.286.
Not tested: only 18 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Economics:1d:no` used a sample size of 163 markets across 45 event clusters.
Estimate: -0.063. 95% confidence interval: -0.675 to 0.549. Observed range: -1.000 to 32.333.
Raw p-value: 0.841; multiple-testing adjusted q-value: 1.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Economics:1d:yes` used a sample size of 192 markets across 46 event clusters.
Estimate: -0.677. 95% confidence interval: -0.783 to -0.570. Observed range: -1.000 to 2.125.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Elections:1d:no` used a sample size of 57 markets across 38 event clusters.
Estimate: -0.728. 95% confidence interval: -0.936 to -0.519. Observed range: -1.000 to 0.471.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Elections:1d:yes` used a sample size of 185 markets across 54 event clusters.
Estimate: -0.869. 95% confidence interval: -1.003 to -0.734. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Entertainment:1d:no` used a sample size of 1164 markets across 376 event clusters.
Estimate: -0.173. 95% confidence interval: -0.253 to -0.093. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Entertainment:1d:yes` used a sample size of 2440 markets across 428 event clusters.
Estimate: -0.640. 95% confidence interval: -0.695 to -0.585. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Financials:1d:no` used a sample size of 69 markets across 20 event clusters.
Estimate: -0.338. 95% confidence interval: not available to not available. Observed range: -1.000 to 7.333.
Not tested: only 20 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Financials:1d:yes` used a sample size of 79 markets across 26 event clusters.
Estimate: -0.585. 95% confidence interval: not available to not available. Observed range: -1.000 to 3.348.
Not tested: only 26 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Health:1d:no` used a sample size of 5 markets across 1 event clusters.
Estimate: 0.120. 95% confidence interval: not available to not available. Observed range: 0.000 to 0.370.
Not tested: only 1 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Health:1d:yes` used a sample size of 12 markets across 4 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:1d:no` used a sample size of 18031 markets across 1138 event clusters.
Estimate: -0.121. 95% confidence interval: -0.150 to -0.092. Observed range: -1.000 to 32.333.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:1d:yes` used a sample size of 18203 markets across 1141 event clusters.
Estimate: -0.285. 95% confidence interval: -0.306 to -0.264. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Politics:1d:no` used a sample size of 276 markets across 81 event clusters.
Estimate: -0.578. 95% confidence interval: -0.730 to -0.427. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Politics:1d:yes` used a sample size of 431 markets across 125 event clusters.
Estimate: -0.449. 95% confidence interval: -0.623 to -0.275. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Science and Technology:1d:no` used a sample size of 7 markets across 6 event clusters.
Estimate: -0.538. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.235.
Not tested: only 6 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Science and Technology:1d:yes` used a sample size of 27 markets across 13 event clusters.
Estimate: -0.962. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.020.
Not tested: only 13 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Social:1d:no` used a sample size of 2 markets across 2 event clusters.
Estimate: -0.500. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.000.
Not tested: only 2 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Social:1d:yes` used a sample size of 3 markets across 3 event clusters.
Estimate: -0.667. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.000.
Not tested: only 3 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Sports:1d:no` used a sample size of 276 markets across 53 event clusters.
Estimate: -0.280. 95% confidence interval: -0.426 to -0.134. Observed range: -1.000 to 3.762.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Sports:1d:yes` used a sample size of 308 markets across 53 event clusters.
Estimate: -0.022. 95% confidence interval: -0.288 to 0.244. Observed range: -1.000 to 7.333.
Raw p-value: 0.872; multiple-testing adjusted q-value: 1.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Transportation:1d:no` used a sample size of 76 markets across 74 event clusters.
Estimate: 0.061. 95% confidence interval: -0.344 to 0.467. Observed range: -1.000 to 13.286.
Raw p-value: 0.767; multiple-testing adjusted q-value: 0.949.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Transportation:1d:yes` used a sample size of 75 markets across 73 event clusters.
Estimate: -0.426. 95% confidence interval: -0.640 to -0.213. Observed range: -1.000 to 4.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:World:1d:no` used a sample size of 5 markets across 5 event clusters.
Estimate: 0.051. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.174.
Not tested: only 5 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:World:1d:yes` used a sample size of 10 markets across 10 event clusters.
Estimate: -0.880. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.205.
Not tested: only 10 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:annual:1d:no` used a sample size of 254 markets across 62 event clusters.
Estimate: -0.133. 95% confidence interval: -0.309 to 0.042. Observed range: -1.000 to 10.111.
Raw p-value: 0.137; multiple-testing adjusted q-value: 0.204.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:annual:1d:yes` used a sample size of 472 markets across 78 event clusters.
Estimate: -0.430. 95% confidence interval: -0.649 to -0.212. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:1d:no` used a sample size of 2510 markets across 292 event clusters.
Estimate: -0.163. 95% confidence interval: -0.230 to -0.095. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:1d:yes` used a sample size of 2857 markets across 344 event clusters.
Estimate: -0.411. 95% confidence interval: -0.469 to -0.354. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:daily:1d:no` used a sample size of 854 markets across 342 event clusters.
Estimate: -0.017. 95% confidence interval: -0.100 to 0.066. Observed range: -1.000 to 15.667.
Raw p-value: 0.692; multiple-testing adjusted q-value: 0.868.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:daily:1d:yes` used a sample size of 1710 markets across 382 event clusters.
Estimate: -0.606. 95% confidence interval: -0.659 to -0.552. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:hourly:1d:no` used a sample size of 87 markets across 3 event clusters.
Estimate: -0.650. 95% confidence interval: not available to not available. Observed range: -1.000 to 2.226.
Not tested: only 3 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:hourly:1d:yes` used a sample size of 76 markets across 3 event clusters.
Estimate: -0.643. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.632.
Not tested: only 3 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:monthly:1d:no` used a sample size of 225 markets across 43 event clusters.
Estimate: -0.362. 95% confidence interval: -0.862 to 0.137. Observed range: -1.000 to 32.333.
Raw p-value: 0.155; multiple-testing adjusted q-value: 0.229.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:monthly:1d:yes` used a sample size of 276 markets across 44 event clusters.
Estimate: -0.442. 95% confidence interval: -0.764 to -0.120. Observed range: -1.000 to 13.286.
Raw p-value: 0.007; multiple-testing adjusted q-value: 0.012.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:1d:no` used a sample size of 16715 markets across 1167 event clusters.
Estimate: -0.135. 95% confidence interval: -0.165 to -0.105. Observed range: -1.000 to 32.333.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:1d:yes` used a sample size of 17147 markets across 1206 event clusters.
Estimate: -0.294. 95% confidence interval: -0.316 to -0.272. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:weekly:1d:no` used a sample size of 49 markets across 22 event clusters.
Estimate: -0.716. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.041.
Not tested: only 22 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:weekly:1d:yes` used a sample size of 47 markets across 21 event clusters.
Estimate: -0.340. 95% confidence interval: not available to not available. Observed range: -1.000 to 5.250.
Not tested: only 21 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:1d:1d:no` used a sample size of 20694 markets across 1931 event clusters.
Estimate: -0.140. 95% confidence interval: -0.166 to -0.113. Observed range: -1.000 to 32.333.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:1d:1d:yes` used a sample size of 22585 markets across 2078 event clusters.
Estimate: -0.338. 95% confidence interval: -0.358 to -0.318. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Climate and Weather:7d:no` used a sample size of 58 markets across 16 event clusters.
Estimate: -0.365. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.439.
Not tested: only 16 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Climate and Weather:7d:yes` used a sample size of 62 markets across 17 event clusters.
Estimate: -0.519. 95% confidence interval: not available to not available. Observed range: -1.000 to 5.667.
Not tested: only 17 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Commodities:7d:no` used a sample size of 43 markets across 3 event clusters.
Estimate: -0.884. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.282.
Not tested: only 3 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Commodities:7d:yes` used a sample size of 44 markets across 4 event clusters.
Estimate: 0.674. 95% confidence interval: not available to not available. Observed range: -1.000 to 19.000.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Companies:7d:no` used a sample size of 3 markets across 3 event clusters.
Estimate: -0.663. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.010.
Not tested: only 3 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Companies:7d:yes` used a sample size of 7 markets across 4 event clusters.
Estimate: -0.589. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.639.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Crypto:7d:no` used a sample size of 31 markets across 11 event clusters.
Estimate: -0.437. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.149.
Not tested: only 11 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Crypto:7d:yes` used a sample size of 59 markets across 15 event clusters.
Estimate: -0.007. 95% confidence interval: not available to not available. Observed range: -1.000 to 24.000.
Not tested: only 15 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Economics:7d:no` used a sample size of 101 markets across 29 event clusters.
Estimate: -0.349. 95% confidence interval: not available to not available. Observed range: -1.000 to 3.167.
Not tested: only 29 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Economics:7d:yes` used a sample size of 119 markets across 29 event clusters.
Estimate: -0.253. 95% confidence interval: not available to not available. Observed range: -1.000 to 11.500.
Not tested: only 29 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Elections:7d:no` used a sample size of 53 markets across 32 event clusters.
Estimate: -0.133. 95% confidence interval: -0.490 to 0.223. Observed range: -1.000 to 7.333.
Raw p-value: 0.463; multiple-testing adjusted q-value: 0.617.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Elections:7d:yes` used a sample size of 152 markets across 48 event clusters.
Estimate: -0.829. 95% confidence interval: -0.931 to -0.727. Observed range: -1.000 to 5.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Entertainment:7d:no` used a sample size of 560 markets across 126 event clusters.
Estimate: -0.143. 95% confidence interval: -0.243 to -0.043. Observed range: -1.000 to 10.111.
Raw p-value: 0.005; multiple-testing adjusted q-value: 0.009.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Entertainment:7d:yes` used a sample size of 838 markets across 135 event clusters.
Estimate: -0.576. 95% confidence interval: -0.656 to -0.496. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Financials:7d:no` used a sample size of 54 markets across 15 event clusters.
Estimate: -0.463. 95% confidence interval: not available to not available. Observed range: -1.000 to 2.125.
Not tested: only 15 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Financials:7d:yes` used a sample size of 65 markets across 20 event clusters.
Estimate: -0.363. 95% confidence interval: not available to not available. Observed range: -1.000 to 10.111.
Not tested: only 20 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Health:7d:no` used a sample size of 6 markets across 3 event clusters.
Estimate: 0.046. 95% confidence interval: not available to not available. Observed range: 0.000 to 0.136.
Not tested: only 3 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Health:7d:yes` used a sample size of 12 markets across 4 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:7d:no` used a sample size of 2980 markets across 234 event clusters.
Estimate: 0.011. 95% confidence interval: -0.057 to 0.079. Observed range: -1.000 to 19.000.
Raw p-value: 0.759; multiple-testing adjusted q-value: 0.941.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Mentions:7d:yes` used a sample size of 3013 markets across 234 event clusters.
Estimate: -0.333. 95% confidence interval: -0.384 to -0.281. Observed range: -1.000 to 9.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Politics:7d:no` used a sample size of 206 markets across 76 event clusters.
Estimate: -0.360. 95% confidence interval: -0.503 to -0.216. Observed range: -1.000 to 4.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Politics:7d:yes` used a sample size of 308 markets across 99 event clusters.
Estimate: -0.372. 95% confidence interval: -0.556 to -0.188. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Science and Technology:7d:no` used a sample size of 13 markets across 6 event clusters.
Estimate: -0.086. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.493.
Not tested: only 6 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Science and Technology:7d:yes` used a sample size of 25 markets across 11 event clusters.
Estimate: -0.859. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.500.
Not tested: only 11 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Social:7d:no` used a sample size of 1 markets across 1 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 1 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Social:7d:yes` used a sample size of 2 markets across 2 event clusters.
Estimate: 0.282. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.564.
Not tested: only 2 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Sports:7d:no` used a sample size of 22 markets across 8 event clusters.
Estimate: -0.153. 95% confidence interval: not available to not available. Observed range: -1.000 to 1.381.
Not tested: only 8 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:Sports:7d:yes` used a sample size of 22 markets across 8 event clusters.
Estimate: -0.244. 95% confidence interval: not available to not available. Observed range: -1.000 to 2.030.
Not tested: only 8 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:World:7d:no` used a sample size of 2 markets across 2 event clusters.
Estimate: -0.474. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.053.
Not tested: only 2 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:category:World:7d:yes` used a sample size of 5 markets across 5 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 5 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:annual:7d:no` used a sample size of 185 markets across 47 event clusters.
Estimate: -0.144. 95% confidence interval: -0.322 to 0.034. Observed range: -1.000 to 10.111.
Raw p-value: 0.112; multiple-testing adjusted q-value: 0.171.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:annual:7d:yes` used a sample size of 327 markets across 58 event clusters.
Estimate: -0.488. 95% confidence interval: -0.645 to -0.330. Observed range: -1.000 to 19.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:7d:no` used a sample size of 1083 markets across 167 event clusters.
Estimate: -0.047. 95% confidence interval: -0.146 to 0.052. Observed range: -1.000 to 10.111.
Raw p-value: 0.352; multiple-testing adjusted q-value: 0.485.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:custom:7d:yes` used a sample size of 1265 markets across 204 event clusters.
Estimate: -0.427. 95% confidence interval: -0.504 to -0.350. Observed range: -1.000 to 11.500.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:daily:7d:no` used a sample size of 1 markets across 1 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 1 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:daily:7d:yes` used a sample size of 1 markets across 1 event clusters.
Estimate: -1.000. 95% confidence interval: not available to not available. Observed range: -1.000 to -1.000.
Not tested: only 1 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:monthly:7d:no` used a sample size of 189 markets across 33 event clusters.
Estimate: -0.474. 95% confidence interval: -0.682 to -0.266. Observed range: -1.000 to 2.333.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:monthly:7d:yes` used a sample size of 217 markets across 33 event clusters.
Estimate: -0.213. 95% confidence interval: -0.679 to 0.252. Observed range: -1.000 to 24.000.
Raw p-value: 0.369; multiple-testing adjusted q-value: 0.506.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:7d:no` used a sample size of 2660 markets across 313 event clusters.
Estimate: -0.036. 95% confidence interval: -0.105 to 0.034. Observed range: -1.000 to 19.000.
Raw p-value: 0.317; multiple-testing adjusted q-value: 0.449.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:one_off:7d:yes` used a sample size of 2909 markets across 335 event clusters.
Estimate: -0.380. 95% confidence interval: -0.435 to -0.325. Observed range: -1.000 to 15.667.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:weekly:7d:no` used a sample size of 15 markets across 4 event clusters.
Estimate: -0.531. 95% confidence interval: not available to not available. Observed range: -1.000 to 0.020.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:frequency:weekly:7d:yes` used a sample size of 14 markets across 4 event clusters.
Estimate: 1.570. 95% confidence interval: not available to not available. Observed range: -1.000 to 11.500.
Not tested: only 4 independent events (needs 30).

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:7d:7d:no` used a sample size of 4133 markets across 565 event clusters.
Estimate: -0.065. 95% confidence interval: -0.121 to -0.010. Observed range: -1.000 to 19.000.
Raw p-value: 0.020; multiple-testing adjusted q-value: 0.033.

### Segmented — candidate (discovery only)

Hypothesis `segmented:time_to_close:7d:7d:yes` used a sample size of 4733 markets across 635 event clusters.
Estimate: -0.387. 95% confidence interval: -0.435 to -0.338. Observed range: -1.000 to 24.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.

### Listing drift — candidate (discovery only)

Hypothesis `listing_drift:brier_1h_vs_24h` used a sample size of 22560 markets across 1988 event clusters.
Estimate: 0.109. 95% confidence interval: 0.093 to 0.125. Observed range: -0.998 to 1.000.
Raw p-value: 0.000; multiple-testing adjusted q-value: 0.000.
