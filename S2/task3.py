# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

string1 = 'qwe rty'
string2 = 'rty'
if len(string1) > len(string2):
    print(string1.count(string2))  
else:
     print(string2.count(string1))
