# task 2.2.5.4

def get_range(num):
    if 0 <= num <= 100:
        return f"Число {num} находится в пределах диапазона от 0 до 100."
    else:
        return f"Число {num} выходит за пределы диапазона от 0 до 100."


num = int(input())
print(get_range(num))