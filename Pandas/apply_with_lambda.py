
# Example 3: Pandas - Using Apply with Lambda Functions
import pandas as pd

# Creating a DataFrame
data = {
    
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [85, 90, 95]
}

df = pd.DataFrame(data)
print(df)

# applying a lambda function to modify score:

df['Adjusted_Score'] = df['Score'].apply(lambda x: x + 5 if x < 90 else x)

print('Data Frame With Adjusted Score: \n',df)