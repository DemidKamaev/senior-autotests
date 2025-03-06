# task 2.2.5.3

def get_num(num):
    if num > 0 and num % 2 == 0:
        return f"Число {num} является положительным и четным"
    else:
        return f"Число {num} не подходит под условия"


num = int(input())
print(get_num(num))