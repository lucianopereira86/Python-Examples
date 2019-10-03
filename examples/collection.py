# Simple list
names = ['Luciano', 'PEREIRA']
print('names = ' + str(names))

# Populating a list dynamically
numbers = []
numbers.append(1)
numbers.append(2)
print('numbers = {}'.format(numbers))
print('first number = {0}'.format(numbers[0]))

# Array with defined type ('d' = digits)
from array import array
grades = array('d')
grades.append(9.5)
grades.append(7)
grades.append(10)
print(f'grades = {grades}')
print(f'higher grade = {grades[2]}')

# Common operations
pokemon = ['Bulbasaur', 'Charmander', 'Squirtle']
print(f'Pokemon = {pokemon}')
pokemon.insert(0, 'Pikachu')
print(f'Added Pokemon = {pokemon}')
pokemon.sort()
print(f'Sorted Pokemon = {pokemon}')

# Ranges
heroes = ['Superman', 'Batman', 'Wolverine'] 
dc_heroes = heroes[0:2]
print('DC Heroes = ' + str(dc_heroes))

# Dictionaries
pikachu = { 'color' : 'yellow' }
pikachu['type'] = 'eletric'
print('Pikachu color = ' + pikachu['color'])

