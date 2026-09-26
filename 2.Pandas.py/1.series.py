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

## Example 4: String Operations & Custom Transformations (e.g., Product Inventory)

# products = pd.Series(['  Laptop ', 'smartPHONE', 'TABLET', 'HeAdPhOnEs', 'smartwatch'], name="Gadgets")

# print("\nOriginal Series:\n", products)
# print("\nCleaned & Uppercase:\n", products.str.strip().str.upper())
# print("\nCheck containing 'smart':\n", products.str.strip().str.lower().str.contains('smart'))

# # Using .apply() with a custom function or lambda
# print("\nCharacter counts:\n", products.str.strip().apply(len))

# # Example 5: Time Series & Cumulative Operations (e.g., Daily Website Visitors)

# dates = pd.date_range(start="2026-01-01", periods=6, freq="D")
# visitors = pd.Series([150, 200, 250, 220, 300, 450], index=dates, name="Website_Visitors")

# print("\nTime Series Data:\n", visitors)
# print("\nCumulative Visitors (cumsum):\n", visitors.cumsum())
# print("\n3-Day Rolling Average:\n", visitors.rolling(window=3).mean())
# print("\nDay with Maximum Visitors:", visitors.idxmax(), "with", visitors.max(), "visitors")

## Example 6: Categorical Mapping, Ranking & Conditions (e.g., Employee Performance)

# ratings = pd.Series(['Good', 'Excellent', 'Average', 'Poor', 'Good', 'Excellent'], name="Performance")

# # Mapping categories to numeric scores
# grade_scale = {'Poor': 1, 'Average': 2, 'Good': 3, 'Excellent': 4}
# numeric_scores = ratings.map(grade_scale)

# print("\nCategorical Performance Ratings:\n", ratings)
# print("\nMapped to Numeric Scores:\n", numeric_scores)
# print("\nUnique Ratings:", ratings.unique())
# print("\nRating Counts (normalized):\n", ratings.value_counts(normalize=True))
# print("\nScore Ranks:\n", numeric_scores.rank(ascending=False))

