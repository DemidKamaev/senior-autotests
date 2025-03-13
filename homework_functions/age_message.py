# Вывод сообщения в зависимости от возраста
def get_age(age, now_age):
    age_current = now_age - age
    print(f"Ваш возраст: {age_current}")
    if age_current < 18:
        print("Вы еще молоды, учеба - ваш путь!")
    elif 18 <= age_current <= 65:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")

now_age = 2025
age = int(input("Введите год вашего рождения: "))
get_age(age, now_age)
