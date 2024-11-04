
# Example 8: NumPy - Conditional Indexing
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# setting elements that satisfy a condition:

array[array % 2 == 0] = -1  # set even numbers to -1
print('Array After Conditional Indexing:', array)