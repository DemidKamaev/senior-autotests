class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Приватный атрибут, недоступный напрямую

    def deposit(self, amount):
        """Метод для пополнения счета"""
        if amount > 0:
            self.__balance += amount
            print(f"Баланс пополнен на: {amount}")
        else:
            raise ValueError("Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        """Метод для снятия со счета"""
        if self.__balance >= amount:
            self.__balance -= amount
            return f'С баланса снято: {amount}'
        else:
            raise ValueError("Недостаточно средст на счете")

    def get_balance(self):
        """Метод для получение текущего баланса"""
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, interest_rate=0.05, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate  # Атрибут процентная ставка

    def apply_interest(self):
        """Метод начисляет проценты на остаток по счету"""
        interest_amount = self.get_balance() * self.interest_rate
        # Используем get_balance для получения баланса, тк self.__balance является приватным атрибутом в родительском классе
        print(f"Сумма процента на остаток: {interest_amount}")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        """Переопределение метода withdraw(self, amount)"""
        # Убираем проверку на наличие средств на счете
        if amount > 0:
            self._BankAccount__balance -= amount  # Изменение приватного атрибута
            return f'С баланса снято: {amount}'
        else:
            raise ValueError("Сумма снятия должна быть положительная")


user_1 = SavingsAccount("Demid", 0.05, 500)  # Предоставлять начальный баланс
user_1.deposit(500)

try:
    user_1.withdraw(1000)  # Попытка снять 1000
except ValueError as ve:
    print(ve)
user_1.apply_interest()

user_2 = CheckingAccount("Ivan", 0)
user_2.deposit(1000)
user_2.withdraw(1500)  # Снятие средств, даже если баланс будет отрицательным
print(user_2.get_balance())



