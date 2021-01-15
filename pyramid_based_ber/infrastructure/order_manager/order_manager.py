import transaction
from pyramid_based_ber.models import BurgerDB, OrderDB


def register_order(request, order_info):
    burger = BurgerDB(
        bun=repr(order_info.burger_config.bun),
        cutlet=repr(order_info.burger_config.cutlet),
        sauces=repr(order_info.burger_config.sauces.sauces),
        stuffings=repr(order_info.burger_config.stuffings.stuffings))
    request.dbsession.add(burger)
    transaction.commit()
    query = request.dbsession.query(BurgerDB)
    id = query.order_by(BurgerDB.id.desc()).first().id
    order = OrderDB(
        name=order_info.name,
        phone=order_info.phone_number,
        address=order_info.address,
        burger=id,
        time=order_info.creation_date
    )
    request.dbsession.add(order)
    transaction.commit()
