
# Example 20: NumPy - Cumulative Sum and Product
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4])

# calculating cumalative sum and product:

cumalative_sum = np.cumsum(array)
cumalative_product = np.cumprod(array)
print('Cumalative Sum: ',cumalative_sum)
print('Cumalative Product: ', cumalative_product)