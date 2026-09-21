import os
import pandas as pd

# data = {
#     "Name": ["faizan" , "Faizan", "Ali", "Hassan"],
#     "Age": [23, 24, 25, 27],
#     "City": ["Karachi", "Lahore", "Islamabad", "Multan"]
# }

# df = pd.DataFrame(data)

# print(df)


# # Load sample CSV file

df = pd.read_csv('2.Pandas.py/3.retail_sales.csv')


# # Inspect Data Frame
# print('Info : \n', df.info())

# print('Shape : \n', df.shape)
# print("Head : \n" , df.head(5))
# print("Describe : \n", df.describe())
# print("\nData Typess:\n" , df.dtypes)
# print("\nStatistical Summary:\n" , df.describe())
# print("\nNumber of rows and columns : \n" , (df.shape))
