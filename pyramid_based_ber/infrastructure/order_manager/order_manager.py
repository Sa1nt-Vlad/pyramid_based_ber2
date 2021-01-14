from pyramid_based_ber import models
import transaction


def register_order(request, order_info):
    transaction.commit()
