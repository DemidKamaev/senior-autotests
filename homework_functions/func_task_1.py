# 1. Плоащадь треугольника

# def rectange_area(a, b):
#     c = a * b
#     return f"Площадь треугольника с длиной {a} и шириной {b} равна {c}."
#
# a = int(input("Введите длину: "))
# b = int(input("Введите ширину: "))
# print(rectange_area(a, b))


# 2. Перевод времени из секунд в часы и минуты

# def convert_seconds(s):
#     hours = s // 3600
#     minutes = round((s % 3600) // 60)
#     return (hours, minutes)
#
# s = 3672
# results = convert_seconds(s)
#
# print(f"В {s} секундах содержит {results[0]} час(ов) и {results[1]} минут(ы).")

# 3. Функция с аргументом по умолчанию

def power_of(num, exp=2):
    # Результат возведения в степень
    res = num**exp

    # Формируем вывод в зависимости от значения exp
    if exp == 2:
        print(f"Число {num} в степени {exp} равно {res}.")
    else:
        print(f"Число {num} в степени {exp} равно {res}.")

    return res

res_1 = power_of(3, 4)
res_2 = power_of(5)

# 4. Подсчёт элементов
def count_items(*args):
    a = len(args)
    return f"Количество переданных элементов: {a}"

print(count_items(1, 2, 3, 4, 5))
print(count_items("apple", "banana", "cherry"))