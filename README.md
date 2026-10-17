# Logistics Shipment Analytics

## Project Overview
This project analyzes logistics and shipment data to understand delivery performance, transportation costs, shipment status, and regional operations. It uses Python for data cleaning and analysis, SQL for business queries, and Power BI for interactive visualization.

The goal is to turn raw shipment data into meaningful business insights that can help improve logistics efficiency and support data-driven decision-making.

## Objectives
- Clean and prepare raw shipment data for analysis.
- Identify missing values, duplicate records, and potential data-quality issues.
- Analyze shipment volume, delivery performance, and transportation costs.
- Compare logistics performance across regions and shipment statuses.
- Build an interactive Power BI dashboard to present key performance indicators (KPIs).

## Tools and Technologies
- **Python:** Data cleaning, analysis, and automation.
- **Pandas:** Data manipulation and descriptive statistics.
- **NumPy:** Numerical analysis and outlier investigation.
- **SciPy:** Statistical analysis.
- **Matplotlib:** Data visualization.
- **SQL / SQLite:** Data querying and business analysis.
- **Power BI:** Dashboard development and DAX measures.
- **Excel / CSV:** Data storage and inspection.

## Dataset Description
The project uses logistics shipment records containing fields such as:

- Shipment ID and customer information
- Order, shipping, and delivery dates
- Origin and destination cities
- Region, carrier, and transport mode
- Product category, quantity, weight, and distance
- Shipping cost and fuel surcharge
- Delivery status and customer rating

**Data privacy:** Use an anonymized or synthetic dataset when sharing this project publicly. Do not publish personal contact information or confidential business records.

## Project Workflow

### 1. Data Inspection
- Loaded the raw dataset using Python.
- Examined column names, data types, missing values, and duplicate records.
- Generated an initial data-quality profile.

### 2. Data Cleaning
- Removed duplicate records and handled data-quality issues.
- Prepared the dataset for downstream analysis.
- Created derived fields such as dispatch days, delivery days, and total transport cost.

### 3. Exploratory Data Analysis
- Used Pandas and NumPy for numerical summaries.
- Investigated shipping costs, shipment patterns, and potential outliers.
- Created charts to explore shipment status, regional costs, and shipping-cost distribution.

### 4. SQL Analysis
- Queried the final dataset stored in SQLite.
- Practiced aggregations, filtering, sorting, grouping, and business KPI calculations.
- Analyzed shipment and transportation metrics to answer operational questions.

### 5. Power BI Dashboard
- Developed an interactive dashboard using the final dataset.
- Created KPI cards and visualizations for shipment and transportation analysis.
- Used DAX measures to calculate key metrics.

## Key Performance Indicators
The dashboard focuses on metrics such as:

- Total Shipments
- Total Transport Cost
- Average Shipping Cost
- Delivery Performance
- Shipment Status Distribution
- Regional Transportation Costs

*Final KPI values should be added after validating the published dashboard against the final dataset.*

## Business Questions
1. How many shipments were processed?
2. What is the total transportation cost?
3. Which regions have higher shipping costs?
4. How are shipments distributed by delivery status?
5. What patterns can be observed in shipping costs?
6. How can shipment and delivery performance be monitored?

## Project Structure

```text
Logistics-Shipment-Analytics/
├── PYTHON/
│   ├── 01_load_inspect.py
│   ├── 02_clean_data.py
│   ├── 03_numpy_analysis.py
│   ├── 04_pandas_analysis.py
│   ├── 05_eda.py
│   └── 06_business_insights.py
├── SQL/
│   └── SQL_Queries.sql
├── OUTPUT/
│   ├── Logistics_Cleaned_Data.csv
│   ├── Logistics_Final_Data.csv
│   └── Charts and analysis reports
├── PowerBI/
│   └── Logistics_Shipment_Analytics.pbix
└── README.md
```

*Adjust the folder and filenames above to match the files actually present in your project.*

## Skills Demonstrated
- Data cleaning and validation
- Exploratory data analysis
- Python programming
- SQL querying and aggregation
- Statistical analysis and outlier detection
- KPI development
- Power BI dashboards and DAX
- Business-oriented analytical thinking

## Conclusion
This project demonstrates an end-to-end logistics analytics workflow, from raw data inspection and cleaning to SQL analysis and Power BI reporting. It showcases practical data analysis skills and the ability to communicate operational metrics through visualizations.

## Author
**Ketan Mhamunkar**

Aspiring Data Analyst | MIS / Reporting Analyst

**Tools:** Python | SQL | Power BI | Excel

