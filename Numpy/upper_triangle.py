

# Example 20: NumPy - Extracting Upper Triangle of a Matrix
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# extracting the upper elements(above the main diagonal):

upper_triangle = np.triu(matrix)
print('Upper Triangle Matrix: \n', upper_triangle)