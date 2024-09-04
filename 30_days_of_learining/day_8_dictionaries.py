# empty_dict = {}
# empty_dict = dict()

# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
#     }
# print(len(person))# len() shows the number of 'key:value'

# print(person['first_name'])
# print(person['age'])
# print(person['address']['street'])

# person['job_title'] = 'Instructor'
# person['skills'].append('HTML') # ['skill'] points  to a list, so we can use append function

# person['age'] = 19

# print('age'in person)

# pop(),popitem(),del
# person.pop('first_name')
# person.popitem()
# del person['is_marred']
# print(person)

# person.clear()

# del person

# person_copy = person.copy()

# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# values = dct.values()
# print(values)

dog = dict()
dog['name'] = 'cola'
dog['color'] = 'yellow'
dog['breed'] = 'unknown'
dog['legs'] = 'four'
dog['age'] = '3'
print(dog)
print(dog.get('name'))

student = {
    'first_name' : 'bro',
    'last_name' : 'Mikey',
    'gender' : 'man',
    'age' : 19,
    'marital status' : 'unmarried',
    'country' : 'China',
    'city' : 'shangcai',
    'skill' : ['Cpp/C', 'python']
}

print(len(student))

keys_student = student.keys()
print(keys_student)
values_student = student.values()
print(values_student)

student['skill'].append('AI')
print(student['skill'])

list_student = student.items()
print(list_student)

del student['marital status']

del student