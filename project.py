import random


class Human():
    HANDIMEN_ACTIONS = {
        'починил душ', 'повесил телевизор', 'прикрутил картину',
        'собрал кровать', 'собрал стул', 'вкрутил лампочку',
        'передвинул диван'
    }

    def __init__(self, name):
        self.name = name
        self.money = 100
        self.respect = 0
        self.energy = 100

    def part_time_work(self) -> str:
        if self.energy - 10 < 0:
            return 'Мало энергии!'
        self.money += 2
        self.energy -= 10
        salary: float = 2
        return (f'Сегодня - {self.name} сходил на подработу, '
                f'и заработал - ${salary}, осталось энергии - {self.energy}')

    def mover(self) -> str:
        if self.energy - 15 < 0:
            return 'Мало энергии!'
        self.respect += 1
        self.money += 10
        self.energy -= 15
        respec: int = 1
        salary: float = 10
        return (f'Сегодня {self.name} впахал не хило '
                f'поднял увадение на - {respec} '
                f'и заработал - ${salary}, осталось энергии - {self.energy}')

    def handimen(self) -> str:
        if self.energy - 25 < 0:
            return 'Мало энергии!'
        self.respect += 3
        self.money += 15
        self.energy -= 25
        salary: float = 15
        respec: int = 3
        return (f'Сегодня ты - {random.choice(self.HANDIMEN_ACTIONS)} '
                f'поднял уважение на - {respec}, и заработал ${salary}, '
                f'осталось энергии - {self.energy}')

    def seller(self):
        pass


class Easy(Human):
    pass