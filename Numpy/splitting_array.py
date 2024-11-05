
# Example 16: NumPy - Splitting Arrays
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# splitting the array into three parts:

split_array = np.array_split(array,3)
print(split_array)