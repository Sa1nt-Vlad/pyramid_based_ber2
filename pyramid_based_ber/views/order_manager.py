from pyramid.view import view_config
from pyramid_based_ber.infrastructure.order_info_parser.info_parser import parse_order_info
from pyramid_based_ber.infrastructure.order_manager.order_manager import register_order
from pyramid_based_ber.infrastructure.validation.info_validator import *


@view_config(route_name='order', renderer='../templates/order_info.jinja2')
def make_order(request):
    order_info = parse_order_info(request.params)
    order_info.order_id = 'Заказ не оформлен!'

    if not validate(order_info):
        order_info = get_valid_personal_data(order_info)
    else:
        order_id = register_order(request, order_info)
        order_info.order_id = order_id

    return {'order_info': order_info}
