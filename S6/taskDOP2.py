# Дан список, вывести отдельно буквы и цифры.

# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')



# inp = list(map(str, input('Введите список: ').split()))
# print([int(num) for num in filter(lambda num: num.isnumeric(), inp)])


a = ( "a", 'b', '2', '3' ,'c')

b = filter(str.isalpha, a)
c = filter(str.isdigit, a)

print(*b)
print(*c)
