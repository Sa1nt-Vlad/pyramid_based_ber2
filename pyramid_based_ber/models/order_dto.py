from pyramid_based_ber.models.burger import Burger


class OrderDto(object):
    def __init__(self, name: str, phone_number: str, address: str, burger_config: Burger):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.burger_config = burger_config
