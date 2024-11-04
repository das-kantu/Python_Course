# Example 7: NumPy - Indexing with Arrays
import numpy as np

# creating a 2-D array:
array_2D = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# using arrays for indexing:
rows = np.array([0, 1, 2])
cols = np.array([2, 1, 0])
index_elements = array_2D[rows, cols]

print('Two Dimensional Array:\n', array_2D)
print('===============================')
print('Index Elements: ', index_elements)
