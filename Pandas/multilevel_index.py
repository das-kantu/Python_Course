
# Example 41: Pandas - Combining DataFrames with Multi-level Indexes
import pandas as pd

# creating dataframe with multilevel index:

arrays = [['A', 'A', 'B', 'B'], [2020, 2021, 2020, 2021]]
data1 = [100, 150, 200, 250]

index = pd.MultiIndex.from_arrays(arrays, names = ('Category', 'Year'))
df1 = pd.DataFrame(data1, index = index, columns= ['Sales'])

data2 = [300, 400, 500, 600]

df2 = pd.DataFrame(data2, index = index, columns = ['Profit'])

# combining dataframe:

combined_df = pd.concat([df1, df2], axis = 1)

print('Combined DataFrame With Multilevel Indexing: ',combined_df)