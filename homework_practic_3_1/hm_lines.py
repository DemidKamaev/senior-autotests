# 1. Анаграмма

# def is_anagram(s1, s2):
#     # Убираем пробелы в строках
#     s1 = s1.replace(" ", "")
#     s2 = s2.replace(" ", "")
#
#     # Сравниваем отсортированные символы
#     return sorted(s1) == sorted(s2)
#
#
# s1 = input("Введите первую строку: ").lower()
# s2 = input("Введите вторую строку: ").lower()
# print(is_anagram(s1, s2))

# 2. Палиндром

# def is_palindrome(s):
#     new_lst = []
#     for i in s:
#         new_lst.append(i)
#
#     for i in new_lst:
#         if i[0] == i[-1]:
#             new_lst.pop(0)
#             new_lst.pop(-1)
#             continue
#         else:
#             return False
#
#     return True
#
# s = (input("Введите число больше 3 символов: "))
# print(is_palindrome(s))

# 3. Самое длинное слово

def longest_word(s):
    new_lst = s.split()  # Разбить текст на отдельные строки(слова)
    maximum = ''
    for word in new_lst:
        # Убираем знаки препинания
        clear_word = ''.join(char for char in word if char.isalnum())
        if len(clear_word) > len(maximum):  # сравниваем длину слова с длиной слова в переменной макс
            maximum = word
    return maximum

s = "In the middle of a vast desert, an extraordinary adventure awaits"
print(longest_word(s))


# 4. Формирование номера телефона

# def format_phone_number(digits):
#     part_1 = digits[0:3]
#     part_2 = digits[3:6]
#     part_3 = digits[6:]
#     print(f"({part_1}) {part_2}-{part_3}")
#
# digits = input("Введите номер телефона: ")
# format_phone_number(digits)

# 5. Удаление дублирующих символов

# def remove_duplicates(s):
#     new_lst = []
#     for elem in s:
#         if elem not in new_lst:
#             new_lst.append(elem)
#     print(''.join(new_lst))
#
# s = "programming"
# remove_duplicates(s)

# 6. Проверка на уникальность символов

def is_inuque(s):
    new_lst = set(s)
    if len(s) == len(new_lst):
        return True
    else:
        return False

s = input('Введите строку: ')
print(is_inuque(s))
