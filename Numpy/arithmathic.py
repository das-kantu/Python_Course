# example 2: Numpy basic arithmathic operations:

import numpy as np

# creating arrays:

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

# arithmetic operations:

added = np.add(array_1, array_2)
subtracted = np.subtract(array_1, array_2)
multiplicated = np.multiply(array_1 , array_2)
divided = np.divide(array_1, array_2)
dotted = np.dot(array_1, array_2)



print('Added: ', added)
print('Subtracted: ', subtracted)
print('Multiplicated: ', multiplicated)
print('Divided: ', divided)
print('Dotted: ', dotted)
