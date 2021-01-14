import datetime

from pyramid_based_ber.classes.burger import Burger


class OrderDto(object):
    def __init__(self, order_id: int, creation_date: datetime,
                 name: str, phone_number: str, address: str,
                 burger_config: Burger):
        self.order_id = order_id
        self.creation_date = creation_date
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.burger_config = burger_config
