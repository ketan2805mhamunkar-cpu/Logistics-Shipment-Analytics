
# 01_load_inspect.py
# Logistics Shipment Analytics

import pandas as pd
from pathlib import Path

# Main project folder
project_folder = Path(__file__).resolve().parent.parent

# Load existing cleaned dataset
file_path = project_folder / "OUTPUT" / "Logistics_Cleaned_Data.csv"

df = pd.read_csv(file_path)

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET SIZE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- BASIC STATISTICS ---")
print(df.describe().round(2))

print("\nData loaded successfully!")
