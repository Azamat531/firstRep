# Problem1
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# lang1=input('Input language: ')
# for i in languages:
#     if i == lang1:
#         print('have')


# Problem2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
#     print(i)


# Problem3
# num1=1
# for i in range(5):
#     num1 *=7
# print(num1)


# Problem4
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in range(len(languages)):
#     print(f'{i} {languages[i]}')


# Problem5
a = 1
b = 1
nums = []
while a>0:
    nums.append(a)
    a+=b
    if a == 10:
        b = -1
print(nums)


# Problem6
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай',
# 'Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(0,len(names),2):
#     print(names[i])


# Problem7
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай',
# 'Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in range(1,len(names),2):
#     print(names[i])


# Problem8
# num1 = int(input('input number: '))
# # check1
# if num1 > 99 and num1 < 1000:
#     print('YES')
# else:
#     print('NO')

# # check2
# if num1 > 0 and num1 % 2 == 0:
#     print('YES')
# else:
#     print('No')

# # check3
# if num1 % 31 == 0:
#     print('YES')
# else:
#     print('NO')

# # check4
# if (num1 > 100 and num1 % 17 == 0) or (num1 > 150 and num1 == 13**2):
#     print(num1)
# else:
#     print('NO')


# Problem9
# count1=0
# count2=0
# for i in range(-100,101):
#     if i % 13 == 0 and i % 2 == 0:
#         count1 += 1
#         # print(i ** 2)
#     if i % 7 == 0 and i % 2 == 1:
#         count2 += 1
#         # print(i)
# print(f'{count1} count of first type numbers')
# print(f'{count2} count of second type numbers')