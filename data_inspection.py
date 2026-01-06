import pandas as pd
file_path = "data/raw/superstore.csv"
df = pd.read_csv(file_path)


# Step 1: Data Inspection
df.head()
df.columns
print(df.dtypes)
df.info()
print(df.describe())


# Step 2: Data Quality Assessment
print("\n Missing values per column:")
print(df.isnull().sum())

print("\n Number of duplicate rows:")
print(df.duplicated().sum())

print("\n Null values in Sales and Profit:")
print(df[['Sales', 'Profit']].isnull().sum())

print("\n Invalid Quantity values:")
print(df[df['Quantity']<=0])

print("\n Order Date data type:", df['Order Date'].dtype)
print("Ship Date data type:", df['Ship Date'].dtype)

print("\n Unique Segments:")
print(df['Segment'].unique())

print("\n Unique Ship Modes:")
print(df['Ship Mode'].unique())


# Step 3: Data Cleaning & Transformation
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

print(df[['Order Date', 'Ship Date']].dtypes)  # double square brackets used bcz we want to multiple columns


 # postal code has high no of missing values
 # It will be retained in raw data but excluded from KPI analysis

# create derived date columns
df['order_year'] = df['Order Date'].dt.year
df['order_month'] = df['Order Date'].dt.month
df['order_month_name'] = df['Order Date'].dt.month_name()

# validate numeric columns
df[['Sales', 'Profit', 'Quantity', 'Discount']] = df[['Sales', 'Profit', 'Quantity', 'Discount']].apply(pd.to_numeric)

# checking if the numeric columns are in numeric n new columns are created or not
print(df[['Sales', 'Profit', 'Quantity', 'Discount']].dtypes)
print(df[['order_year', 'order_month', 'order_month_name']].head())

# save cleaned data
df.to_csv("data/processed/superstore_cleaned.csv", index=False)
print("Cleaned data saved successfully")