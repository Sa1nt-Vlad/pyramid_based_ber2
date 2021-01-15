from pyramid.view import view_config
from pyramid_based_ber.infrastructure.order_info_parser.info_parser import parse_order_info
from pyramid_based_ber.infrastructure.order_manager.order_manager import register_order
from pyramid_based_ber.infrastructure.validation.info_validator import validate


@view_config(route_name='burgers', renderer='../templates/burger_list.jinja2')
def make_order(request):
    from .. import models
    query = request.dbsession.query(models.BurgerDB)
    burgers = query.all()
    return {'burgers': burgers}
    # else:
    # return {'': 'Incorrect data'}