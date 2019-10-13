# Logging before and after a function be executed
def logger(func):
    def wrapper(): # Function called by the decorator
        print('Start')
        func() # External function
        print('End')
    return wrapper

@logger # Decorator
def my_function(): # External function
    print('...Executing function...')

my_function()
