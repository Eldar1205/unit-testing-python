from onlineshop.order import Order
from onlineshop.testable.iorder_validator import IOrderValidator


class OrderPurchaseCostValidator(IOrderValidator):
    def validate(self, order: Order) -> bool:
        return sum(item.price for item in order.items) == order.purchase_cost