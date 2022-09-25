# Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел,
# делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.


from random import randint

list1 = [i for i in range(10, 100)]
list2 = list(filter(lambda x: x % 9 == 0, list1))
list3 = sum(list(map(lambda x: x**2, list2)))

print(list1)
print()
print(list2)
print()
print(list3)


print(sum(map(lambda x: x**2, list(filter((lambda x: x % 9 == 0), list(range(10, 100)))))))
