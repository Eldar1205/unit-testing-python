from datetime import datetime, timezone

from onlineshop.order import Order


class OrderValidator:
    def validate(self, order: Order) -> bool:
        # We trust type checkers to ensure order is not None
        if order.order_id <= 0:
            return False

        if order.purchase_date > datetime.now(timezone.utc):
            return False
        
        # Checks for None and empty list, no need to check for None since @dataclass validates fields
        if not order.items:
            return False

        if sum(item.price for item in order.items) != order.purchase_cost:
            return False

        return True