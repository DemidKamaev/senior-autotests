# Задача 2.2.4

def convert_temp(F):
    temp_C = (F - 32) * 5 / 9
    return f'{F} градусов по Фаренгейту {round(temp_C, 2)} по Цельсию'

F = 100
print(convert_temp(F))