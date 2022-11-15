# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} * {j} = { i * j }') 


# space = ' '
# we_need = ''
# for i in range(0,2):
#     for j in range(1,11):
#         for k in range(i * 5 + 1,(i+1) * 5 + 1):
#             if j < 10:
#                 we_need += space
#             if k * j < 10:
#                 we_need += space
#             print(f'{k} * {j} = {k * j}   {we_need}', end='')
#             we_need = ''
#         print()
#     print()

# lst = [[1,2,3], [4,5,6], [7,8,9]]
# lst2 = []

# for i in lst:
#     for j in i:
#         lst2.append(j)
# print(lst2)


# lst = [[1,2,3],['first','second','third'],[7,8,9]]
# letters = []
# numbers = []

# for i in lst:
#     for j in i:
#         if type(j) == str:
#             letters.append(j)
#         elif type(j) == int:
#             numbers.append(j)

# print(letters)
# print(numbers)





# numbers = []
# sum_numbers = 0
# count = 0
# while True:
#     command = input('input number: ')
#     if command == 'end':
#         break
#     else:
#         numbers.append(int(command))

# for i in numbers:
#     print(i)
#     sum_numbers += i
#     count += 1
# print(command)

# print(f'you entered: {numbers}')
# print(f'total: {sum_numbers}')
# print(f'average: {sum_numbers/count}')


# print('Enter two strings: ')
# first_str = input()
# second_str = input()

# if len(first_str) > len(second_str):
#     print(f'first string is longer by {len(first_str) - len(second_str)} characters')
# elif len(second_str) > len(first_str):
#     print(f'second string is longer by {len(second_str) - len(first_str)} characters')
# else:
#     print('strings are equal')