# Problem0
# a = [7,8,8,4,8,4,8,4,8,4,8,4,8]
# print(sum(a)) 


# Problem1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i > 5:
#         print(i)


# Problem2
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# for i in digits:
#     print(i / 9)


# Problem3
# fruits = ('banana','stawberry','apple','orange','limon','ananas')
# print(fruits[0])
# print(fruits[len(fruits) - 1])


# Problem4
# spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# for i in spisok_2:
#     if i not in spisok_1:
#         print(i)


# Problem5
# for i in range(1, 300 + 1):
#     if i % 2 == 0:
#         print(i)
#     if i == 237:
#         exit()


# Problem6
# from random import randint
# rnd = randint(1,5)
# count = 0
# while True:
#     num = int(input('input number 1-5: '))
#     count += 1
#     if num == rnd:
#         print('you won')
#         exit()
#     elif count == 3:
#         print('you lose')
#         print(f'true number was - {rnd}')
#         exit()


# Problem7
# snt = input('input sentense: ')
# my_list = snt.split()
# list_1 = []
# list_2 = []
# for i in range(len(my_list)):
#     if i < len(my_list) / 2:
#         list_1.append(my_list[i])
#     else:
#         list_2.append(my_list[i])
# list_2.extend(list_1)
# print(list_2)


# while True:
#     count = 1
#     list_1 = []
#     list_2 = []
#     snt = input('input sentense: ')
#     for i in snt:
#         if i == ' ':
#             count += 1
#     if count >=6:


# Problem8
# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# def a(my_list):
#     even = 0
#     odd = 0
#     for i in my_list:
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd +=1
#     return f'odd - {odd},  even - {even}'
# print(a(numbers))


# Problem9
# numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
# my_list = []
# for i in numbers:
#     if i < 0:
#         my_list.append(-1)
#     elif i > 0:
#         my_list.append(1)
#     else:
#         my_list.append(0)
# print(my_list)


# Problem10
# my_list = [2,4,6,8,10,1,3,5,7,9,11,13,17]
# for i in range(0,len(my_list),2):
#     print(my_list[i])


# Problem11
# numbers = [1,0,-2,4,3,6,6,3,5,8,4,2] 
# for i in range(1,len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         print(numbers[i])


# Problem12
# a = 175315354518498331
# count = 0
# while a > 0:
#     if a % 10 == 3:
#         count +=1
#     a = a // 10
# print(count)


# Problem13
# print('27 ** 3')
# print('3 * 19683')
# print('7 + 5')
# print('12 * 56')
# print('672 / 59049')
# print('(7 + 5) * 56 / (3 * (27**3))')


# Problem14
# modified = '''исследователи ESET с()()бщили чт() в наст()ящее время активн()сть 
# xDSpy прекратилась и пр()из()шл() эт() п()сле предупреждения ()публик()ванн()г() 
# бел()русским cert в феврале текущег() г()да! П() сути/ т()гда эксперты 
# ()бнаружили ()дну из вред()н()сных кампаний хакер()в к()т()рая и была детальн() 
# ()писана в д()кументе! именн() инф()рмация бел()русск()г() cert стала 
# ()тправн()й т()чк()й для начала расслед()вания eset и п()м()гла аналитикам 
# ()бнаружить пр()шлые ()перации XDSpy!'''
# original = modified.replace('()','o')
# print(original)


# Problem15
# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# if sum(list_1) > sum(list_2):
#     print(list_1)
# elif sum(list_2) > sum(list_1):
#     print(list_2)
# else:
#     print('draw')


# Problem16
# y_friends = {
# "Joomart": "+996555246810", 
# "Adinai": "+996555013579",
# "Ermek": "+996777013579",
# "Atai": "+996777246810",
# "Aslan": "+996999246810",}
# his_her_friends = {
# "Lyazat": "+996551123456",
# "Salavat": "+996552234567",
# "Daniyar": "+996553345678",
# "Bolot": "+996554456789",
# "Alymbek": "+996555501234",
# "Dastan": "+996556678912",
# "Maksat": "+996557789012",
# "Aibek": "+996558890123",
# }
# dict_3 = {**y_friends, **his_her_friends}
# print(dict_3)


# Problem17
# a = input('input: ')
# list_1 = ''
# list_2 = ''
# for i in range(len(a)):
#     if i < len(a) / 2:
#         list_1 += a[i]
#     else:
#         list_2 += a[i]
# list_1 = list_1.upper()
# result = list_1 + list_2
# print(result)


# Problem18
# a = input('input numbers: ')
# my_list = a.split()
# new_list = []
# b = int(input('input number: '))
# for i in range(len(my_list)):
#     new_list.append(my_list[i -b])
# print(my_list)
# print(new_list)


# Problem19
# d = {'1': 'kyrgyzstan', '2': 'kazahstan'}
# a = input('')
# # for i in d.keys():
# #     if i == a:
# #         print(d)
# if a in d.keys():
#     print(d[a])
# if a in d.values():
#     key_list = list(d.keys())
#     val_list = list(d.values())
#     pos = val_list.index(a)
#     print(key_list[pos])


# Problem20
# Напишите задания для этого кода

# a = [1, 1, 2, 3,13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# b = a.count(13) * 100 / len(a)

# if b == 70.0:
#         print('совпадение? не думаю')
# if b < 70.0:
#         print('неужели')
# if b > 70.0:
#         print('я так и знал')
# Есть список 
#a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 
#13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
#1.Добавьте в список ещё одну цифру 13
#2.Узнайте сколько раз встречается цифра 13
#3.узнайте длину списка а
#4.узнайте сколько процентов списка занимает цифра 13 формула (количество цифры 13 * 100 / длина списка)
#Если процент будет меньше 70% вывести: НЕУЖЕЛИ
#Если будет больше 70% вывести: Я ТАК И ЗНАЛ
#Если равен 70% вывести : СОВПАДЕНИЕ ? НЕ ДУМАЮ


# Problem21
# height = int(input('height: '))
# width = int(input('width: '))
# print(f'perimeter - {2 * (height + width)}')
# print(f'area {height * width}')


# Problem22
# distance = int(input('distance in km: '))
# speed = int(input('speed in km/h: '))
# print(f'{distance / speed} hours')

# x / 2022 * 100,2)
# num = int(input('input number: '))
# print(a(num))
# Problem23
# a = lambda x: round(x / 2022 * 100,2)
# num = int(input('input number: '))
# print(a(num))