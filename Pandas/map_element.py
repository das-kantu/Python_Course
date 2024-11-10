
# Example 21: Pandas - Using applymap for Element-wise Operations
import pandas as pd

# creating a dataframe:
data = {'A': [1, 2, 3],
        'B': [4, 5, 6]
        }
df = pd.DataFrame(data)
# print(df)

# applying an operation to each element in the DataFrame:

df_transformed = df.applymap(lambda x : x ** 2)

print('Data Framed With Squared Values: \n',df_transformed)