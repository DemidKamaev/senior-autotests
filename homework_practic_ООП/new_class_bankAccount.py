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
            raise ValueError

    def withdraw(self, amount):
        """Метод для снятия со счета"""
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'С баланса снято: {amount}')
        else:
            raise ValueError

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
        super().withdraw(amount)   # Вызываем метод withdraw из родительского класса


user_1 = SavingsAccount("Demid", 0.05, 500)  # Предоставлять начальный баланс
user_1.deposit(500)
user_1.withdraw(100)
user_1.apply_interest()

# После внесенных правок ваш код должен работать корректно.
# Метод apply_interest теперь правильно использует баланс со счета,
# а метод withdraw для CheckingAccount правильно вызывает родительский метод.

