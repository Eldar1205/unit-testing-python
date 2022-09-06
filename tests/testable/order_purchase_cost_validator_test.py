from onlineshop.item import Item
from onlineshop.order import Order
from onlineshop.testable.order_purchase_cost_validator import OrderPurchaseCostValidator


def test_order_with_single_item_price_equals_purchase_cost_is_valid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderPurchaseCostValidator()
    test_order.items = [Item(item_id=2, price=84)]
    test_order.purchase_cost = 84

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == True

def test_order_with_single_item_price_not_equals_purchase_cost_is_invalid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderPurchaseCostValidator()
    test_order.items = [Item(item_id=2, price=84)]
    test_order.purchase_cost = 88

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == False

def test_order_with_multple_items_price_total_equals_purchase_cost_is_valid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderPurchaseCostValidator()
    test_order.items = [Item(item_id=2, price=84), Item(item_id=3, price=66)]
    test_order.purchase_cost = 150

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == True

def test_order_with_multple_items_price_total_not_equals_purchase_cost_is_invalid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderPurchaseCostValidator()
    test_order.items = [Item(item_id=2, price=84), Item(item_id=3, price=66)]
    test_order.purchase_cost = 140

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == False