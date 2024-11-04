# Example 2:Numpy -2 D Array Indexing:

import numpy as np

# creating a 2-D array:

array_2D = np.array([[1, 2, 3], 
                     [4, 5, 6],
                     [7, 8, 9]])

# accessing individual elements:

element = array_2D[1, 2]       # accessing elements at row 1 and col 2

# slicing rows and columns:

row_slice = array_2D[0 , :]    # first row
column_slice = array_2D[:, 1]  # second column

print('Element at (1,2):', element)
print('First Row:', row_slice)
print('Second Column:', column_slice)