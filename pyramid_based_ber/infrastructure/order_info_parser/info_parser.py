from datetime import datetime

from pyramid_based_ber.classes.burger_config.bun import Bun
from pyramid_based_ber.classes.burger_config.cutlet import Cutlet
from pyramid_based_ber.classes.burger_config.sauce import Sauce
from pyramid_based_ber.classes.burger_config.sauces import Sauces
from pyramid_based_ber.classes.burger_config.stuffing import Stuffing
from pyramid_based_ber.classes.burger_config.stuffings import Stuffings
from pyramid_based_ber.infrastructure.enums_parser import ingredients_parser
from pyramid_based_ber.classes.burger import Burger

from pyramid_based_ber.infrastructure.validation.info_validator import *

default_values = {'bread': Bun.no_sesame, 'meat': Cutlet.beef,
                  'sauces': [Sauce.ketchup, Sauce.mustard],
                  'stuffings': [Stuffing.tomato, Stuffing.cucumber, Stuffing.cheese]}


def parse_order_info(params) -> OrderDto:
    burger = parse_burger_info(params)
    return OrderDto(
        creation_date=datetime.now(tz=None),
        name=remove_unnecessary_whitespaces(params['name']),
        phone_number=remove_unnecessary_whitespaces(params['phone_number']),
        address=remove_unnecessary_whitespaces(params['address']),
        burger_config=burger)


def parse_burger_info(params) -> Burger:
    if 'bread' in params:
        bun = ingredients_parser.parse_bun(params['bread'])
    else:
        bun = default_values['bread']

    if 'meat' in params:
        cutlet = ingredients_parser.parse_cutlet(params['meat'])
    else:
        cutlet = default_values['meat']

    if 'sauce' in params:
        sauces = Sauces(ingredients_parser.parse_sauces(params.getall('sauce')))
    else:
        sauces = Sauces(default_values['sauces'])

    if 'stuffing' in params:
        stuffings = Stuffings(ingredients_parser.parse_stuffings(params.getall('stuffing')))
    else:
        stuffings = Stuffings(default_values['stuffings'])

    return Burger(bun, cutlet, sauces, stuffings)


def remove_unnecessary_whitespaces(string: str) -> str:
    result = string
    for char in string:
        if char.isspace():
            result = result.replace(char, '', 1)
        else:
            return result
