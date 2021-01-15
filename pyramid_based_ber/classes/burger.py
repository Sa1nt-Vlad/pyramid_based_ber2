from pyramid_based_ber.classes.burger_config.bun import Bun
from pyramid_based_ber.classes.burger_config.cutlet import Cutlet
from pyramid_based_ber.classes.burger_config.sauces import Sauces
from pyramid_based_ber.classes.burger_config.stuffings import Stuffings


class Burger(object):
    def __init__(self, bun: Bun, cutlet: Cutlet, sauces: Sauces, stuffings: Stuffings):
        self.bun = bun
        self.cutlet = cutlet
        self.sauces = sauces
        self.stuffings = stuffings
