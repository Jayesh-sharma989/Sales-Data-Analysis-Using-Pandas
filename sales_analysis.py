import pandas as pd

data = {
    "Order_ID": [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116],
    "Customer": ["Amit","Riya","Rahul","Neha","Aman","Priya","Rohit","Pooja","Karan","Simran","Sonia","Amit","Vikas","Pooja","Rahul","Sonia"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Mumbai","Delhi","Pune","Mumbai","Delhi","Pune","Rewari","Delhi","Gurgaon","Rewari","Delhi","Gurgaon"],
    "Category": ["Electronics","Clothing","Electronics","Furniture","Clothing",
                "Electronics","Furniture","Clothing","Furniture","Electronics","Grocery","Clothing",
              "Electronics","Grocery","Clothing","Electronics"],
    "Quantity": [2,5,3,1,4,2,1,6,1,3,4,5,1,3,2,2],
    "Price": [1500,60,800,12000,150,1200,55000,55,2500,1800,60,450,25000,150,800,1500],
    "Date": ["2026-01-05","2026-01-10","2026-02-15","2026-02-20",
             "2026-03-01","2026-03-08","2026-04-12","2026-04-18",
             "2026-05-10","2026-05-25","2026-03-05","2026-03-09",
           "2026-03-13","2026-03-17","2026-03-21","2026-03-25"],
  "Region" : ["North","North","South","North","North","South","North","South",
               "North","North","South","North","North","South","North","North"],
 "Product" : ["Mixer","Rice Bag","Shirt","Mobile","Oil Can","Jeans","Laptop","Wheat Bag",
             "Jacket","Earbuds","Rice Bag","T-Shirt","Tablet","Oil Can","Shirt","Mixer"]   
}

df = pd.DataFrame(data)

print(df)

#1Task 1 - Display First 5 Rows

print(df.head())

df["Sales"] = df["Quantity"] * df["Price"]

print(df)

print(2)

#2 check dataset shape

print(df.shape)

print(3)
#3 check data type

print(df.dtypes)

print(4)

#4 . Find missing values

print(df.isna().sum())

print(5)

#5. Find duplicate rows

print(df.duplicated().sum())

print(6)

#6.calculate total sales

print("total sales",df["Sales"].sum()) #116470
print(7)

#7.Calculate average sales

print("average sales",df["Sales"].mean()) #7279.375

print(8)

#8.Find highest sales

print("highest sales",df["Sales"].max())
print(9)

#9.Find lowest sales

print("lowest sales",df["Sales"].min())
print(10)

#10.Find total quantity sold

print("total quantity sold",df["Quantity"].sum())
print(11)

#11.Find sales by city

sales_by_city = df.groupby('City')['Sales'].sum()
print(sales_by_city)

print(12)

#12. Find sales by category

sales_by_category = df.groupby("Category")["Sales"].sum()
print(sales_by_category)
print(13)

#13.Average sales by category

average_sales_by_cat = df.groupby("Category")["Sales"].mean()
print(average_sales_by_cat)
print(14)

#14.Find top 5 orders

top_5 = df.sort_values("Sales",ascending=False).head(5)
print(top_5)
print(15)

#15. Filter sales above ₹5,000

high_value = df[df["Sales"]>5000]
print(high_value)
print(16)

#16.Find unique cities

print(df["City"].unique())
print(17)

#17.Count orders by category

print(df["Category"].value_counts())
print(18)


# 18. Convert Date to datetime

df['Date'] = pd.to_datetime(df['Date'])

print(df['Date'])
print(19)

#19. Extract month

df["Month"] = df["Date"].dt.month 
print(df[["Month","Date"]])
print(20)

#20.Calculate monthly sales

monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

#21.TOP CUSTOMERS

top_customers = df.groupby("Customer")["Sales"].sum()\
.sort_values(ascending=False)

print(top_customers)




                              #PIVOT Table 
                        
print("PIVOT_TABLE")
                            
pivot = pd.pivot_table(df,values="Sales",index="City",columns="Category",aggfunc="sum")   
print(pivot)                          
                     

df.to_csv("cleaned_sales_data.csv",index=False)

print("CSV FILE EXPORTED SUCCESSFULLY")

df2 = df.copy
print(df2)