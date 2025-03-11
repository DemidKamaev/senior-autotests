# Хранение данных

# 1
# name = input("Введите имя: ")
# job = input("На какой должности в трудитесь? ")
# name_tool = input("Любимый инструмент для тестирования: ")
#
# name = input("Введите другое имя, если вы хотите изменить данные: ")
# if not name:
#     print("Имя не указано. Введите снова")
#     name = input("Введите имя снова: ")
# else:
#     print(f'Ваше имя: {name}')
#
# if not name_tool:
#     print("Инструмент не указан. Попробуйте снова")
#     name_tool = input("Любимый инструмент для тестирования: ")
# else:
#     print(f"Ваш любимый инструмент {name_tool}. Отличный выбор!")
#
# print(job)


# Обработка внесения данных

def get_input(prompt):
    """Обработка пустых значений при внесении данных пользователем"""
    info = input(prompt).strip()
    if not info:
        print("Ошибка! Внесены пустые данные в поле. Попробуйте снова.")
        return None
    return info

# Инициализация переменных

user_name = ""
prof_name = ""
tool_name = ""

# Проверка наличия данных в переменных

while not user_name:
    user_name = get_input("Введите ваше имя: ")

while not prof_name:
    prof_name = get_input("Введите вашу должность: ")

while not tool_name:
    tool_name = get_input("Ваша любимый инстурмент для тестирования: ")

# Вывод данных
print("Ваши данные")
print(f"Имя пользователя: {user_name}")
print(f"Профессия: {prof_name}")
print(f"Инструмент для тестирования: {tool_name}")