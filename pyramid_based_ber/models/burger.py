from pyramid_based_ber.models.burger_config.bun import Bun
from pyramid_based_ber.models.burger_config.cutlet import Cutlet


class Burger(object):
    def __init__(self, bun: Bun, cutlet: Cutlet, sauces: list, stuffings: list):
        self.bun = bun
        self.cutlet = cutlet
        self.sauces = sauces
        self.stuffings = stuffings
