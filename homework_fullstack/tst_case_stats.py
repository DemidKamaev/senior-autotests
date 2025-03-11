# общее кол-во кейсов
# цикл 7 дней
# ввод кол-ва кейсов за один день

count = 0
days = 7
for i in range(1, days+1):
    temp = int(input(f"Введите выполненное количество тест кейсов за день {i}: "))
    count += temp
    i += 1

print(f"Общее количество тестов за неделю: {count}")
case_day = count / days
print(f"Среднее кол-во тестов в день: {round(case_day)}")

if case_day > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")


