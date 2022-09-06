from onlineshop.item import Item
from onlineshop.order import Order
from onlineshop.testable.order_has_items_validator import OrderHasItemsValidator


def test_order_with_items_is_valid(test_order: Order, test_item: Item) -> None:
    # Arrange
    order_validator = OrderHasItemsValidator()
    test_order.items = [test_item]

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == True

def test_order_without_items_is_invalid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderHasItemsValidator()
    test_order.items = []

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == False