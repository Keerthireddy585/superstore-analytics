# load modeled data
import pandas as pd

fact_sales = pd.read_csv("data/models/fact_sales.csv")
dim_products = pd.read_csv("data/models/dim_products.csv")
dim_customers = pd.read_csv("data/models/dim_customers.csv")
dim_location = pd.read_csv("data/models/dim_location.csv")

print(fact_sales.head())


# basic business overview
# 1. Total revenue & profit
total_sales = fact_sales['Sales'].sum()
total_profit = fact_sales['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# Sales trend over time
fact_sales['Order Date'] = pd.to_datetime(fact_sales['Order Date'])

monthly_sales = fact_sales.groupby(fact_sales['Order Date'].dt.to_period('M'))['Sales'].sum()

print(monthly_sales.head())

# top products by sales
product_sales = fact_sales.merge(
    dim_products, on='Product ID'
).groupby('Category')['Sales'].sum().sort_values(ascending=False)

print(product_sales)

# Regional Performance
regional_sales = (
    fact_sales
    .merge(dim_location, on='Location_ID')
    .groupby('Region')['Sales']
    .sum()
    .sort_values(ascending=False)
)

print(regional_sales)

# Customer segmentation impact
customer_sales = fact_sales.merge(
    dim_customers, on='Customer ID'
).groupby('Segment')['Sales'].sum()

print(customer_sales)