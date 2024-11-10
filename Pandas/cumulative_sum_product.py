
# Example 13: Pandas - Cumulative Sum and Product
import pandas as pd

# Creating a DataFrame
data = {   
    
    'Sales': [100, 200, 150, 300, 250]
    
    }
df = pd.DataFrame(data)


# calculating cumulative sum and product:

df['Cumulative Sum'] = df['Sales'].cumsum()
df['Cumulative Product'] = df['Sales']. cumprod()

print('DataFrame With Cumulative Productions:\n',df)