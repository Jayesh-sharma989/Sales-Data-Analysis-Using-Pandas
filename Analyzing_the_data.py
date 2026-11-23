import pandas as pd

df = pd.read_csv("cleaned_sales_data.csv")

#Finding Sales
df["Sales"] = df["Quantity"] * df["Price"]
print(df)

#6.calculate total sales

print("total sales",df["Sales"].sum()) #116470

#7.Calculate average sales

print("average sales",df["Sales"].mean()) #7279.375

#8.Find highest sales

print("highest sales",df["Sales"].max())

#9.Find lowest sales

print("lowest sales",df["Sales"].min())

#10.Find total quantity sold

print("total quantity sold",df["Quantity"].sum())

#11.Find sales by city

sales_by_city = df.groupby('City')['Sales'].sum()
print(sales_by_city)


#12. Find sales by category

sales_by_category = df.groupby("Category")["Sales"].sum()
print(sales_by_category)


#13.Average sales by category

average_sales_by_cat = df.groupby("Category")["Sales"].mean()
print(average_sales_by_cat)
