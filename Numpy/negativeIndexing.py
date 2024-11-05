# Example 11: NumPy - Indexing with Negative Indices
import numpy as np

# creating an array:
array = np.array([10, 20, 30, 40, 50])

# accessing elements for the end using negative indices:

last_element = array[-1]
second_last_element = array[-2]

print('Original One Dimensional Array: \n', array)
print('=============================================')
print('Last Element: ', last_element)
print('Second Last Element: ', second_last_element)