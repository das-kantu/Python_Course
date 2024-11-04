# Example 22: NumPy - Extract Lower Triangle of a Matrix
import numpy as np

# creating a square matrix:

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# extracting the lower trianglge(below the main diagonal):
print('Original Matrix:\n', matrix)
print('--------------------------------')

lower_triangle = np.tril(matrix)
print('Lower Triangle of the Matrix:\n', lower_triangle)