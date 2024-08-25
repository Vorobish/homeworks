import module_12_4 as m
import unittest as u
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='UTF-8',
                    format="%(asctime)s / %(levelname)s / %(message)s")

class RunnerTest(u.TestCase):
    is_frozen = False

    @u.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            obj = m.Runner('Ann', -5)
            for i in range(10):
                obj.walk()
            self.assertEqual(obj.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @u.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            obj = m.Runner(50, 7)
            for i in range(10):
                obj.run()
            self.assertEqual(obj.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err2:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @u.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj1 = m.Runner('Ann', 5)
        obj2 = m.Runner('Mila', 10)
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance)


if __name__ == '__main__':
    u.main()

