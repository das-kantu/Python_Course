# Example 18: NumPy - Meshgrid Creation
import numpy as np

# Creating 1D arrays
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# creating a MeshGrid:

X , Y = np.meshgrid(x, y)

print('Mesh Grid X:\n',X)
print('Mesh Grid Y:\n',Y)