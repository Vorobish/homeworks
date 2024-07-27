import threading


class BankAccount:

    def __init__(self):
        self.summ = 1000
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()

    def deposit(self, amount):
        with self.lock1:
            self.summ += amount
            print(f'Deposited {amount}, new balance is {self.summ}')

    def withdraw(self, amount):
        with self.lock2:
            self.summ -= amount
            print(f'Withdrew {amount}, new balance is {self.summ}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
