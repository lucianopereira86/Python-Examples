# 'for' loop with a list
countries = ['Brazil', 'China', 'USA']
for country in countries:
    print('Country = ' + country)

# 'for' loop with a range
for x in range(0, 5):
    print('Counting = ' + str(x))

# 'while' loop
fruits = ['orange', 'apple', 'pear']
cont = 0
while cont < len(fruits):
    print(f'Fruit #{cont + 1} = {fruits[cont]}')
    cont = cont + 1

