#Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки

# было
# n = int(input('Введите число: '))
# lst = [round((1 + 1 / i) ** i, 5) for i in range(1, n + 1)]
# print(f'Список: {lst}')
# print(f'Сумма чисел списка: {round(sum(lst), 5)}')


#стало
n = int(input('Введите число N: '))
fc = lambda x: (1 + 1 / x) ** x
numbers = [fc(x) for x in range (1, n + 1)]
print(round(sum(numbers), 3))