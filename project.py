import random


class Human():
    HANDIMEN_ACTIONS = {
        'починил душ', 'повесил телевизор', 'прикрутил картину',
        'собрал кровать', 'собрал стул'
    }

    def __init__(self, name):
        self.name = name
        self.money = 100
        self.respect = 0

    def part_time_work(self):
        self.money += 2
        return (f'Сегодня - {self.name} сходил на подработу, '
                f'и заработал - {self.money}')

    def mover(self):
        self.respect += 1
        self.money += 10
        return (f'Сегодня {self.name} впахал не хило '
                f'поднял увадение на - {self.respect} '
                f'и заработал - {self.money}')

    def handimen(self):
        self.respect += 3
        self.money += 15
        return (f'Сегодня ты - {random.choice(self.HANDIMEN_ACTIONS)}')

    def seller(self):
        pass


class PersonOne(Human):
    pass