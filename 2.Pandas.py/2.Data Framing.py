# import os
# import pandas as pd

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


# Example: Creating DataFrame from a list of dictionaries & adding calculated columns
import pandas as pd

employee_data = [
    {"EmpID": 101, "Name": "Ayesha", "Department": "HR", "Salary": 60000},
    {"EmpID": 102, "Name": "Bilal", "Department": "IT", "Salary": 85000},
    {"EmpID": 103, "Name": "Hamza", "Department": "Finance", "Salary": 75000},
    {"EmpID": 104, "Name": "Zainab", "Department": "IT", "Salary": 92000},
]

df_emp = pd.DataFrame(employee_data)

# Adding derived/calculated columns
df_emp["Bonus"] = df_emp["Salary"] * 0.10
df_emp["Total_Comp"] = df_emp["Salary"] + df_emp["Bonus"]

print("--- Employee DataFrame ---")
print(df_emp)

print("\n--- Filter (IT Department) ---")
print(df_emp[df_emp["Department"] == "IT"])
