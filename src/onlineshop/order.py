from dataclasses import dataclass
from datetime import datetime

from onlineshop.item import Item

@dataclass
class Order:
    order_id: int
    purchase_date: datetime
    purchase_cost: int
    items: list[Item]