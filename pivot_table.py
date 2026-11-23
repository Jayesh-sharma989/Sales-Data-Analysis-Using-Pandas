#A Pivot Table summarizes data by categories and helps compare business performance.

import pandas as pd


df=pd.read_csv("cleaned_sales_data.csv")



# Pivot 1: City-wise category sales

city_pivot = pd.pivot_table(
    df,
    values="Sales",
    index="City",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print(city_pivot)


#Pivot 2: Monthly sales


monthly_pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Month",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print(monthly_pivot)


#Pivot 3: Customer-wise sales

customer_pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Customer",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print(customer_pivot)


#Pivot 4: Product-wise quantity


product_pivot = pd.pivot_table(
    df,
    values="Quantity",
    index="Product",
    aggfunc="sum",
    fill_value=0
)

print(product_pivot)


#Pivot 5: Region-wise sales

region_pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc="sum",
    fill_value=0
)

print(region_pivot)

#Pivot 6: Category-wise quantity

category_pivot = pd.pivot_table(
    df,
    values="Quantity",
    index="Category",
    aggfunc="sum",
    fill_value=0
)

print(category_pivot)