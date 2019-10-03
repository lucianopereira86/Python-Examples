from datetime import datetime
# Without parameters
def print_time():
    print(f'Now = {datetime.now()}')

print_time()
for x in range(0, 5):
    print(x)
print_time()

# With parameters
def counter(count):
    print(f'Count = {count}')

counter(0)
for x in range(1, 5):
    counter(x)
counter(5)

# With return and parameters
def sum(a, b):
    print(f'a = {a}, b = {b}')
    return a + b 
x = sum(1, 2)
print(f'x = {x}')
y = sum(x, 2)
print(f'y = {y}')
z = sum(y, 2)
print(f'z = {z}')

# Named notation and Boolean parameter
def print_line(text, isPrint = False):
    if isPrint:
        print('Text = ' + text)

print_line('No print')
print_line(isPrint=True, text='Print me!')



