# string
# letter = 'P'
# print(letter)

# greeting1 = 'Hello World!'
# print(greeting1)
# print(len(greeting1))
# greeting2 = "Hello World!"
# print(greeting2)
# print(len(greeting2))

# mult_setence = '''I am  a teacher and enjoy teaching.
# I didn't find anything as rewarding as empower people.'''# there can be line breaks between sentencce in this way
# print(mult_setence)

# first_name = 'bro'
# last_name = 'mikey'
# space = ' '
# full_name = first_name + space + last_name

# print(full_name)

# print('hello world! \n I\'m ',full_name, ' and I\'m test the escape sequences in strings, for example:\'\\n\', \'\\t\', \'\\\'\', \'\\\"\'')

# print('12345678\n \tno way')

# print('I\'m enjoying the python learning\tAnd you?')
# print('Days\tExercises\tTopics')
# print('Day 1\t5\t\t1')
# print('Day 2\t6\t\t2')
# print('Day 3\t7\t\t12')
# print('Day 4\t1\t\t23')

#  old string formatted
# first_name = 'bro'
# last_name = 'mikey'
# language = 'Python'
# formated_string = 'I am %s %s.I am learing %s'%(first_name, last_name, language)
# print(formated_string)

radius = 10
pi = 3.1415926
area = pi * radius**2
# print('%.2f'%(area))
# formated_string = 'The area of circle with a radius %d is %.2f'%(radius, area)
# print(formated_string)
# print('%d, %s, %f, %.3f'%(radius,radius,area,area))

# new formatted string
# first_name = 'bro'
# last_name = 'mikey'
# language = 'Python'
# formated_string = 'I am {} {}, I am learning {}'.format(first_name,last_name,language)
# print(formated_string)

# a, b = 3, 4
# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {}'.format(a, b, a / b))
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(b, a, b // a))
# print('{} ** {} = {}'.format(a, b, a ** b))

# print('The area of a circle with a radius {} is {:.5f}.'.format(radius, area))

# another new formatted string
# a = 4
# b = 3
# print(f'{a} + {b} = {a +b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')

# str_test1 = 'Hello World!'
# str_test2 = 'Python'
# print('{} {}.'.format(str_test1,str_test2))
# print(f'{str_test1} {str_test2}.')

# language = 'Python'

# letter1 = language[0]
# letter2 = language[1]
# letter3 = language[2]
# letter4 = language[3]
# letter5 = language[4]
# letter6 = language[5]
# print(letter1,letter2)
# print(letter6)
# letter_last = language[-1]
# print(letter_last)
# print('la%s'%(letter1))

# substring 
# language = 'Python'
# first_three = language[0:3] # [0, 3)
# print(first_three)
# last_three = language[3:6] # [3, 6)

# last_char = language[2:]
# print(last_char)
# last_char = language[-2:]
# print(last_char)

# resersing a string
# greeting = 'Hello world!'
# print(greeting[::-1])

# skipping characters while slicing
# language = 'Python'
# substring = language[0:6:2]
# print(substring)
# substring = language[0:6:3]
# print(substring)
# substring = language[5:0:-1]
# print(substring)


# string method

# sentence = '''hello world! thirty days of python'''
# print(sentence.capitalize())
# print(sentence.count('y', 10, 21))
# print(sentence.count('th'))
# print(sentence.endswith('on'))
#format()
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# age = 250
# job = 'teacher'
# country = 'Finland'
# sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
# print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

# challenge = 'thirty days of pythoonnn'
# print(challenge.strip('thon')) # 'irty days of py'

# challenge = 'thirty days of python'
# print(challenge.split()) # ['thirty', 'days', 'of', 'python']
# challenge = 'thirty, days, of, python'
# print(challenge.split(',')) # ['thirty', 'days', 'of', 'python']


# exercise Day 4

str1 = ['Tirty', 'Days', 'of', 'Python']
res1 = ' '.join(str1)
print(res1)

company = 'Coding For All'
print(company)
upper_company = company.upper()
print(upper_company)

print(company.capitalize())
print(company.swapcase())
print(company.lower())
print(company.upper())
print(company.title())

print(company.split(' '))

company2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(company2.split(','))

print(company[0])
print(company[-1])
print(company[10])

company3 = '''I am enjoying this challenge.
\tI just wonder what is next.'''
print(company3.expandtabs(15))

print('Name\t\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

a, b = 8, 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


