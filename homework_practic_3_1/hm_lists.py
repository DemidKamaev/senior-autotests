# 1. Удаление дубликатов

def remove_duplicates(lst):
    new_lst = []
    for num in lst:
        if num not in new_lst:
            new_lst.append(num)

    # new_lst = set(lst)  # вывод {1, 2, 3, 4}
    return new_lst

lst = [1, 2, 2, 3, 4, 4]
print(remove_duplicates(lst))

# 2. Генерация списка квадратов

def generate_squares(n):
    result = [num**2 for num in range(1, n+1)]
    return result

n = int(input("Введите числи: "))
res = generate_squares(n)
print(res)

# 3. Объединение двух списков

def merge_lists(lst_1, lst_2):
    # Конкатенация строк + метод set для удаления дублей
    merge_lst = set(lst_1 + lst_2)

    # Из множества {} перенести элементы в список
    new_lst = []
    for num in merge_lst:
        new_lst.append(num)
    return new_lst

list_1 = [1, 2, 3]
list_2 = [3, 4, 5]
print(merge_lists(list_1, list_2))


# 4. Проверка на отсортированность

def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False

lst = [5, 2, 3, 4, 1]
print(is_sorted(lst))

# 5. Слияние списков

def merge_lists(list_1, list_2):
    # Перебрать индексы всей длины одного списка и сложить элементы 1-ого и 2-ого списка
    new_lst = [list_1[i] + list_2[i] for i in range(len(list_1))]
    return new_lst

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
result = merge_lists(lst_1, lst_2)
print(result)