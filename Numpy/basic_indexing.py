# Example 1: NumPy - Basic Indexing and Slicing
import numpy as np

# Creating an array
array = np.array([10, 20, 30, 40, 50])

# accessing elements by index:

first_element = array[0]
second_element = array[-1]



# slicing the elements:
slice_array = array[1:4]

print('First Element:', first_element)
print('Second Element:', second_element)
print('Sliced Array: ', slice_array)