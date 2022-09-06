from datetime import datetime, timedelta, timezone
import pytest
from onlineshop.item import Item

from onlineshop.order import Order

# pytest supports writing fixtures once in conftest.py and
# tests in same folder or subfolders can use them

@pytest.fixture()
def test_order() -> Order:
    return Order(
        order_id=1,
        purchase_date=datetime.now(timezone.utc) - timedelta(minutes=5),
        purchase_cost=100,
        items=[Item(item_id=2, price=100)]
    )

@pytest.fixture()
def test_item() -> Item:
    return Item(item_id=2, price=100)