print(abs(-1))

# input('Enter your name:')

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#    'firstname':'Asabeneh',
#    'lastname':'Yetayeh',
#    'country':'Finland',
#    'city':'Helsinki'
#    }
# print('First name:', first_name)
# print('First name length:', len(first_name))
# print('Last name: ', last_name)
# print('Last name length: ', len(last_name))
# print('Country: ', country)
# print('City: ', city)
# print('Age: ', age)
# print('Married: ', is_married)
# print('Skills: ', skills)
# print('Person information: ', person_info)

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)

# first_name = input('What is your name: ')
# age = input('How old are you ? ')

# print(first_name, age)

# num_int = 10
# num_str = str(num_int)
# print('num_int: ',num_int, ', num_str: ', num_str)
# num_com = 1 + 2j
# print(num_com)



# Day 2: 30 Days of python programming

# variables.py
# first_name = 'bro'
# last_name = 'mikey'
# full_name = 'MikeyBro'
# city = 'QingDao'
# country = 'China'
# age = 19
# year = 2024
# is_married = False
# is_true = True

first_name, last_name, full_name, city, country, age,year, is_married, is_true = 'bro', 'mikey', 'MikeyBro', 'QingDao', 'Chian', 19, 2024, False, True

print(type(full_name))
print(type(age))
print(type(is_married))

print('Len of the first_name is: ', len(first_name))

len_first, len_last = len(first_name), len(last_name)

if len_first > len_last:
    print('the longer one is first name')
elif len_last > len_first:
    print('last name is longer')
else:
    print('the same length')

radius = float(input('Enter the radius: '))
area_circle = 3.14 * (radius * radius)
circum_circle = 3.14 * radius * 2
print('the area of the circle is ', area_circle, ', and the circum of the circle is ', circum_circle)

