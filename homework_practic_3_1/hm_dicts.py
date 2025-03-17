# 1. Частотный анализ строки

def char_frequency(s):
    # Создаем словарь
    n_dict = {}

    new_s = s.replace(" ", "")

    # Проходимся по элемента в строке* + условие проверка ключа в словаре
    for item in new_s:
        if item in n_dict:
            n_dict[item] += 1
        else:
            n_dict[item] = 1

    return n_dict

s = input("Введите текст: ")
result = char_frequency(s)
print(result)


# 2. Слияние двух словарей

def merge_dicts(dict_1, dict_2):
    for key, item in dict_2.items():
        if key in dict_1:
            dict_1[key] += item
        else:
            dict_1[key] = item

    return dict_1

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}
print(merge_dicts(dict_1, dict_2))

# 3. Обратное преобразование словаря в два списка

def dict_to_lists(my_dict):
    s_value = []
    s_key = []
    for key in my_dict.keys():
        s_key.append(key)

    for value in my_dict.values():
        s_value.append(value)

    return s_key, s_value

my_dict = {"a": 1, "b": 2, "c": 3}
res = (dict_to_lists(my_dict))
print(res)

# 4. Группировка элементов по первому символу

def group_by_first_letter(strings):
    m_dict = {}

    for elem in strings:
        first_char = elem[0]  # Получаем первую букву элемента
        if first_char not in m_dict:  # Инициализация списка, если ключа нет в словаре
            m_dict[first_char] = []
        m_dict[first_char].append(elem)  # Добавляем элемент в соответствующий список

    return m_dict

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))


# 5. Извлечение подсловаря

def extract_subdict(n_dict, keys):
    new_dict = {}

    for key in n_dict.keys():
        if key in keys:
            new_dict[key] = n_dict[key]  # Копируем существующие элементы

    return new_dict

n_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(n_dict, keys))