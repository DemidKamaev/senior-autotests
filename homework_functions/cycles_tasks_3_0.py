# 1. Сумма чисел от 1 до N

# def sum_numbers(n):
#     count = 0
#     for num in range(1, n+1):
#         count += num
#
#     return f"Сумма чисел от 1 до {n}: {count}"
#
# n = int(input("Введите число: "))
# print(sum_numbers(n))

# 2. Поиск минимального числа в списке

# def get_min(numbers):
#     # Проверка, что список не пустой
#     if not numbers:
#         return None
#
#     # Устанавливаем первое число как минимальное
#     num_min = numbers[0]
#     for num in numbers:
#         if num < num_min:
#             num_min = num
#
#     return num_min
#
# numbers = [3, 1, 5, 1, 8]
# result = get_min(numbers)
# print(f"Минимальное число в списке {numbers}: {result}")

# 3. Подсчет гласных букв

# def count_vowels(string):
#     lst = ["a", "e", "i", "o", "u", "y"]
#     count = 0
#     # lst_char = []
#     for char in string:  # Проход по элемента в списке(без сплита)
#         if char in lst:  # Если элемент равен одну из списка глассных
#             count += 1
#             # lst_char.append(char)
#     return count
#
# string = input("Введите текст: ")
# res = count_vowels(string)
# print(f"Количество глассных в строке {string}: {res}")


# 4. Ромбовидный треугольник

def print_diamond(rows):
    # Диапазон вывода до середины включая
    for num in range(1, rows//2+2):  # to 0 from 4
        print('*' * num, sep="\n")

    for num in range(rows//2+2, rows+1):  # to 5 from 7
        print('*' * (rows-num+1), sep="\n")
    # Диапазон вывода от середины не включая до конца


rows = int(input("Введите кол-во строк: "))
print_diamond(rows)

# 5. Обратный отсчёт

def countdown():
    for num in range(10, 0, -1):
        print(num)
    print("Старт!")

countdown()

# 6. Обратный отсчёт - 2

def count_down():
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Старт!")

countdown()