from datetime import datetime, timezone
from onlineshop.order import Order
from onlineshop.testable.iorder_validator import IOrderValidator


class OrderPurchaseDateValidator(IOrderValidator):
    def validate(self, order: Order) -> bool:
        return order.purchase_date <= datetime.now(timezone.utc)