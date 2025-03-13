# Функция принимает имя пользователя и выводит приветствие
def greet_uset(name):
    print(f"Привет, {name}! Добро пожаловать в мир Python!")

name = input('Введите имя: ')
greet_uset(name)

# Функция принимает 2 числа и возвращает их сумму
def caluclation_sum(a, b):
    return f"Сумма чисел: {a + b}"

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(caluclation_sum(a, b))

