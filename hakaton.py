# task1 problem1
# a = input('input: +, -, /, *, **, //, %:  ')
# num1 = int(input('input first number: '))
# num2 = int(input('input second number: '))

# if a == '+':
#     print(num1 + num2)
# elif a == '-':
#     print(num1 - num2)
# elif a == '/':
#     print(num1 / num2)
# elif a == '*':
#     print(num1 * num2)
# elif a == '**':
#     print(num1 ** num2)
# elif a == '//':
#     print(num1 // num2)
# elif a == '%':
#     print(num1 % num2)
# else:
#     print(NameError)


# task1 problem2
# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 
# 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# a_13 = a.count(13)
# a_len = len(a)
# a_percent = a_13 * 100 / a_len
# if a_percent < 70:
#     print('really?')
# elif a_percent > 70:
#     print('I know that')
# else:
#     print('I dont think its a coincidence')


# task1 problem3
# login = input('input login: ')
# password = input('input password: ')
# users = []
# users.append(login)
# users.append(password)

# login_2 = input('input login: ')
# password_2 = input('input password: ')

# if login_2 in users and password_2 in users:
#     print('Welcome!')
# else:
#     print('Incorrect login or password')


# task2 problem1
# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# for key, value in dict1.items():
#     if value % 3 == 0:
#         print(f'{key} = Hi')
#     if value % 5 == 0:
#         print(f'{key} = Bye')


# task2 problem2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in range(len(languages)):
#     print(f'{i+1} {languages[i]}')


# task2 problem3
# total = 0
# for i in range(1,1000):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i
# print(total)


# task2 problem4
# num = 4729461084
# total = 0
# while num > 0:
#     total += num % 10
#     num = num // 10
# print(total)


# task2 problem5


# task2 problem6
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 
# 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 
# 'слова', 'фраза', 'введите', 'слово', 'кнопк    у',]
# for i in words:
#     check = True
#     for j in range(len(i) // 2):
#         if i[j] != i[len(i) - 1 - j]:
#             check = False
#     print(check)


# final
