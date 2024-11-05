
# Example 19: NumPy - Setting Values Using Indexing
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# setting specific values using indexing:
array[[1, 3]] = [100, 300]
print('Array After Setting Values: \n', array)