x = lambda param1, param2, param3:param1+param2+param3
# print(x(1,2,3))

numbers_tuple = (1,2,3,4,5)
numbers_list = [i for i in numbers_tuple if i % 2 == 0]
# print(numbers_list)

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers_filter = [i for i in numbers if i > 0]
# print(numbers_filter)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = [i for sublist1 in list_of_lists for sublist2 in sublist1 for i in sublist2]
# print(output)

list_tower = [(i,i**0,i**1,i**2,i**3,i**4,i**5,i**6)for i in range(11)]
# print(list_tower)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
output = [[country.upper(), country[:3:], capital.upper()]for subtuple in countries for country, capital in subtuple ]
# print(output)

