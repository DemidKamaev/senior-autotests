def calculator():

    while True:
        try:
            # Ввод первого числа
            num_1 = int(input("Введите первое число: "))
            num_2 = int(input("Введите второе число: "))
            sign = input("Введите операцию (+, -, *, /): ")
            if sign not in ["+", "-", "*", "/"]:
                raise ValueError("Введите арифметическое число: ")


            if sign in "+":
                result = num_1 + num_2
            elif sign in "-":
                result = num_1 - num_2
            elif sign in "*":
                result = num_1 * num_2
            elif sign in "/":
                if num_2 == 0:
                    raise ZeroDivisionError("На ноль делить нельзя")
                result = num_1 / num_2
            print(f"Результат: {result}")

        except ValueError as ve:
            print(f"Ошибка ввода: {ve}")
        except ZeroDivisionError as zde:
            print(f"Ошибка: {zde}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")


calculator()