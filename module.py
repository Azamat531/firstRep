# from random import choice as c
# password = ''
# letters = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
# count = 0
# while password != 'QWE':
#     password = ''
#     for i in range(3):
#         password += c(letters)
#     count += 1
# print(count)


# Problem1.1a
# from my_module import text
# print(text)


# Problem1.1b
# from random import choice as c
# names = ['valentina','adilet','altynai','ekaterina','azim','nikita','kaynush',
# 'suyunt','tima','adil','samat','azamat','akan']

# new_names = []
# for i in range(4):
#     new_names.append(c(names))
# print(new_names)


# Problem1.2
# import sys
# print(sys.version)


# Problem1.4 
# import os
# os.system('touch /home/azamat/lessons/casuro.txt')

# Problem1.5 
# from random import choice as c
# names = ['zarina','adilet','altynai','ekaterina','azim','kaynush',
# 'suyunt','tima','adil','samat','azamat','akan']
# team1 = []
# team2 = []
# team3 = []
# team4 = []

# for i in range(3):
#     a = c(names)
#     team1.append(a)
#     names.remove(a)
#     a = c(names)
#     team2.append(a)
#     names.remove(a)
#     a = c(names)
#     team3.append(a)
#     names.remove(a)
#     a = c(names)
#     team4.append(a)
#     names.remove(a)
# print(f'first team: {team1}')
# print(f'second team: {team2}')
# print(f'third team: {team3}')
# print(f'fourth team: {team4}')


# Problem2.2
# import sys
# a = input('input first: ')
# b = input('input second: ')

# a_size = sys.getsizeof(a)
# b_size = sys.getsizeof(b)
# if a_size > b_size:
#     print(f'first is bigger: {a_size}')
# elif b_size > a_size:
#     print(f'second is bigger: {b_size}')
# else:
#     print('they are equal')


# Problem2.3
# from string import ascii_letters,digits
# from random import choice
# characters = []
# for i in ascii_letters:
#     characters.append(i)
# for i in digits:
#     characters.append(i)
# password = ''
# a = int(input('input lenght of password: '))
# while len(password) < a:
#     password += choice(characters)

# print(password)


# Problem2.4
# from random import choice
# choises = ['scissor','stone','paper']
# print('choise one: ')
# for i in choises:
#     print(f'{choises.index(i)} - {i}')
# your_index = int(input('input index: '))
# print()
# computer_choise = choice(choises)
# print(f'your: {choises[your_index]}')
# print(f'computer: {computer_choise}')

# if choises[your_index] == computer_choise:
#     print('draw')
# elif choises[your_index] == 'scissor' and computer_choise == 'stone':
#     print('you lose')
# elif choises[your_index] == 'scissor' and computer_choise == 'paper':
#     print('you win')
# elif choises[your_index] == 'stone' and computer_choise == 'paper':
#     print('you lose')
# elif choises[your_index] == 'stone' and computer_choise == 'scissor':
#     print('you win')
# elif choises[your_index] == 'paper' and computer_choise == 'scissor':
#     print('you lose')
# elif choises[your_index] == 'paper' and computer_choise == 'stone':
#     print('you win')
# else:
#     print('error')


# Problem3.1
# from random import randint, randrange
# # print(randrange(6, 12 + 1, 2))
# print(randrange(5, 100 + 1, 5))


# Problem3.3
# from datetime import datetime, time, timedelta
# now = datetime.now()
# after_1000_days = now + timedelta(days= 1000)
# print(after_1000_days)


# Problem4.1
# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]
# for i in range(len(numbers) - 1):
#     print(numbers[i] + numbers[i + 1])


# Problem4.2
# from datetime import datetime
# now = datetime.now()
# print(now)


# Problem4.3
# def create_file(f_name: str) -> str:
#     f = open(f_name,'w')
#     return f
# f_create = create_file(file_name)
# f_create
# list2 = [2, 4, 6, 8, 10, 12, 14]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if i == j:
#             print(f'{list1[i]}  {list2[j]}')