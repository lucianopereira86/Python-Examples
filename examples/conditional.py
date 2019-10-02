# Multiple conditions
x = 0
if x > 0:
    print("It's a positive number")
elif x == 0:
    print("It's zero")
else:
    print("It's a negative number")

# Case sensitivity and 'or' operator
name = 'Luciano'
if name == 'LUCIANO':
    print('You are LUCIANO')
else:
    print('You are not LUCIANO')
    
if name.upper() == 'LUCIANO' or name.lower() == 'luciano':
    print('You are LUCIANO')
else:
    print('You are not LUCIANO')

# 'and' operator
word = input('Enter a word with at least 4 characters and containing the letter "a":\n')
if word.count('a') > 0 and len(word) >= 4:
    print(f'{word} is a valid word!')
else:
    print(f'{word} is an invalid word!')

# 'in' operator and Boolean variable
x = int(input(f'Enter a number:\n'))
y = (1, 3, 5, 7, 11, 13, 17)
if x in y:
    contains = True
else:
    contains = False
print(f'{x} { "is" if contains else "is not" } in {y}')

