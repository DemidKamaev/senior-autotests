# Данные о баге-репорте

info_bug = {
    "id": 145,
    "name": "Не приходят данные по среднему заработку",
    "status": "in progress"
}

# Изменение статуса в баг-репорте

info_status = ["create", "in progress", "in tests", "analyst_demo", "closed"]

# При выборе элемента в списке info_status, значение status изменяется в словаре info_bug
def get_status(text):
    for key in info_bug:
        if "status" in key:
            info_bug[key] = text

text = input("Введите текст равный статусу по задачи: ")
get_status(text)
print(info_bug)

