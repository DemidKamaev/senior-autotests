# task 2.2.5.5

def num_not_multiple(num):
    if num % 3 != 0:
        return f"Число {num} не кратно 3."
    else:
        return f"Число {num} кратно 3."

num = int(input())
print(num_not_multiple(num))