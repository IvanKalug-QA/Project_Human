from random import randint


def hit_by_a_car(user: object) -> str:
    urgent_treatment: int = 200
    if user.money < urgent_treatment:
        user.money = 0
        return ('Вас сбила машина, '
                'и у вас нехватает средств, '
                'чтобы оплатить лечение, '
                'но больница пошла вам на встречу и '
                'согласилась взять все деньги что у вас есть')
    user.money -= urgent_treatment
    return ('Вас сбила машина, '
            f'и операция стоила вам - ${urgent_treatment}')


def homeless_mans_attack(user: object) -> str:
    prey: int = randint(1, 20)
    if user.money < prey:
        user.money = 0
        return ('На тебя напал бомж, '
                'он запросил у тебя слишком много, '
                'и ты не смог ему столько дать, '
                'поэтому бомж просто забрал твой кошелек')
    user.money -= prey
    return ('На тебя напал бомж,'
            'и чтобы он тебя не пырнул, '
            f'пришлось отдать бродяге - ${prey}')
