from pyramid_based_ber.infrastructure.enums_parser import ingredients_parser
from pyramid_based_ber.models.burger import Burger
from pyramid_based_ber.models.order_dto import OrderDto


def parse_order_info(params) -> OrderDto:
    burger = parse_burger_info(params)
    return OrderDto(remove_unnecessary_whitespaces(params['name']),
                    remove_unnecessary_whitespaces(params['phone_number']),
                    remove_unnecessary_whitespaces(params['address']), burger)


def parse_burger_info(params) -> Burger:
    bun = ingredients_parser.parse_bun(params['bread'])
    cutlet = ingredients_parser.parse_cutlet(params['meat'])
    sauces = ingredients_parser.parse_sauces(params.getall('sauce'))
    stuffings = ingredients_parser.parse_stuffings(params.getall('stuffing'))
    return Burger(bun, cutlet, sauces, stuffings)


def remove_unnecessary_whitespaces(string: str) -> str:
    result = string
    for char in string:
        if char.isspace():
            result = result.replace(char, '', 1)
        else:
            return result
