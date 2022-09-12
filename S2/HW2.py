# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# from math import factorial
# n = int(input('Введите число N: '))
# faktorial = 1

# if n == 1 or n == 0:
#     print(f'Произведение числа {n} равен: 1')
# else: 
#     for i in range(2, n+1):
#         faktorial *= i
    
# print(f'Произведение чисел от 1 до {n} равен: {faktorial}')

num = int(input("Введите число : "))
a = 1
for i in range(1, num + 1):
    a *= i
    print(a, end=" ")
