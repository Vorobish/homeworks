class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

obj1 = Runner('Ann')
obj2 = Runner('Mila')
for i in range(10):
    obj1.walk()
    obj2.run()

print(obj1.distance, obj2.distance)


