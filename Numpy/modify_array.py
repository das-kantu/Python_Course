# Example 10: NumPy - Modifying Array Values using Indexing
import numpy as np

# creating an array:
array = np.array([10, 20, 30, 40, 50])

# modifying values at specific indices:

array[[1, 3]] = [100, 200]
print('Modified Array: ', array)