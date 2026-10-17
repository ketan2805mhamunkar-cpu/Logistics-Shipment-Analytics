
# 02_clean_data.py
# Logistics Shipment Analytics

import pandas as pd
from pathlib import Path

# 1. Set file paths
project_folder = Path(__file__).resolve().parent.parent

input_file = project_folder / "OUTPUT" / "Logistics_Cleaned_Data.csv"
output_folder = project_folder / "OUTPUT"
output_file = output_folder / "Logistics_Final_Data.csv"

# 2. Load data
df = pd.read_csv(input_file)

print("Original rows:", len(df))

# 3. Remove exact duplicate rows
df = df.drop_duplicates()

print("Rows after removing duplicates:", len(df))

# 4. Convert date columns
date_columns = [
    "Order_Date",
    "Ship_Date",
    "Delivery_Date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        errors="coerce"
    )

# 5. Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# 6. Check suspicious numerical values
print("\nSuspicious numerical values:")

print(
    "Quantity greater than 1000:",
    (df["Quantity"] > 1000).sum()
)

print(
    "Weight greater than 10000 kg:",
    (df["Weight_kg"] > 10000).sum()
)

print(
    "Distance greater than 10000 km:",
    (df["Distance_km"] > 10000).sum()
)

print(
    "Delivery days greater than 60:",
    (df["Delivery_Days"] > 60).sum()
)

# 7. Check missing values after date conversion
print("\nMissing values after date conversion:")
print(df.isnull().sum())

# 8. Save dataset
df.to_csv(output_file, index=False)

print("\nCleaning checks completed!")
print("Final rows:", len(df))
print("Final columns:", len(df.columns))
print("Saved file:", output_file)
