import pandas as pd

fact_sales = pd.read_csv("data/models/fact_sales.csv")
dim_products = pd.read_csv("data/models/dim_products.csv")
dim_customers = pd.read_csv("data/models/dim_customers.csv")
dim_location = pd.read_csv("data/models/dim_location.csv")

fact_sales['Order Date'] = pd.to_datetime(fact_sales['Order Date'])


# Revenue & growth KPIs
total_revenue = fact_sales['Sales'].sum()

monthly_revenue = (
    fact_sales
    .groupby(fact_sales['Order Date'].dt.to_period('M'))['Sales']
    .sum()
    .reset_index()
)

# Order & customer KPIs
total_orders = fact_sales['Order ID'].nunique()
avg_order_value = total_revenue / total_orders

# dropping these from fact_sales because the fact sales used here has category column n also the dim_product table also has category column, so when we re trying to merge both, the category column is read as category_x, category_y. 
fact_sales_clean = fact_sales.drop(
    columns=['Category', 'Sub-Category', 'Product Name'],
    errors='ignore'
)

# Product performance KPIs
product_contribution = (
    fact_sales_clean
    .merge(dim_products,
            on='Product ID')
    .groupby('Category')['Sales']
    .sum()
    .sort_values(ascending=False)
)

# # Regional Performance KPIs
regional_revenue = (
    fact_sales_clean
    .merge(dim_location, on='Location_ID')
    .groupby('Region')['Sales']
    .sum()
    .sort_values(ascending=False)
)

print(total_revenue)
print(monthly_revenue)
print(avg_order_value)
print(product_contribution)
print(regional_revenue)