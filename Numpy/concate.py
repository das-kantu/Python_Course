# Example 15: NumPy - Concatenation of Arrays
import numpy as np

# creating array:

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

concatenated_array = np.concatenate((array_1, array_2))
print('Concatenated Array: ', concatenated_array)