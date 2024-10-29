# tuple comprehension using generator expression:
# creating a tuple using generator expressions for elements that meet a condition

# example range of numbers:

# creating a tuple of squares of even numbers:

numbers = range(11, 30)
odd_squares = tuple(x **2 for x in numbers if x % 2 == 1)

print('Tuple of Odd Squares:', odd_squares)