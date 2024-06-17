
class Plant:
    adible = False # съедобность
    name = 'Растение'


class Animal:
    alive = True # живой
    fed = False # накормленный
    name = 'Животное'

    def eat(self, food):
        if food.adible:
            print(f'{self.name} съел {food.name}')
            fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            alive = False


class Mammal(Animal): # млекопитающее

    def __init__(self, name):
        self.name = name


class Predator(Animal): # хищник
    def __init__(self, name):
        self.name = name


class Flower(Plant):
    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    adible = True

    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
