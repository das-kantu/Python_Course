
# Example 27: NumPy - Advanced Indexing with Meshgrid
import numpy as np

# creating 1D-array:

x = np.array([1, 2, 3])
y = np.array([4, 5])

# creating a meshgrid for advance indexing:

X , Y = np.meshgrid(x,y)

indices = np.vstack([X.ravel(), Y.ravel()])
print('Indices For Meshgrid Advanced Indexing: \n', indices)