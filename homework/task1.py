# 17.	Напишите программу, которая находит факториал числа,
# введенного пользователем, используя цикл while.
number = int(input('Введите число = '))
i = 1
factorial = 1

while i <= number:
    factorial *= i
    i += 1

print('Факториал = ', factorial)