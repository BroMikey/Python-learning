# st = set()

# st = {'item1', 'item2', 'item3', 'item4'}

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# len(fruits)
# print('banana in fruits:','banana'in fruits)

# fruits.add('watermelon')

# st = {'item1', 'item2', 'item3', 'item4'}
# st.update(['item5','item6'])

# fruits.pop()
# print(fruits)
# removed_fruit = fruits.pop()
# print(fruits)
# print(removed_fruit)

# fruits.clear()
# print(fruits)

# fruits = set()
# del fruits

# fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
# fruits = set(fruits) # set will clear the same element
# print(fruits)

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# print(fruits.union(vegetables))
# print(fruits)

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# print(whole_numbers.intersection(even_numbers))
# print(whole_numbers)

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# print(whole_numbers.issubset(even_numbers))
# print(whole_numbers.issuperset(even_numbers))

# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# print(st2.difference(st1)) # st2 - (st1 ∩ st2) = set()
# print(st1.difference(st2)) # st1 - (st1 ∩ st2) = {'item1', 'item4'}
# st3 = st1 - st2
# print(st3)

# relative complement
# B \ A = B - A = {x|x∈B x∉A}
# symmetric difference
# A ⊕ B = (A - B) ∪ (B - A) = (A ∪ B) - (A ∩ B)
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# some_numbers = {1, 2, 3, 4, 5}
# print(whole_numbers.symmetric_difference(some_numbers))
# print(some_numbers.symmetric_difference(whole_numbers))

# disjoint
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# print(st2.isdisjoint(st1))
# even_numbers = {0, 2, 4 ,6, 8}
# odd_numbers = {1, 3, 5, 7, 9}
# print(even_numbers.isdisjoint(odd_numbers))



it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# print(len(it_companies))

# it_companies.add('Twitter')

# print(it_companies)
# it_companies.update(['Huawei','Samsung'])
# print(it_companies)

# print(A.union(B))
# print(A.intersection(B))
# print(A.issubset(B))
# print(A.isdisjoint(B))
# print(A.union(B))
# print(B.union(A))

# print(A.symmetric_difference(B))
# del A, B

# age_set = set(age)
# print(age)
# print(len(age))
# print(age_set)
# print(len(age_set))

# string常见字符串，list即列表（cpp中的数组），tuple是不可更改的一列元素，set即为集合

sentence = "I am a teacher and I love to inspire and teach people."

words = sentence.split()  # Split the sentence into words
unique_words = set(words)  # Create a set to eliminate duplicates
print(unique_words)
num_unique_words = len(unique_words)  # Get the count of unique words

print("Number of unique words:", num_unique_words)