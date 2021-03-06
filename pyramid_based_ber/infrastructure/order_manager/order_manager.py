import transaction
from pyramid_based_ber.models import BurgerDB, OrderDB, PW


def register_order(request, order_info):
    burger = BurgerDB(
        bun=str(order_info.burger_config.bun),
        cutlet=str(order_info.burger_config.cutlet),
        sauces=str(order_info.burger_config.sauces),
        stuffings=str(order_info.burger_config.stuffings))
    request.dbsession.add(burger)
    transaction.commit()
    query = request.dbsession.query(BurgerDB)
    id = query.order_by(BurgerDB.id.desc()).first().id
    order = OrderDB(
        name=order_info.name,
        phone=order_info.phone_number,
        address=order_info.address,
        burger=id,
        time=order_info.creation_date,
        done=order_info.done
    )
    request.dbsession.add(order)
    transaction.commit()

    query = request.dbsession.query(OrderDB)
    order_id = query.order_by(OrderDB.id.desc()).first().id
    return order_id
