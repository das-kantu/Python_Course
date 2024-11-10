
# Example 28: Pandas - Concatenating DataFrames
import pandas as pd

# Creatig DataFrames:

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'C': [5, 6], 'D': [7, 8]})

# concatening dataframe:

concat_df = pd.concat([df1, df2], ignore_index= True)
print('Concatenated DataFrame: \n', concat_df)