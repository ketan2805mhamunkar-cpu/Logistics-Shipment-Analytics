
# 05_scipy_analysis.py
# Logistics Shipment Analytics - SciPy

import pandas as pd
from scipy import stats
from pathlib import Path

# Load data
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "OUTPUT" / "Logistics_Final_Data.csv"
output_folder = project_folder / "OUTPUT"

df = pd.read_csv(file_path)

# Select shipping cost
cost = pd.to_numeric(
    df["Shipping_Cost_INR"], errors="coerce"
).dropna()

print("=" * 40)
print("SCIPY STATISTICAL ANALYSIS")
print("=" * 40)

# Basic statistics
print("\nShipping Cost Statistics")
print("Mean:", round(cost.mean(), 2))
print("Median:", round(cost.median(), 2))

# Calculate IQR
q1 = cost.quantile(0.25)
q3 = cost.quantile(0.75)
iqr = stats.iqr(cost)

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

# Identify potential outliers
outliers = cost[
    (cost < lower_limit) | (cost > upper_limit)
]

print("\nIQR Analysis")
print("Q1:", round(q1, 2))
print("Q3:", round(q3, 2))
print("IQR:", round(iqr, 2))
print("Lower Limit:", round(lower_limit, 2))
print("Upper Limit:", round(upper_limit, 2))
print("Potential Outliers:", len(outliers))

# Run a normality test on a sample if sufficient data exists
sample = cost.sample(
    n=min(len(cost), 5000),
    random_state=42
)

if len(sample) >= 8:
    statistic, p_value = stats.normaltest(sample)

    print("\nNormality Test")
    print("Test Statistic:", round(statistic, 4))
    print("P-value:", round(p_value, 6))

    if p_value < 0.05:
        print("Result: Evidence that the sample is not normally distributed.")
    else:
        print("Result: Insufficient evidence to reject normality.")

# Save outliers for review
outliers.to_frame(name="Shipping_Cost_INR").to_csv(
    output_folder / "SciPy_Potential_Outliers.csv",
    index=False
)

print("\nSciPy analysis completed!")
print("Potential outliers saved for review.")
