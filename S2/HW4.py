# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


# from random import randint
# n = int(input('Введите число N - '))
# numbers = []
# for i in range(n):
#     numbers.append(randint(-n, n+1))
# print(numbers)

# f = open('file.txt', 'w')
# while True:
#     s = input('Укажите позицию для вычисления - ')
#     if s == "":
#         break
#     f.write(s+"\n")
# f.close()

# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)


######## 


import random

N = int(input("Введите размер списка: ")) 
a = []

for i in range(N):  
    new_element = random.randint(-N, N)
    a.append(new_element)
print(f'Ваш список: {a}')

num = 1
with open('file.txt') as file:
    for pos in file:
        if int(pos) < N:
            num *= a[int(pos)]
        # else: num *= 1
print(num)

