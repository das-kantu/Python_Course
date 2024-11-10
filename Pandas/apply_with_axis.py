# Example 51: Pandas - Using df.apply with Axis Parameter
import pandas as pd

# creating a DataFrame:

data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
}

df = pd.DataFrame(data)

# Applying a function to rows and columns using the axis parameter:

row_sum = df.apply(lambda x: x.sum(), axis = 1)
col_sum = df.apply(lambda x: x.sum(), axis = 0)
print('Row Wise_Sum: \n',row_sum)
print('Column Wise Sum: \n',col_sum)