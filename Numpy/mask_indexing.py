
# Example 15: NumPy - Masked Indexing
import numpy as np

# Creating an array
array = np.array([1, -2, 3, -4, 5])

# creating a mask for positive values:

mask = array > 0

# applysing mask to get only positive values:

positive_values = array[mask]
print('Positive Values: ', positive_values)