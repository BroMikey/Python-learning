# 一个带有__init__.py的module文件夹
# import my_package.my_module1
# my_package.my_module1.module1_info()

# from my_package import my_module1

# from my_package.my_module1 import module1_info

import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("Hello Python"))

file_util.print_file_info('C:/Users/34698/Desktop/30DaysOfPython/python_learning/bill.txt')
file_util.append_to_file('C:/Users/34698/Desktop/30DaysOfPython/python_learning/bill.txt','\nend')
file_util.print_file_info('C:/Users/34698/Desktop/30DaysOfPython/python_learning/bill.txt')
















