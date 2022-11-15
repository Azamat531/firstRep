# dict1 = {
#     '8932569':
#     {
#         'name': 'azat',
#         'age': 20,
#         'gender': 'm',
#         'id': 789932489
#     }
# }
# for key in dict1:
#     for key_2 in dict1[key]:
#         print(dict1[key][key_2])


# Problem1.1
# def add(n1, n2):
#     return n1 + n2

# def substract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# num1 = int(input('>>>> '))
# num2 = int(input('>>>> '))

# print(add(num1, num2))
# print(substract(num1, num2))
# print(multiply(num1, num2))
# print(divide(num1, num2))


# Problem1.2
# def count_len(asdf):
#     count = 0
#     for i in asdf:
#         count += 1
#     return count
# print(count_len('jnvaebh'))


# Problem1.3 ???
# def join_dict(d_1, d_2):
#     print(d_1.update(d_2))
#     return d_1.update(d_2)
# dict_1 = {
#     'name': 'aza',
#     'age': 25
# }
# dict_2 = {
#     'gender': 'male',
#     'id': 978223
# }
# print(join_dict(dict_1,dict_2))


# Problem1.4
# def create_file(order):
#     with open('menu.txt', 'w') as f:
#         f.write(order)
# order = input('what you want?  ')
# create_file(order)


# Problem1.5
# file_name = input('write name to file: ')
# def create_file(f_name: str) -> str:
#     f = open(f_name,'w')
#     return f
# f_create = create_file(file_name)
# f_create


# Problem2.1
# def main_funciton():
#     print('I am main function')
#     sub_function()
# def sub_function():
#     print('I am sub function')
# main_funciton()


# Problem2.2 ???


# Problem2.3
# def prime_numbers(number):
#     for i in range(2,number):
#         if number % i == 0:
#             return False
#     return True
# num = int(input('input number: '))
# if prime_numbers(num):
#     print('prime')
# else:
#     print('not prime')


# Problem3.1
# def join_values(a, b):
#     list_1 = []
#     list_1.append(a)
#     list_1.append(b)
#     return list_1
# print(join_values(4, 'aoo'))


# Problem3.2
# def number_of_lines(n_lines):
#     for i in range(n_lines):
#         print(n_lines)
# number = int(input('>>>  '))
# number_of_lines(number)


# Problem3.3
# def salary(name, s = 5000):
#     return f'{name} {s}'
# print(salary('dan'))


# Problem3.4
# def gen(n):
#     from random import choice
#     list1 = []
#     for i in range(n):
#         list1.append(choice('qwertyuopasdfghjklimnbvcxz'))
#     return list1
# print(gen(7))