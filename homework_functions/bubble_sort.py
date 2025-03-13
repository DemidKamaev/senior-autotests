# Реализовывать простые алгоритмы сортировки

nums = input("Введите числа через запятую: ").split(", ")

# преобразовать элементов с типом str в int
num_list = []
for i in nums:
    num_list.append(int(i))

n = len(num_list)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

print(f'Отсортированный список: {num_list}')
