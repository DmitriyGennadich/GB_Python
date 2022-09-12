# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите число N: '))
# numbers = {i:(1 + 1 / i) ** i for i in range(1, n+1)}
# print(f'Последовательность чисел:{numbers}')
# summa = 0
# for i in numbers:
#     summa += round(numbers[i], 2)
# print(f'Сумма цифр последовательности равна:{summa}') 



n = int(input('Введите число: '))
lst = [round((1 + 1 / i) ** i, 5) for i in range(1, n + 1)]
print(f'Список: {lst}')
print(f'Сумма чисел списка: {round(sum(lst), 5)}')
    # except ValueError:
    # print('Вводить необходимо только целое число')
