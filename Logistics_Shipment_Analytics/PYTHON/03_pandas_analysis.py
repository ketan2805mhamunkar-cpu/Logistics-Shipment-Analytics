
# 03_pandas_analysis.py
# Logistics Shipment Analytics

import pandas as pd
from pathlib import Path

# 1. Load cleaned data
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "OUTPUT" / "Logistics_Final_Data.csv"

df = pd.read_csv(file_path)

# 2. Calculate business KPIs
total_shipments = len(df)

total_shipping_cost = df["Shipping_Cost_INR"].sum()
average_shipping_cost = df["Shipping_Cost_INR"].mean()

average_delivery_days = df["Delivery_Days"].mean()

total_transport_cost = df["Total_Transport_Cost_INR"].sum()

delivered_shipments = (
    df["Delivery_Status"].astype(str).str.strip().str.lower()
    == "delivered"
).sum()

delayed_shipments = (
    df["Delivery_Days"] > 7
).sum()

# 3. Display results
print("=" * 45)
print("LOGISTICS BUSINESS KPI REPORT")
print("=" * 45)

print("Total Shipments:", total_shipments)
print("Total Shipping Cost (INR):", round(total_shipping_cost, 2))
print("Average Shipping Cost (INR):", round(average_shipping_cost, 2))
print("Average Delivery Days:", round(average_delivery_days, 2))
print("Total Transport Cost (INR):", round(total_transport_cost, 2))
print("Delivered Shipments:", int(delivered_shipments))
print("Shipments Taking More Than 7 Days:", int(delayed_shipments))

# 4. Region-wise analysis
print("\nREGION-WISE SHIPMENT COUNT")

region_analysis = df.groupby("Region").size()

print(region_analysis)

# 5. Carrier-wise analysis
print("\nCARRIER-WISE SHIPMENT COUNT")

carrier_analysis = df.groupby("Carrier").size()

print(carrier_analysis)

# 6. Delivery status analysis
print("\nDELIVERY STATUS ANALYSIS")

status_analysis = df["Delivery_Status"].value_counts()

print(status_analysis)

# 7. Save KPI results
kpis = pd.DataFrame({
    "KPI": [
        "Total Shipments",
        "Total Shipping Cost INR",
        "Average Shipping Cost INR",
        "Average Delivery Days",
        "Total Transport Cost INR",
        "Delivered Shipments",
        "Shipments Taking More Than 7 Days"
    ],
    "Value": [
        total_shipments,
        round(total_shipping_cost, 2),
        round(average_shipping_cost, 2),
        round(average_delivery_days, 2),
        round(total_transport_cost, 2),
        int(delivered_shipments),
        int(delayed_shipments)
    ]
})

output_file = project_folder / "OUTPUT" / "Business_KPIs.csv"
kpis.to_csv(output_file, index=False)

print("\nKPI report saved to:", output_file)
print("\nAnalysis completed successfully!")
