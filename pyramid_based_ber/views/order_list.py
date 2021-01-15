import transaction
from pyramid.view import view_config
from pyramid_based_ber.infrastructure.order_info_parser.info_parser import parse_order_info
from pyramid_based_ber.infrastructure.order_manager.order_manager import register_order
from pyramid_based_ber.infrastructure.validation.info_validator import validate


@view_config(route_name='list', renderer='../templates/order_list.jinja2')
def make_order(request):
    from .. import models
    query = request.dbsession.query(models.OrderDB)
    order_infos = query.all()
    return {'order_infos': order_infos}
    # else:
    # return {'': 'Incorrect data'}


@view_config(route_name='done', renderer='../templates/order_list.jinja2')
def done_order(request):
    from .. import models
    order = request.dbsession.query(models.OrderDB).filter_by(id=request.params["id"]).first()
    order.done = 1
    transaction.commit()
    return {'order_infos': request.dbsession.query(models.OrderDB).all()}
    # else:
    # return {'': 'Incorrect data'}