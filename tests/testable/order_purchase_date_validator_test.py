from datetime import datetime, timedelta, timezone
from freezegun import freeze_time
from onlineshop.order import Order
from onlineshop.testable.order_purchase_date_validator import OrderPurchaseDateValidator

# Tests in this file use freezegun to control the datetime.now() calls made by OrderPurchaseDateValidator.
# Generally speaking such a monkeypatching approach is ill-advised for unit testing,
# because it makes assumptions about implementations details of the tested class, e.g. using datetime.now(),
# however when it comes to testing code that relies on datetime.now() it's usually considered acceptable for practical reasons.

@freeze_time("2020-01-14")
def test_order_with_past_purchase_date_is_valid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderPurchaseDateValidator()
    test_order.purchase_date = datetime.now(timezone.utc) - timedelta(minutes=5)

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == True

@freeze_time("2020-01-14")
def test_order_with_now_purchase_date_is_valid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderPurchaseDateValidator()
    test_order.purchase_date = datetime.now(timezone.utc)

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == True

@freeze_time("2020-01-14")
def test_order_with_future_purchase_date_is_invalid(test_order: Order) -> None:
    # Arrange
    order_validator = OrderPurchaseDateValidator()
    test_order.purchase_date = datetime.now(timezone.utc) + timedelta(minutes=5)

    # Act
    is_valid = order_validator.validate(test_order)

    # Assert
    assert is_valid == False