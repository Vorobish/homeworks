import threading
import queue
from time import sleep


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):

    def __init__(self, table, customer):
        super().__init__()
        self.table = table
        self.customer = customer


    def run(self):
        print(f'{self.customer} сел за стол {self.table.number}')
        sleep(5)
        print(f'{self.customer} покушал и ушёл')
        self.table.is_busy = False


class Cafe:
    customers = []

    def __init__(self, tables):
        self.q = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        threads = []
        for i in range(1, 21):
            customer = f'Посетитель номер {i}'
            print(f'{customer} прибыл')
            serve = threading.Thread(target=self.serve_customer, args=(customer, ))
            serve.start()
            threads.append(serve)
            sleep(1)

        for thread in threads:
            thread.join()

    def serve_customer(self, customer):

        threads = []
        Cafe.customers.append(customer)
        self.q.put(customer)
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                next = self.q.get()
                customer_thread = Customer(table, next)
                Cafe.customers.remove(next)
                customer_thread.start()
                threads.append(customer_thread)
                break
        else:
            print(f'{customer} ожидает свободный стол')

        for thread in threads:
            thread.join()

        while Cafe.customers:
            for table in self.tables:
                if not table.is_busy:
                    table.is_busy = True
                    next = self.q.get()
                    customer_thread = Customer(table, next)
                    Cafe.customers.remove(next)
                    customer_thread.start()
                    threads.append(customer_thread)
                    break
            sleep(1)

        for thread in threads:
            thread.join()


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)
#
# # Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()
