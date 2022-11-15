# Problem1
# list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# def half_reverse(arr: list) -> list:
#     list_a = []
#     list_b = []
#     for i in range(len(arr) // 2):
#         list_a.append(arr[i])
#         list_b.append(arr[len(arr) - 1 - i])
#     list_a.reverse()    
#     for i in range(len(list_a)):
#         arr[i] = list_a[i]
#     for i in range(len(list_b)):
#         arr[len(arr) - 1 - i] = list_b[len(list_b) - 1 -i]
#     return arr
# print(half_reverse(list1))


# Problem2
# def fibonacci(a):
#     total = 0
#     list_fib = [0, 1]
#     for i in range(a-2):
#         list_fib.append(list_fib[i] + list_fib[i + 1])
#     total = sum(list_fib)
#     return total
# print(fibonacci(100))

# Problem3
# def add_numbers(n1: int, n2: int) -> int:
#     sum = n1 + n2
#     return sum
# def diff_numbers(n1: int, n2: int) -> int:
#     diff = n1 - n2
#     return diff
# def main():
#     num1 = int(input('input first number: '))
#     num2 = int(input('input second number: '))
#     command = input('sum / diff / exit: ')
#     if command == 'sum':
#         print(add_numbers(num1, num2))
#     elif command == 'diff':
#         print(diff_numbers(num1, num2))
#     elif command == 'exit':
#         exit()
#     else: 
#         return  NameError
# while True:
#     main()



# Problem4
# file_name = input('write name to file: ')
# def create_file(f_name: str) -> str:
#     f = open(f_name,'w')
#     return f
# f_create = create_file(file_name)
# f_create


# Problem5
# from random import choice as c
# possible_digits = '145790'
# tel_number = '0444'
# def gen_number(tel_number_: str, possible_digits_: str) -> str:
#     for i in range(6):
#         tel_number_ += c(possible_digits_)
#     return tel_number_

# print(gen_number(tel_number, possible_digits))
