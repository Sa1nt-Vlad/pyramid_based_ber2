from enum import Enum

sauce_types_translation = {'barbecue': 'барбекю', 'mustard': 'горчица',
                           'garlic': 'сметанно-чесночный', 'ketchup': 'кетчуп'}


class Sauce(Enum):
    barbecue = 0
    mustard = 1
    garlic = 2
    ketchup = 3

    def __str__(self):
        return sauce_types_translation[self.name]
