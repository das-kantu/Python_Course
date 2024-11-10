# Example 47: Pandas - Using pd.cut for Binning Data
import pandas as pd

# Creating a DataFrame
data = {
    'Scores': [50, 60, 70, 80, 90, 100]
    
    
    }
df = pd.DataFrame(data)

# binning the score in category:

df['Grade'] = pd.cut(df['Scores'], 
                     bins = [0, 59, 69, 79, 89, 100],
                     labels = ['F', 'D', 'C', 'B', 'A'])

print('DataFrame With Binned Scores: \n', df)