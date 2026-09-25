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
