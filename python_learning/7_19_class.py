# class Student:
#     name = None
#     gender = None
#     nationality = None
#     native_place = None
#     age = None
#
# stu_1 = Student()
#
# stu_1.name = 'BroMikey'
# stu_1.age = 19
# stu_1.gender = '男'
# stu_1.nationality = 'China'
# stu_1.native_place = '河南'
#
# print(stu_1.name)
# print(stu_1.age)
# print(stu_1.gender)
# print(stu_1.nationality)
# print(stu_1.native_place)

# class Student:
#     name = None
#     age = None
#     tel = None
#     def say_hi(self):
#         print(f'hi,I am {self.name}',end='')
#         print(f' and I am {self.age} years old')
#
#     def __init__(self,name,age,tel,test):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.test = test
#     def print_stu_info(self):
#         print(f'I am {self.name}, and I am {self.age} years old, my number is {self.tel}')

# stu_1 = Student()
# stu_1.name = 'Bromikey'
# stu_1.age = 19
# stu_1.say_hi()
# stu_1 = Student('BroMikey','19','156****2725',True)
# stu_1.print_stu_info()

# class Student:
#     name = None
#     age = None
#
#     def __init__(self,name,age):
#         '''
#         两个变量的构造函数
#         :param name: the student's name
#         :param age: age
#         '''
#         self.name = name
#         self.age = age # If it has already been defined, a value is assigned to the variable
#         # If not defined, the variable is defined
#     def __int__(self):
#
#     def print_stu_info(self):
#         print(f'The student is {self.name},and {self.name} is {self.age}')
#
#
# stu_1 = Student('Bro Mikey',19)
# stu_1.print_stu_info()
#
# stu_2 = Student()

# class Student:
#     name = None
#     age = None
#     adress = None
#     def __init__(self):
#         self.name = input('请输入学生姓名：')
#         self.age = input('请输入学生年龄：')
#         self.adress = input('请输入学生地址：')
#
#     def print_stu_info(self):
#         print(f'【学生姓名：{self.name}, 年龄：{self.age}，地址：{self.adress}】')
#
# students = []
# for i in range(10):
#     print(f'当前录入第{i+1}位学生信息，总共需录入10位学生信息')
#     stu = Student()
#     students.append(stu)
#     print(f'学生{i+1}信息录入完成，信息为',end = '')
#     stu.print_stu_info()

#
# class Student:
#     name = None
#     age = None
#     address = None
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def print_stu_info(self):
#         print(f'【学生姓名：{self.name}, 年龄：{self.age}，地址：{self.address}】')
#
#     def __str__(self):
#         return f'Student类对象，name:{self.name}，age:{self.age}，address:{self.address}'
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
# stu_1 = Student('Bro',19,'henan')
# stu_2 = Student('China',75,'Asia')
# print(stu_1 > stu_2)
# print(stu_1 == stu_2)

# class Phone:
#     __is_5g_enable = True
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print('5g开启')
#             return True
#         else:
#             print('5g关闭,使用4g网络')
#             return False
#
#     def call_by_5g(self):
#         self.__check_5g()
#         print('正在通话中')
#
# phone = Phone()
# phone.call_by_5g()

# class Phone:
#     IMEI = None
#     producer = 'HM'
#
#     def call_by_4g(self):
#         print('4g通话')
#
# class Phone2022(Phone):
#     producer = 'itBRO'
#     face_id = 10001
#
#     def call_by_4g(self):
#         # print(f'{Phone.producer}')
#         # Phone.call_by_4g(self)
#         print(f'{super().producer}')
#         super().call_by_4g()
#         print('子类的4g通话')
#
#     def call_by_5g(self):
#         print('5g通话')
#
# phone = Phone2022()
# phone.call_by_4g()


# import random
# random.randint()

# my_list_1: list = [1, 2, 3]
# my_list_2: list[int] = [1, 2, 3]
# my_tuple: tuple[str, int, bool] = ('Bro', 19, True)
# my_dict: dict[str, int] = {'Bro': 19}
# import random
# var_1 = random.randint(1, 10) # type: int

# from typing import Union
#
#
# def func(data: list) -> list:
#     pass
#
#
# my_list: list[Union[int, str]] = [1, 2, 'itBro']
#
#
# data_1 = list()
# func(data_1)

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')

def make_noise(animal: Animal):
    animal.speak()

