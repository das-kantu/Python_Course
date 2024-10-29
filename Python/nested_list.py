# Example 1: Nested Lists Operations
# Working with nested lists by accessing elements, modifying values, and flattening the list.

# example nested list:

nested_list = [[1, 2, 3], [4, 5, [6, 7]], [8, 9]]

# accessing a nested element:

nested_element = nested_list[1]
nested_element = nested_list[1][2]
nested_element = nested_list[1][2][1]


# modifying a nested elements:

nested_list[2][1] = 10 # changing 9 to 10


# flattening the nested list:
flattened_list = [element for sublist in nested_list for item in sublist for element in (item if isinstance(item, list) else[item]) ]

print('Nested Element: ', nested_element)
print('Modified Nested List:', nested_list)
print('Flattened List: ', flattened_list)