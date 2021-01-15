from datetime import datetime

from pyramid_based_ber.classes.burger_config.sauces import Sauces
from pyramid_based_ber.classes.burger_config.stuffings import Stuffings
from pyramid_based_ber.infrastructure.enums_parser import ingredients_parser
from pyramid_based_ber.classes.burger import Burger
from pyramid_based_ber.classes.order_dto import OrderDto


def parse_order_info(params) -> OrderDto:
    burger = parse_burger_info(params)
    return OrderDto(
        creation_date=datetime.now(tz=None),
        name=remove_unnecessary_whitespaces(params['name']),
        phone_number=remove_unnecessary_whitespaces(params['phone_number']),
        address=remove_unnecessary_whitespaces(params['address']),
        burger_config=burger)


def parse_burger_info(params) -> Burger:
    bun = ingredients_parser.parse_bun(params['bread'])
    cutlet = ingredients_parser.parse_cutlet(params['meat'])
    sauces = Sauces(ingredients_parser.parse_sauces(params.getall('sauce')))
    stuffings = Stuffings(ingredients_parser.parse_stuffings(params.getall('stuffing')))
    return Burger(bun, cutlet, sauces, stuffings)


def remove_unnecessary_whitespaces(string: str) -> str:
    result = string
    for char in string:
        if char.isspace():
            result = result.replace(char, '', 1)
        else:
            return result
