from enum import Enum

stuffing_types_translation = {'cheese': 'сыр', 'salad': 'салат', 'cucumber': 'огурец', 'egg': 'яйцо',
                              'onion': 'лук', 'tomato': 'томаты', 'bacon': 'бекон', 'crisps': 'чипсы'}


class Stuffing(Enum):
    cheese = 0
    salad = 1
    cucumber = 2
    onion = 3
    tomato = 4
    bacon = 5
    egg = 6
    crisps = 7

    def __str__(self):
        return stuffing_types_translation[self.name]
