# Example 3: Set Comprehension with Condition
# Creating a set using comprehension with a condition to filter specific elements.

# example list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# creating a set even numbers:

odd_set = {num for num in numbers if num % 2 == 1} 

print('Set Of Odd Numbers: ', odd_set)