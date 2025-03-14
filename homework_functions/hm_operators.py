# 1. Оценка по шкале

# def check_grade(scope):
#     if scope < 50:
#         return f"Оценка за {scope} баллов: Неудовлетворительно."
#     elif 50 <= scope <= 74:
#         return f"Оценка за {scope} баллов: Удовлетворительно."
#     elif 75 <= scope <= 89:
#         return f"Оценка за {scope} баллов: Хорошо."
#     elif 90 <= scope <= 100:
#         return f"Оценка за {scope} баллов: Отлично."
#     else:
#         return f"Введите корректное значение от 0 до 100"
#
# scope = int(input("Введите оценку: "))
# print(check_grade(scope))


# 2. Четное или нечетное число

# def is_even(number):
#     if number % 2 == 0:
#         return f"Число {number} является чётным."
#     else:
#         return f"Число {number} является нечётным."
#
# number = int(input("Введите число: "))
# print(is_even(number))


# 3. Максимальное из двух чисел

# def find_max(a, b):
#     maximum = a
#     if a > b:
#         return f"Максимальное из чисел {a} и {b}: {maximum}"
#     else:
#         maximum = b
#         return f"Максимальное из чисел {a} и {b}: {maximum}"
#
# a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
# print(find_max(a, b))


# 4. Проверка числа на положительность и четность

# def check_number(number):
#     if number > 0:
#         if number % 2 == 0:
#             return f"Число {number} положительное и чётное."
#         else:
#             return f"Число {number} положительное и нечётное."
#     else:
#         return f"Число {number} отрицательное."
#
#
# number = int(input("Введите число: "))
# print(check_number(number))

# 5. Проверка длины строки

def check_string_length(string, length):
    ln = 0
    for i in range(len(string)):
        ln += 1

    if ln > length:
        return f"Длина строки достаточная"
    else:
        return f"Строка слишком короткая"

string = input("Введите строку: ")
length = int(input("Введите число: "))

result = check_string_length(string, length)
print(result)