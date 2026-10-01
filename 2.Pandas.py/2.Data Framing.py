import os
import pandas as pd

# # data = {
# #     "Name": ["faizan" , "Faizan", "Ali", "Hassan"],
# #     "Age": [23, 24, 25, 27],
# #     "City": ["Karachi", "Lahore", "Islamabad", "Multan"]
# # }

# # df = pd.DataFrame(data)

# # print(df)


# # # Load sample CSV file

# df = pd.read_csv('2.Pandas.py/3.Retail_sales.csv')


# # # Inspect Data Frame
# print('Info : \n', df.info())

# print('Shape : \n', df.shape)
# print("Head : \n" , df.head(5))
# print("Describe : \n", df.describe())
# print("\nData Typess:\n" , df.dtypes)
# print("\nStatistical Summary:\n" , df.describe())
# print("\nNumber of rows and columns : \n" , (df.shape))


# # Example: Creating DataFrame from a list of dictionaries & adding calculated columns:

# employee_data = [
#     {"EmpID": 101, "Name": "Ayesha", "Department": "HR", "Salary": 60000},
#     {"EmpID": 102, "Name": "Bilal", "Department": "IT", "Salary": 85000},
#     {"EmpID": 103, "Name": "Hamza", "Department": "Finance", "Salary": 75000},
#     {"EmpID": 104, "Name": "Zainab", "Department": "IT", "Salary": 92000},
# ]

# df_emp = pd.DataFrame(employee_data)

# # Adding derived/calculated columns
# df_emp["Bonus"] = df_emp["Salary"] * 0.10
# df_emp["Total_Comp"] = df_emp["Salary"] + df_emp["Bonus"]

# print("--- Employee DataFrame ---")
# print(df_emp)

# print("\n--- Filter (IT Department) ---")
# print(df_emp[df_emp["Department"] == "IT"])


# # Example: Creating DataFrame with Custom Index & Accessing with loc / iloc:

# scores_data = {
#     "Math": [85, 92, 78, 90],
#     "Science": [88, 95, 72, 89],
#     "English": [79, 85, 88, 91]
# }
# students = ["Alice", "Bob", "Charlie", "David"]

# df_scores = pd.DataFrame(scores_data, index=students)

# print("\n--- Student Scores (Custom Index) ---")
# print(df_scores)

# print("\n--- Access by label using .loc['Bob'] ---")
# print(df_scores.loc["Bob"])

# print("\n--- Access by integer position using .iloc[0:2] ---")
# print(df_scores.iloc[0:2])


# # Example: GroupBy and Aggregation:

# sales_data = {
#     "Region": ["North", "South", "North", "West", "South", "West"],
#     "Salesperson": ["Ali", "Sara", "Faizan", "Amna", "Bilal", "Arslan"],
#     "Sales": [25000, 34000, 18000, 42000, 29000, 31000],
#     "Units": [50, 70, 35, 90, 60, 65]
# }

# df_sales = pd.DataFrame(sales_data)

# print("\n--- Sales DataFrame ---")
# print(df_sales)

# # Group by Region with summary statistics
# print("\n--- Total & Average Sales by Region ---")
# print(df_sales.groupby("Region")[["Sales", "Units"]].agg(["sum", "mean"]))


# # Example: Handling Missing Data (NaN values) & Dropping/Imputing:

# import numpy as np

# raw_data = {
#     "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
#     "Price": [1200, 25, np.nan, 300, 80],
#     "Stock": [15, np.nan, 50, 20, np.nan]
# }

# df_inventory = pd.DataFrame(raw_data)

# print("\n--- Inventory with Missing Values ---")
# print(df_inventory)

# print("\n--- Missing Value Count ---")
# print(df_inventory.isnull().sum())

# # Fill missing Price with median and Stock with 0
# df_inventory_filled = df_inventory.copy()
# df_inventory_filled["Price"] = df_inventory_filled["Price"].fillna(df_inventory_filled["Price"].median())
# df_inventory_filled["Stock"] = df_inventory_filled["Stock"].fillna(0)

# print("\n--- Cleaned Inventory DataFrame ---")
# print(df_inventory_filled)


# # Example: Merging and Joining DataFrames (e.g., Customers & Orders):

# customers = pd.DataFrame({
#     "CustomerID": [1, 2, 3, 4],
#     "CustomerName": ["Faizan", "Ayesha", "Bilal", "Zainab"],
#     "City": ["Karachi", "Lahore", "Islamabad", "Peshawar"]
# })

# orders = pd.DataFrame({
#     "OrderID": [501, 502, 503, 504, 505],
#     "CustomerID": [1, 2, 1, 3, 5],  # Customer 5 has no profile, Customer 4 has no order
#     "Amount": [1200, 450, 800, 2300, 150]
# })

# print("\n--- Inner Merge (matching customers & orders) ---")
# df_inner = pd.merge(customers, orders, on="CustomerID", how="inner")
# print(df_inner)

# print("\n--- Left Merge (all customers with orders if any) ---")
# df_left = pd.merge(customers, orders, on="CustomerID", how="left")
# print(df_left)


# # Example: Pivot Table & Cross-Tabulation (e.g., Store Sales by Category & Region):

# store_sales = pd.DataFrame({
#     "Region": ["East", "West", "East", "West", "East", "West", "East"],
#     "Category": ["Electronics", "Electronics", "Clothing", "Clothing", "Electronics", "Clothing", "Electronics"],
#     "Quarter": ["Q1", "Q1", "Q1", "Q1", "Q2", "Q2", "Q2"],
#     "Revenue": [5000, 7000, 3000, 4000, 6200, 4500, 5800]
# })

# print("\n--- Pivot Table (Average & Total Revenue by Region and Category) ---")
# pivot_revenue = store_sales.pivot_table(
#     values="Revenue",
#     index="Region",
#     columns="Category",
#     aggfunc="sum",
#     fill_value=0
# )
# print(pivot_revenue)


# # Example: Sorting, Ranking & Filtering with .query():

# print("\n--- Top 3 Highest Revenue Records ---")
# top_sales = store_sales.sort_values(by="Revenue", ascending=False).head(3)
# print(top_sales)

# print("\n--- Query: Electronics with Revenue > 5500 ---")
# electronics_high = store_sales.query("Category == 'Electronics' and Revenue > 5500")
# print(electronics_high)


