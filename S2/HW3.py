# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число N: '))
numbers = {i:(1 + 1 / i) ** i for i in range(1, n+1)}
print(f'Последовательность чисел:{numbers}')
summa = 0
for i in numbers:
    summa += round(numbers[i], 3)
print(f'Сумма цифр последовательности равна:{summa}') 
