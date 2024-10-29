# Example 2: tuple unpacking:
# unpacking a tuple with multiple values into variables , including using the * operator for remaining values:
# example tuple:

person_information = ('Kelly', '30', 'California', 'Engineer', 'Single')

# unpacking tuple into variables:

name , age , *other_details = person_information

print('Name:',name)
print('Age:', age)
print('Other_details:', other_details)