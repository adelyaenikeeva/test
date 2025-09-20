# numbers = [1, 2, 2, 3, 4, 5, 6, 6, 6]
# # 6. Подсчет уникальных элементов
# # Посчитать, сколько в списке уникальных элементов.
# # print(set(numbers))
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# # print(unique)
# # print(len(unique))
#
# # 2. Напишите программу, которая находит сумму и произведение всех элементов в списке.
# numbers = [1, 2, 2, 3, 4, 5, 6, 6, 6]
# summa = 0
# prod = 1
# for num in numbers:
#     summa += num
#     prod *= num
# # print(summa)
# # print(prod)
#
# # 3. Напишите программу, которая создает новый список, состоящий
# # только из четных чисел исходного списка
# numbers = [1, 2, 2, 3, 4, 5, 6, 6, 6]
# even_numbers = []
#
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)
# # print(even_numbers)
#
# # 8. Поменять местами min и max
# # В списке поменять местами минимальный и максимальный элементы.
# numbers = [2, 10, 13, 56, 2, 3, 4, -1]
# min_index = max_index = 0
#
# for i, num in enumerate(numbers):
#     if num < numbers[min_index]:
#         min_index = i
#     if num > numbers[max_index]:
#         max_index = i
#
# numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 51, 52]
# numbers = list(range(1, 101))
# print(numbers)

n = int(input('Введите кол-во элементов: '))
numbers = []
for i in range(n):
    num = int(input('Введите число: '))
    numbers.append(num)
print(numbers)

for num in numbers:
    if num > 50:
        print(num)
