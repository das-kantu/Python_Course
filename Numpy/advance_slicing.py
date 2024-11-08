
# Example 18: NumPy - Advanced Slicing with Step in 2D Array
import numpy as np

# creating a 2D array:

array_2D = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(array_2D)

# Slicing every second elements in row and columns:

result = array_2D[::2 , ::2]
print('Advanced Sliced Array With Step:\n', result)