import re

from pyramid_based_ber.classes.order_dto import OrderDto


def get_valid_personal_data(order_info: OrderDto) -> OrderDto:
    if not correct_name(order_info.name):
        order_info.name = 'Ошибка при заполнении имени! (Длина имени не менее 3 и не более 10 символов)'

    if not correct_number(order_info.phone_number):
        order_info.phone_number = 'Ошибка при заполнении мобильного телефона! (Шаблон: 88005553535)'

    if not correct_address(order_info.address):
        order_info.address = 'Ошибка при заполнении адреса! (Длина адреса не менее 5 символов)'

    return order_info


def validate(order_info: OrderDto) -> bool:
    return correct_name(order_info.name) \
           and correct_number(order_info.phone_number) \
           and correct_address(order_info.address)


def correct_name(name: str) -> bool:
    return name is not None and re.match(r'[a-zA-Zа-яА-Я]{3,10}', name) is not None


def correct_number(number: str) -> bool:
    return number is not None and re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', number) is not None


def correct_address(address: str) -> bool:
    return address is not None and len(address) > 5
