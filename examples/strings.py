# Concatenating strings into variable
first_name = 'Luciano'
last_name = 'Pereira'
full_name = first_name + ' ' + last_name
print('full_name = ' + full_name)
# Formating string with functions 
print('UPPER = ' + full_name.upper())
print('lower = ' + full_name.lower())
print('Capitalize = ' + first_name.capitalize() + ' ' + last_name.capitalize())
print('Count = ' + str(full_name.count('a')))
# Test with inputs
first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')
print('Your name is {}'.format(full_name))
print('Your name is {0} {1}'.format(first_name, last_name))
print(f'Your name is {first_name.capitalize()} {last_name.upper()}')

