
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "OUTPUT" / "Logistics_Final_Data.csv"
output_folder = project_folder / "OUTPUT"

df = pd.read_csv(file_path)

# Chart 1: Shipping cost by region
region_cost = df.groupby("Region")["Shipping_Cost_INR"].sum()

region_cost.plot(kind="bar", title="Shipping Cost by Region")
plt.ylabel("Shipping Cost (INR)")
plt.tight_layout()
plt.savefig(output_folder / "Shipping_Cost_by_Region.png")
plt.show()
plt.close()

# Chart 2: Shipping cost distribution
df["Shipping_Cost_INR"].dropna().plot(
    kind="hist", bins=30, title="Shipping Cost Distribution"
)
plt.xlabel("Shipping Cost (INR)")
plt.tight_layout()
plt.savefig(output_folder / "Shipping_Cost_Distribution.png")
plt.show()
plt.close()

# Chart 3: Shipment status
df["Delivery_Status"].value_counts().plot(
    kind="bar", title="Shipments by Delivery Status"
)
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.savefig(output_folder / "Shipments_by_Status.png")
plt.show()
plt.close()

print("All three charts created successfully!")
