def sum_numbers(nums):
    return sum(nums)

# def higher_order_function(f, lst):  # function as a parameter
#     summation = f(lst)
#     return summation
# result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
# print(result)


# return a function
def square(x):
    return x ** 2
def cube(x):
    return x ** 3

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    
# print(higher_order_function('square')(3))

# function closure
def out_function(x):
    def in_function(y):
        return x + y
    return in_function

closure = out_function(10)
# print(closure(5)) # 15

# decorator
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
# print(g())


# '''These decorator functions are higher order functions
# that take functions as parameters'''



# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
# print(greeting())   # WELCOME TO PYTHON

