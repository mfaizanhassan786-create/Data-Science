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
