
# Example 34: Pandas - Adding a Prefix or Suffix to Column Names
import pandas as pd

# creating a dataframe:

data = {'Math': [90, 80],
        'Science': [85, 88]
        }

df = pd.DataFrame(data)
# print(df)

# adding prefix to column name:

df_prefixed = df.add_prefix('Grade_')

# adding a suffix to column name:
df_suffixed = df.add_suffix('_Score')

print('Data Frame with Prefixed: \n',df_prefixed)
print('Data Frame with Suffixed:\n',df_suffixed)