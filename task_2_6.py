# Задача 1. добавление элемента в список

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# Задача 2. Удаление элемента из списка

fruits = ["Москва", "Лондон", "Париж"]
fruits.remove("Лондон")
print(fruits)

# Задача 3. Доступ элемента по индексу

cities = ["Москва", "Питер", "Новосибирск", "Екатеринбург"]
elem = cities[2]
print(elem)

# Задача 4. Доступ к элементу по срезу списка

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_nums = nums[3:7]
print(new_nums)

# Задача 5. Изменение элемента списка

colors = ["red", "green", "blue"]
colors[1] = "yellow"
print(colors)

# Задача 6. Узнаем длину списка

animals = ["dog", "cat", "rabbit", "hamster"]
print(f"Длина списка равна: {len(animals)}")
print()

# Задача 7. Добавление элемента в словарь

student = {"name": "Ivan", "age": 20}
student.setdefault("grade", "A")
print(student)
print()

# Задача 8. Изменение элемента словаря

students = {"name": "Ivan", "age": 20, "grade": "B"}
students['grade'] = "A"
print(students)
print()

# Задача 9. Удаление элемента из словаря

studs = {"name": "Ivan", "age": 20, "grade": "A"}
# age = studs.pop('age')  # удаляем элемент по ключу age, возвращая его значение
# print(age)

del studs['age']
print(studs)
print()

# Задача 10. Доступ к элементу словаря по ключу

studs_10 = {"name": "Ivan", "age": 20, "grade": "A"}
# name = studs_10.get("name")
# print(name)
print(f"Имя стундента: {studs_10["name"]}")

# Задача 11. Проверка наличия ключа в словаре

studs_11 = {"name": "Ivan", "age": 20, "grade": "A"}
if "grade" in studs_11:
    print(f"Ключ 'grade' найден в словаре.")
else:
    print(f"Ключ 'grade' НЕ найден в словаре.")

# Задача 12. Изменение элемента во вложенном словаре

student_12 = {"name": "Ivan", "address": {"city": "Moscow", "street": "Lenina"}}
student_12["address"]["city"] = "Saint-Petersburg"
print(student_12)

# Задача 13. Изменение элемента в списке, находящимся в словаре

student_13 = {"name": "Maria", "grades": [75, 82, 90]}
student_13["grades"][0] = 85
print(student_13)

# Задача 14. Изменение элемента в словаре, находящимся внутри списка

stds_14 = [{"name": "Ivan", "age": 20}, {"name": "Petya", "age": 22}]
stds_14[1]["age"] = 23
print(stds_14)

# Задача 15. Проверка наличия элементов и определение длины кортежа

def get_info(colors_15):
    if "green" in colors_15:
        print(f"Наличие 'green': True. Длина кортежа: {len(colors_15)}")
    else:
        print(f"Элемента 'green' НЕ найдено в кортеже.")

colors_15 = ("red", "green", "blue")
get_info(colors_15)

