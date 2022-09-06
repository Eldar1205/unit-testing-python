from onlineshop.order import Order
from onlineshop.testable.iorder_validator import IOrderValidator


class OrderIdValidator(IOrderValidator):
    def validate(self, order: Order) -> bool:
        return order.order_id > 0