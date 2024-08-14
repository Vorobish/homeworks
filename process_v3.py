import multiprocessing as mp


class WarehouseManager:

    def __init__(self):
        self.data = {}


    def process_request(self, list_):
        for tuple_ in list_:
            product = tuple_[0]
            action = tuple_[1]
            k = tuple_[2]
            if action == 'receipt':
                if product in self.data:
                    self.data[product] += k
                else:
                    self.data[product] = k
            elif product in self.data and self.data[product] >= k:
                self.data[product] -= k

    def run(self, requests):
        if __name__ == '__main__':
            self.data = mp.Manager().dict()

            requests_process = mp.Process(target=self.process_request, args=(requests, ))
            requests_process.start()
            requests_process.join()


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)
