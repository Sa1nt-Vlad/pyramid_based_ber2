from enum import Enum

cutlet_types_translation = {'chicken': 'куриная', 'beef': 'говяжья'}


class Cutlet(Enum):
    chicken = 0
    beef = 1

    def __str__(self):
        return cutlet_types_translation[self.name]
