# Example 16: NumPy - Extracting Diagonal Elements
import numpy as np

# creating a square matrix:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# extracting the main diagonal:
diagonal_elements = np.diag(matrix)


print('Original Matrix:\n', matrix)
print('----------------------------')
print('Diagonal Elements:', diagonal_elements)