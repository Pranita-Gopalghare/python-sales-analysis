import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n", region_sales)

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:\n", category_sales)

# Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nMonthly Sales:\n", monthly_sales)
