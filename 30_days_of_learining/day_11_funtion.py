def generate_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name


print(generate_full_name('bro', 'mikey'))


def change(a):
    a = 10


a = 1

change(a)
print(a)


def generate_groups(team, *args):
    print(team, '1')
    print(args)
    for i in args:
        print(i)


print(generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob'))


def circle_area(radius):
    return 3.14*(radius**2)


print(circle_area(3))


def add_all_nums(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Error: '{arg}' is not a number"
        total += arg
    return total


print(add_all_nums(1, 2, 3, 4, 5))
print(add_all_nums(1, 2, 3, 4, 'a'))


def print_list(lst=[]):
    for i in lst:
        print(i)


lst = list[1, 2, 3, 4, 5]
print_list(lst)


def reverse_list(arg=[]):
    reverse_list_res = []
    for i in range(len(arg) - 1, -1, -1):
        reverse_list_res.append(arg[i])
    return (reverse_list_res)


test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse_list(test_list))


def capitalize_list(arg=[]):
    res_capitalize_list = []
    for i in arg:
        res_capitalize_list.append(i.upper())
    return res_capitalize_list


list_test = ['hello', 'world']
print(capitalize_list(list_test))


def evens_and_odds(num):
    if num % 2 == 0:
        print('The number of odds are {}'.format(num//2))
        print('The number of evens are {}'.format(num//2+1))
    else:
        print('The number of odds are {}'.format(num//2+1))
        print('The number of evens are {}'.format(num//2+1))


evens_and_odds(100)


def factorial(num):
    res = 1
    for i in range(1, num+1):
        res *= i
    return res


print(factorial(5))


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i < n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True
