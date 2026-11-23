import pandas as pd

df = pd.read_csv("cleaned_sales_data.csv")

# Create Sales column if not already present
df["Sales"] = df["Quantity"] * df["Price"]

# KPI 1
total_sales = df["Sales"].sum()

# KPI 2
avg_sales = df["Sales"].mean()

# KPI 3
total_orders = df["Order_ID"].nunique()

# KPI 4
total_customers = df["Customer"].nunique()

# KPI 5
best_product = (
    df.groupby("Product")["Sales"]
      .sum()
      .idxmax()
)

# KPI 6
best_region = (
    df.groupby("Region")["Sales"]
      .sum()
      .idxmax()
)

print("\n======= KPI REPORT =======")

print("Total Sales:", total_sales)
print("Average Sales:", round(avg_sales,2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Best Selling Product:", best_product)
print("Best Performing Region:", best_region)