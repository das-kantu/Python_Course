# Example 23: NumPy - Multi-dimensional Array Indexing with Mixed Types
import numpy as np

# creating a 3D array:

array_3d = np.array([[[1, 2], 
                      [3, 4]],
                      [[5, 6],
                       [7,8]],
                       [[9, 10], 
                        [11, 12]]])

# mixing slicing with direct indexing:
mixed_index = array_3d[1:, 0, 1]
# mixed_index = array_3d[2:, 0, 1]

print('Three Dimension Array: \n', array_3d)
print('Mixed Type Indexing Result: ', mixed_index)