import pandas as pd

df = pd.read_csv("cleaned_sales_data.csv")

print(df)

#1Task 1 - Display First 5 Rows

print(df.head())

df["Sales"] = df["Quantity"] * df["Price"]

print(df)

#2 check dataset shape

print(df.shape)

#3 check data type

print(df.dtypes)

print("First 5 Records")
print(df.head())

print("\nLast 5 Records")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInfo")
print(df.info())

print("\nDescription")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())