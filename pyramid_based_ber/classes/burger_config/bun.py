from enum import Enum

bun_types_translation = {'sesame': 'с кунжутом', 'no_sesame': 'без кунжута'}


class Bun(Enum):
    no_sesame = 0
    sesame = 1

    def __str__(self):
        return bun_types_translation[self.name]
