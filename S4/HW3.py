#Задайте последовательность чисел. Напишите программу, которая выведет 
#список неповторяющихся элементов исходной последовательности.

print('Введите числа:', end=' ')
numbers = [int(i) for i in input().split()]

def find_unique_number(numbers):
    result = []
    for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i != j and numbers[i] == numbers[j]:
                    break
            else:
                result.append(numbers[i]) 
    return result   
        
print(f'Cписок неповторяющихся элементов исходной последовательности: {find_unique_number(numbers)}')