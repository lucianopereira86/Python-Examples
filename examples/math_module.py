from colorama import init, Fore

def sum(a, b):
    c  = a + b
    print(Fore.BLUE + f'sum = {a} + {b} = {c}')

def sub(a, b):
    c  = a - b
    print(Fore.RED + f'sub = {a} - {b} = {c}')
    
def mul(a, b):
    c  = a * b
    print(Fore.GREEN + f'mul = {a} * {b} = {c}')

def div(a, b):
    c  = float(a) / float(b)
    print(Fore.MAGENTA + f'div = {a} / {b} = {c}')
    
def exp(a, b):
    c  = a ** b
    print(Fore.YELLOW + f'exp = {a} ** {b} = {c}')

    