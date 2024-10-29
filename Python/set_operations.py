# example:6
# set operations with multiple sets:
# Performing Union, Intersection and symmetric differences with three sets:

# example sets:

set_1 = {'cat', 'dog' , 'hen', 'duck'}

set_2 = {'hen', 'duck', 'rabbit', 'bird'}

set_3 = {'duck', 'bird', 'tiger', 'snake'}

# performing set operations:

union_result = set_1 | set_2 | set_3

intersection_result = set_1 & set_2 & set_3

symmetric_difference_result = set_1 ^ set_2 ^ set_3

print('Union Result:', union_result)
print('Intersection Result: ', intersection_result)
print('Symmetric_Difference_Result: ', symmetric_difference_result)