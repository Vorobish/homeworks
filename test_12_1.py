import module_12_1 as m
import unittest as u


class RunnerTest(u.TestCase):

    def test_walk(self):
        obj = m.Runner('Ann')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    def test_run(self):
        obj = m.Runner('Ann')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    def test_challenge(self):
        obj1 = m.Runner('Ann')
        obj2 = m.Runner('Mila')
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance)


if __name__ == '__main__':
    u.main()
