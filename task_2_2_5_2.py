# task 2.2.5.2

def get_last_num(num: int):
    get_num = num % 10
    return f"Последняя цифры числа {num}: {get_num}"


num = 1234
print(get_last_num(num))