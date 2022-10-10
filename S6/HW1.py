#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# было
# num = int(input("Введите число : "))
# a = 1
# for i in range(1, num + 1):
#     a *= i
#     print(a, end=" ")   


# стало
def faktorial():

    factorial = lambda f : f * factorial(f-1) if f > 0 else 1
    print("Факториал заданного числа равен:", factorial(int(input('Введите число N:\t'))))

faktorial()