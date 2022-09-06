from onlineshop.order import Order
from onlineshop.testable.iorder_validator import IOrderValidator


class OrderHasItemsValidator(IOrderValidator):
    def validate(self, order: Order) -> bool:
        return len(order.items) > 0