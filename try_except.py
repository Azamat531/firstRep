# Problem1.1
# a = [5,6.17,True,'false',('abs',4.56),[4,5,'era']]
# b = []
# for i in a:
#     try:
#         set(i)
#         b.append(True)
#     except:
#         b.append(False)
# print(all(b))


# Problem1.2
# set1 = set()
# for i in range(5):
#     a = int(input('input: '))
#     set1.add(a)
# print(min(set1))


# Problem1.3
# try:
#     a = eval(input('input function: '))
#     print(a)
# except:
#     print('Error!')


# Problem1.4
# a = int(input('input number: '))
# while a < 50000:
#     a = int(input('input number: '))
# print(round(a*3.47/100+a,2))


# Problem2.1
# try:
#     a = input('input: ')
# except(TypeError,IndexError,NameError):
#     print('error')


# Problem2.2
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# try:
#     values[1] + values[17]
# except(IndexError):
#     print('out of index')
# except(TypeError):
#     print('type error')


# Problem2.3 ????????????
# lst = []
# for i in range(10):
#     lst.append(i)
# a = list(reversed(lst))
# sls_obj = slice(0,8)
# print(a[sls_obj])


# Problem2.4 ???????????
# a = 0
# b = 1
# numbers = []
# while b > a:
#     numbers.append(b)
#     b += 1
# print(numbers)

# Problem3
# dict_ = {'name': 'john', 'lastname': 'snow', 12: 'age'}
# for x in dict_.keys():
#     try:
#         x + 'abc'
#     except(TypeError):
#         print('Type error')