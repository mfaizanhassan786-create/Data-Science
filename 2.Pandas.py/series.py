import pandas as pd

## Creating a Series:

s = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])

print(s)

#Index vs values

print("Values:", s.values)
print("Index:", s.index)
print("Data Type:", s.dtype)

print(s.head)
print(s.tail)



