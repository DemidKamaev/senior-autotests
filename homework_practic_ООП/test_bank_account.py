import pytest
from new_class_bankAccount import BankAccount

# Тест положительно депозита
def test_deposit_positive_amount():
    user_1 = BankAccount("Demid", 500)
    init_balance = user_1.get_balance()
    user_1.deposit(100)  # Пополнение счета
    assert user_1.get_balance() == init_balance + 100, "Баланс должен увеличиться на сумме депозита"

# Тест отрицательного депозита
def test_deposit_negative_amount():
    user_1 = BankAccount("Demid", 500)
    init_balance = user_1.get_balance()

    with pytest.raises(ValueError):  # Проверка на вызов исключения
        user_1.deposit(-100)

    assert user_1.get_balance() == init_balance, "Баланс не должен измениться при отрицательном депозите"

# Тест депозита нуля
def test_deposit_zero_amount():
    user_1 = BankAccount("Demid", 500)
    init_balance = user_1.get_balance()

    with pytest.raises(ValueError):  # Проверка на вызов исключения
        user_1.deposit(0)

    assert user_1.get_balance() == init_balance, "Баланс не должен измениться при депозите нуля"