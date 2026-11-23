import pandas as pd

df = pd.read_csv("cleaned_sales_data.csv")


#4 . Find missing values

print(df.isna().sum())

#5. Find duplicate rows

print(df.duplicated().sum())

