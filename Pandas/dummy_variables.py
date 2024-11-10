# Example 22: Pandas - Creating Dummy Variables
import pandas as pd

# Creating a DataFrame
data = { 
       
       'City': ['NY', 'LA', 'SF', 'NY']
       
       
       }
df = pd.DataFrame(data)

# creating dummpy variables:

dummies = pd.get_dummies(df['City'], prefix= 'City')
print(dummies)