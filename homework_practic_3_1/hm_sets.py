# 1. Уникальные элементы списка

def get_unique_elements(lst):
    my_set = set(lst)
    new_lst = []
    for i in my_set:
        new_lst.append(i)
    return new_lst

lst = [1, 2, 2, 3, 4, 4, 4, 5]
print(get_unique_elements(lst))

# 2. Проверка списка на уникальность элементов

def is_unique_list(lst):
    lenght_lst = len(lst)
    my_set = set(lst)
    if lenght_lst == len(my_set):
        return True
    else:
        return False

lst = [1, 2, 2, 3]
print(is_unique_list(lst))

# 3. Получение уникальных гласных из строки

def get_unique_vowels(s):
    chars = ['a', 'e', 'i', 'o', 'u']
    my_set = set()
    for elem in s:
        if elem in chars:
            my_set.add(elem)

    return my_set

s = input("Введите текст: ").lower()
print(get_unique_vowels(s))