# Поработайте с переменными, создайте несколько, выведите на экран,
#  запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# Переменные variables
str_var = 'Строка'
int_var = 17  # integer целое число.
float_var = 19.5  # float плавающие.
list_var = [7, 5, 'text']
dict_var = {1: 'a', 2: 'b', 3: 'c'}  # Словарь.

# выведите на экран,
print(str_var)
print(int_var)
print(float_var)
print(list_var)
print(dict_var)

# запросите у пользователя несколько чисел и строк.
number_1 = int(input('Введите число '))
number_2 = int(input('Введите число '))
str_1 = input('Введите строку ')
str_2 = input('Введите строку ')

#  сохраните в переменные, выведите на экран.

print('Числа', {number_1}, {number_2}, 'Строки', {str_1}, {str_2})
