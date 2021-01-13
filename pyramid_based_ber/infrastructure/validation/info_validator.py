import re

from pyramid_based_ber.models.order_dto import OrderDto


def validate(order_info: OrderDto) -> bool:
    return correct_name(order_info.name) \
           and correct_number(order_info.phone_number) \
           and correct_address(order_info.address)


def correct_name(name: str) -> bool:
    return re.match(r'[a-zA-Z]{3,10}', name) is not None


def correct_number(number: str) -> bool:
    return re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', number) is not None


def correct_address(address: str) -> bool:
    return len(address) > 5
