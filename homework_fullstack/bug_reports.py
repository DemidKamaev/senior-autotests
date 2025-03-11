# Работа со списком

# Исходный список ошибок
bug_list = ["Ошибка 1 — High", "Ошибка 2 — Low", "Ошибка 3 - Blocker", "Ошибка 4 - Critical", "Ошибка 5 - Middle"]

# Добавление элемента
bug_list.append("Ошибка 6 - High")

# Удаление элемента
for i in bug_list:
    if "Low" in i:
        bug_list.remove(i)

# Установить порядок приоритетов
order_list = {
    "Blocker": 1,
    "Critical": 2,
    "High": 3,
    "Middle": 4,
    "Low": 5
}

# Функция для извлечения приоритета из строки
def get_priority(bug):
    # Разделяем строку по символам и извлекаем приоритет (крайнее слово в списке)
    priority = bug.split()[-1]
    return order_list.get(priority)  # Если приоритета нет, присваиваем высокий приоритет

# Сортируем список с использованием функции get_priority
sort_bugs = sorted(bug_list, key=get_priority)

print(sort_bugs)

