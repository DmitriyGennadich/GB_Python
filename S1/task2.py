# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


a = int(input('введите кол-во чисел для сравнения - '))
numbers = []
for i in range(a):
    numbers.append(int(input()))
# print(max(numbers))
x = numbers[0]
for i in range(len(numbers)):
    if x < numbers[i]:
        x = numbers[i]
print(x)
