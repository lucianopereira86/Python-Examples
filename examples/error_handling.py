# Division by zero
x = 1
y = 0
try:
    print(x/y)
except ZeroDivisionError as e:
    print('You must NOT divide by zero!!!')
finally:
    print('This is a ZeroDivisionError test')

# Wrong type for parsing
a = 'abc'
try:
    print(int(a))
except ValueError as e:
    print('Your string cannot to be parsed to int')
finally:
    print('This is a ValueError test')

# Validation with Input 
try:
    b = int(input("Enter a positive integer: "))
    if b <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
else:
    print('Your number is positive!')
finally:
    print('This is an Input ValueError test')
    
