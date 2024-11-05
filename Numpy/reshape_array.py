# Example 7: NumPy - Reshaping Arrays
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6])

# reshaping to different dimensions:

reshaped_array = array.reshape((2, 3))

print('Original Array:\n', array)
print('Reshape Array:\n ', reshaped_array)