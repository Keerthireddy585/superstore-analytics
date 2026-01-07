# Global Superstore Sales Analytics Project

## Project Overview
This project presents an end-to-end sales analytics solution built using the Global Superstore dataset.  
The objective is to analyze business performance across revenue, growth, products, regions, and customers, and to translate data findings into clear, actionable business insights.

The project emphasizes not only data analysis and visualization, but also structured business storytelling, KPI-driven decision-making, and readiness for real-world analytics workflows through basic automation and scalability considerations. 


## Data Source:
The analysis is based on the Global Superstore dataset, a commonly used retail dataset containing order-level sales, customer, product, and regional information


## Business Questions Addressed
How is the business performing overall, and are we growing?
What are the key revenue and growth trends over time?
Which product categories and products drive the most revenue?
Which regions require attention based on revenue performance?
Who are the most valuable customers, and how concentrated is revenue?


## Project Components

### 1. Data Inspection & Preparation
  - Initial data inspection to understand structure, data types, and completeness
  - Validation checks for key fields such as dates, revenue, and order identifiers 
  - Preparation of clean, analysis-ready datasets

### 2. Data Modeling
  - Fact and dimension-style data organization
  - Calendar table creation for time-based analysis
  - Measures and KPIs designed to support business reporting and trend analysis

### 3. Dashboard & Visualization
Interactive Power BI dashboard with the following sections:
  - Executive Summary
  - Revenue & Growth
  - Product Performance
  - Regional Performance
  - Customer Insights
Use of slicers (date, category, region) to support exploratory analysis
Insight-driven KPIs rather than purely descriptive visuals

### 4. Business Insights Documentation
Key business insights and recommendations are documented separately using a structured framework:
  - What happened
  - Why it happened
  - What the business should do

See detailed insights in: [business_insights.md](business_insights.md)


## Automation & Scalability

This project includes a simulated automation pipeline to demonstrate how the analytics workflow can be scaled and operationalized in a real business environment.

Note:
The automation script is a conceptual demonstration intended to show how this analysis could be operationalized in a production environment. 
It does not rely on scheduling tools (e.g., Airflow) but reflects end-to-end workflow thinking.


### Simulated Automation Pipeline
A script named:

```text
run_pipeline.py
```


## How to Run the Project 

1. Clone the repository
2. Ensure Python is installed
3. Run individual analysis scripts as needed:
   - data_inspection.py
   - eda_analysis.py
   - kpi_design.py
4. To simulate the full pipeline:
   python run_pipeline.py


## Tools & Technologies Used

- Python (Pandas, NumPy)
- Power BI
- Git & GitHub
- CSV-based datasets
- Markdown for documentation
