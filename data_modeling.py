import pandas as pd

# load the cleaned dataset
df = pd.read_csv("data/processed/superstore_cleaned.csv")

print(df.head())

# create customer dimension
dim_customers = df[[
    'Customer ID',
    'Customer Name',
    'Segment',
]].drop_duplicates()

print(dim_customers.head())


# create product dimension
dim_products = df[[                  # dim_products is a dimensional table that should describe each product once, not per order.
    'Product ID',
    'Product Name',
    'Category',
    'Sub-Category'
]].drop_duplicates()

print(dim_products.head())


# create location dimension
dim_location = df[[
    'Country',
    'Region',
    'State',
    'City'
]].drop_duplicates()

# reset index
dim_location = dim_location.reset_index(drop=True)

# create Location_ID
dim_location['Location_ID'] = dim_location.index + 1

# reorder columns
dim_location = dim_location[
    ['Location_ID', 'Country', 'Region', 'State', 'City']
]

print(dim_location.columns)


print(dim_location.head())

# create date dimension
dim_date = df[[
    'Order Date',
    'order_year',
    'order_month',
    'order_month_name'
]].drop_duplicates()

print(dim_date.head())

# create fact table
merged_df = df.merge(
    dim_location,
    on=['Country', 'Region', 'State', 'City'],
    how='left'
)

fact_sales = merged_df[
    [
        'Order ID',
        'Order Date',
        'Customer ID',
        'Product ID',
        'Location_ID',
        'Sales',
        'Profit',
        'Quantity',
        'Discount'
    ]
].copy()

print(fact_sales.head())
print(fact_sales.columns)

# save modeled tables
fact_sales.to_csv("data/models/fact_sales.csv", index=False)
dim_customers.to_csv("data/models/dim_customers.csv", index=False)
dim_products.to_csv("data/models/dim_products.csv", index=False)
dim_location.to_csv("data/models/dim_location.csv", index=False)
dim_date.to_csv("data/models/dim_date.csv", index=False)


# # create fact table
# fact_sales = df[[
#     'Order ID',
#     'Order Date',
#     'Customer ID',
#     'Product ID',
#     'Sales',
#     'Profit',
#     'Quantity',
#     'Discount'
# ]].copy()

# print(fact_sales.head())

# # create customer dimension
# dim_customers = df[[
#     'Customer ID',
#     'Customer Name',
#     'Segment',
#     'Region'
# ]].drop_duplicates()

# print(dim_customers.head())

# # create product dimension
# dim_products = df[[                  # dim_products is a dimensional table that should describe each product once, not per order.
#     'Product ID',
#     'Product Name',
#     'Category',
#     'Sub-Category'
# ]].drop_duplicates()

# print(dim_products.head())

# # create location dimension
# dim_location = df[[
#     'Country',
#     'Region',
#     'State',
#     'City'
# ]].drop_duplicates()



# print(dim_location.head())

# # create date dimension
# dim_date = df[[
#     'Order Date',
#     'order_year',
#     'order_month',
#     'order_month_name'
# ]].drop_duplicates()

# print(dim_date.head())


# # save modeled tables
# fact_sales.to_csv("data/models/fact_sales.csv", index=False)
# dim_customers.to_csv("data/models/dim_customers.csv", index=False)
# dim_products.to_csv("data/models/dim_products.csv", index=False)
# dim_location.to_csv("data/models/dim_location.csv", index=False)
# dim_date.to_csv("data/models/dim_date.csv", index=False)
