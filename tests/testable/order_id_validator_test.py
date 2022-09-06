from onlineshop.order import Order
from onlineshop.testable.order_id_validator import OrderIdValidator


def test_order_with_positive_id_is_valid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderIdValidator()
    test_order.order_id = 5

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == True

def test_order_with_zero_id_is_invalid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderIdValidator()
    test_order.order_id = 0

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == False

def test_order_with_negative_id_is_invalid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderIdValidator()
    test_order.order_id = -5

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == False