# a = [1, 2, -3, -2, -1, -1]
# ls = [1, 3, 5, -1, 2, -1, -7, 0, -4, -3, -1, -4, -4, 1]
# def test(a):
#     sum1 = 0
#     result = []
#     for i in range(len(a)-1)

# cats = [('Мартин', 5, 'Алексей', 'Егоров'),
#         ('Фродо', 3, 'Анна', 'Самохина'),
#         ('Ваня', 4, 'Андрей', 'Белов'),
#         ('Муся', 777, 'Игорь', 'Бероев'),
#         ('Изольда', 2, 'Игорь', 'Бероев')]
# a = {}
# for i in cats:
#     name = i[0] + ', ' + str(i[1])
#     a.setdefault(i[2:], []).append(name)
# for i in a.items():
#     print(i)
# my_dict = {}
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
# biggest_dict(a=5, b=10, c=10)
# print(my_dict)
from random import *
class Warrior:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    def attack(self, warrior):
        warrior.health -= self.damage
        print(f'{self.name} ударил {warrior.name}, и у него осталось {warrior.health}')

TV_man = Warrior('TV', 100, randint(30, 50))
g_man_toilet = Warrior('G-man', 100, randint(30, 50))
while True:
    if randint(1, 3) == 2:
        g_man_toilet.attack(TV_man)
    else:
        TV_man.attack(g_man_toilet)
    if TV_man.health < 0 or g_man_toilet.health < 0:
        print('game over')
        break