# import mymodule

# print(mymodule.full_name('Bro', 'Mikey'))


# from mymodule import full_name

# print(full_name('Bro', 'Mikey'))

# from mymodule import full_name as fullname, add_two as total

# print(fullname('Bro', 'Mikey'))
# print(total(1, 2))

# import os
# print(os.getcwd())

# import sys
# print(sys.version)

# import math

# print(math.pi)
# print(math.sqrt(4))
# print(math.pow(2, 3))

# from math import *# you do not need prefix all functions
# import math

# import string
# print(string.ascii_letters)

# from random import random, randint
# print(random())

import random
import string
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters,k = 6))
    return user_id

# print(random_user_id())

def better_random_user_id(len,num):
    characters = string.ascii_letters + string.digits
    user_id = []
    for i in range(num):
        user_id.append(''.join(random.choices(characters,k = len)))
    
    return user_id

# print(better_random_user_id(16,5))

def red_green_blue():
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)
    rgb_color = f'rgb({R},{G},{B})'
    return rgb_color

# print(red_green_blue())

def random_hex_id(len):
    characters = string.digits + 'abcdef'
    user_id = ''.join(random.choices(characters,k = len))
    return user_id

print(random_hex_id(10))

