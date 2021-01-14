from pyramid_based_ber.classes.burger_config.bun import Bun
from pyramid_based_ber.classes.burger_config.cutlet import Cutlet
from pyramid_based_ber.classes.burger_config.sauce import Sauce
from pyramid_based_ber.classes.burger_config.stuffing import Stuffing

bun_types = {'sesame': Bun.sesame, 'no_sesame': Bun.no_sesame}
cutlet_types = {'chicken': Cutlet.chicken, 'beef': Cutlet.beef}
sauce_types = {'barbecue': Sauce.barbecue, 'ketchup': Sauce.ketchup, 'mustard': Sauce.mustard, 'garlic': Sauce.garlic}
stuffing_types = {'salad': Stuffing.salad, 'bacon': Stuffing.bacon, 'cheese': Stuffing.cheese,
                  'crisps': Stuffing.crisps, 'cucumber': Stuffing.cucumber, 'egg': Stuffing.egg,
                  'onion': Stuffing.onion, 'tomato': Stuffing.tomato}


def parse_bun(bun: str) -> Bun:
    return parse_ingredient(bun, bun_types)


def parse_cutlet(cutlet: str) -> Cutlet:
    return parse_ingredient(cutlet, cutlet_types)


def parse_sauce(sauce: str) -> Sauce:
    return parse_ingredient(sauce, sauce_types)


def parse_sauces(sauces: list) -> list:
    parsed_sauces = list()
    for sauce in sauces:
        parsed_sauces.append(parse_sauce(sauce))
    return parsed_sauces


def parse_stuffing(stuffing: str) -> Stuffing:
    return parse_ingredient(stuffing, stuffing_types)


def parse_stuffings(stuffings: list) -> list:
    parsed_stuffings = list()
    for stuffing in stuffings:
        parsed_stuffings.append(parse_stuffing(stuffing))
    return parsed_stuffings


def parse_ingredient(name: str, possible_values: dict):
    if name in possible_values:
        return possible_values[name]
    raise ValueError(f"{list(possible_values.values())[0]} type {name} doesn't exist")
