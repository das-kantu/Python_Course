# Example 13: NumPy - Indexing Multi-dimensional Arrays with Slices
import numpy as np

# creating a 3x4 array:
array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# selecting specific rows and columns using slices:

selected_slice = array_2d[1:, 2:]
print('Selected Slices:\n', selected_slice)