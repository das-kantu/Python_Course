
# Example 24: Pandas - Assign Method for Adding Columns
import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Score': [85, 90, 95]
        
        }
df = pd.DataFrame(data)

# adding a new column using assign:

df = df.assign(Grade = lambda x: ['A' if score >= 90 else 'B' for score in  x['Score']])
print('DataFrame With Assigned Grade Column: \n', df)