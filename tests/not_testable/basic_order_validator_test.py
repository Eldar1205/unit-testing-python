from onlineshop.item import Item
from onlineshop.order import Order

from onlineshop.not_testable.order_validator import OrderValidator

# Demonstration of using test functions

# We include only few examples for valid order scenarios,
# to test all possible scenarios with all combinations of validations checks
# performed inside OrderValidator will lead to dozens of tests so they are not implemented.

def test_valid_order_single_item(test_order: Order) -> None:
    # Arrange
    order_validator = OrderValidator()
    test_order.items = [Item(item_id=2, price=100)]
    test_order.purchase_cost = 100

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert (with optional message)
    assert is_valid == True, "Expected order to be valid because ids are positive, purchase date is in the past, single item price equals purchase cost"

def test_valid_order_multiple_items(test_order: Order) -> None:
    # Arrange
    order_validator = OrderValidator()
    test_order.items=[Item(item_id=2, price=40), Item(item_id=3, price=60)]
    test_order.purchase_cost = 100

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert (with optional message)
    assert is_valid, "Expected order to be valid because ids are positive, purchase date is in the past, multiple items prices sum up to purchase cost"



