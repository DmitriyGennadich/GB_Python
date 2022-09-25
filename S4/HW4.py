# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

n = int(input(f'Задайте степень числа k:\n'))
koeff = [randint(0, 100) for i in range(n+1)]
print(koeff)

if n != 0:
    def make(n):
        result = []
        for i in range(n):
            if koeff[i] > 1:
                if n - i > 1:
                    result.append(f'{str(koeff[i])}x**{n - i}')
                elif n - i == 1:
                    result.append(f'{str(koeff[i])}x')
            elif koeff[i] == 1:
                if n - i > 1:
                    result.append(f'x**{n - i})')
                elif n - 1 == 1:
                    result.append('x')
        if koeff[-1] != 0:
                result.append(str(koeff[-1]))   
        return ' + '.join(result) + ' = 0' 
    print(make(n))  
else:   
    print(f'n должно быть больше нуля, иначе не многочлен')

f = open('HW4.txt', 'w')
f.write(make(n))
f.close()