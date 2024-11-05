# Example 5: NumPy - Slicing with Step
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# slicing with a step:

step_slice = array[::2]      # every second element
print('Original Array :\n', array)
print('Sliced Array with Step 2:\n', step_slice)
