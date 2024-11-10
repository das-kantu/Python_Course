# Example 35: Pandas - Using at and iat for Fast Scalar Access
import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# accessing a single value using at and iat:

value_at = df.at[1, 'A']
value_iat = df.iat[1, 0]

print('Value Using At:\n', value_at)
print('Value Using IAT:\n', value_iat)