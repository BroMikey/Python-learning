# collection data type 
# list, tuple, set, dictionary

# fruits = ['banana', 'orange', 'mango', 'lemon']
# print('Fruits',fruits)
# print('the number of fruits: ',len(fruits))

# print('Fruits',fruits[-1])

# lst = ['item1','item2','item3', 'item4', 'item5']
# first_item, second_item, third_item, *rest = lst
# print(first_item)     # item1
# print(second_item)    # item2
# print(third_item)     # item3
# print(rest)           # ['item4', 'item5']

# # First Example
# fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
# first_fruit, second_fruit, third_fruit, *rest = fruits 
# print(first_fruit)     # banana
# print(second_fruit)    # orange
# print(third_fruit)     # mango
# print(rest)           # ['lemon','lime','apple']
# # Second Example about unpacking list
# first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)          # 1
# print(second)         # 2
# print(third)          # 3
# print(rest)           # [4,5,6,7,8,9]
# print(tenth)          # 10
# # Third Example about unpacking list
# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr)
# print(fr)
# print(bg)
# print(sw)
# print(scandic)
# print(es)

# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits)
# fruits[0] = 'avocado'
# print(fruits)

# fruits.append('watermelon')# ['avocado', 'mango', 'lemon', 'watermelon']
# print(fruits)
# fruits.insert(2, 'apple')
# print(fruits)

# fruits.remove('apple')
# print(fruits)

# fruits.pop()
# print(fruits)
# fruits.pop(1)
# print(fruits)

# del fruits[0]
# print(fruits)
# # del fruits

# # fruits.clear()

# fruits_copy = fruits.copy()
# print(fruits_copy)

# vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

# fruits_vegetables = fruits + vegetables
# print(fruits_vegetables)

# fruits.extend(vegetables)
# print(fruits)

# print(vegetables.count('Tomato'))

# print(vegetables.index('Tomato'))

# fruits.reverse()
# print(fruits)

# # fruits.sort()
# # print(fruits)

# print(fruits)
# print(sorted(fruits))
# print(fruits)
# fruits.sort(reverse=True)
# print(fruits)



# exercise
# excs1 = list()

# excs2 = ['item1', 'item2', 'item3', 'item4', 'item5']

# print(len(excs2))

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# print(max(ages))
# print(min(ages))

# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# separator = '#'
# joined_companies = separator.join(it_companies)

# print(joined_companies)

# full_stack = joined_companies
# print(full_stack) 
company = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] 
print(company) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 增删改查
# 增
company.append('Tecent') # 向当前列表增加元素
company.extend(['Meta','Huawei']) # 增加另一个列表
# 删
company.remove('Tecent') # 删除元素
company.pop() # 删除列表最后一个元素
company.pop(1) # 删除索引为1的元素
del company[1] # 同上
# 改
company[0] = 'X'# 修改某一元素可以直接使用下标索引
company.reverse()
company.sort()
print(company)
company.sort(reverse = True)
print(company)
sorted_company = sorted(company)
print(sorted_company)
print(company.count('X'))