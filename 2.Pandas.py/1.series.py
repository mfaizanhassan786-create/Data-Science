import pandas as pd

## Creating a Series:

# s = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])

# # print(s)

# # Index vs values

# print("Values:", s.values)
# print("Index:", s.index)
# print("Data Type:", s.dtype)

# print(s.head)
# print(s.tail)
# print(s.value_counts())

## Another Example:

# # Creating a Series from a dictionary (e.g., student scores)
# scores = {
#     'Math': 95,
#     'Science': 88,
#     'English': 92,
#     'History': 85
# }

# s2 = pd.Series(scores, name="Student_Scores")

# print("Series from Dictionary:\n", s2)
# print("\nAccess by label ('Math'):", s2['Math'])
# print("Mean score:", s2.mean())
# print("Scores greater than 90:\n", s2[s2 > 90])

## Example 3: Handling Missing Data & Operations (e.g., Daily Store Sales)

# sales_data = [120, 250, None, 180, 310]
# days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# sales = pd.Series(sales_data, index=days, name="Weekly_Sales")

# print("\nOriginal Sales Series:\n", sales)
# print("\nCheck for null values:\n", sales.isnull())
# print("\nFill missing value with average:\n", sales.fillna(sales.mean()))
# print("\nTotal Sales (ignoring NaN):", sales.sum())
# print("\nSorted by values descending:\n", sales.sort_values(ascending=False))
