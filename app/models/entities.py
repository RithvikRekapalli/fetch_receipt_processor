from dataclasses import dataclass
from typing import List

@dataclass(frozen=True, slots=True)
class Item:
    short_description: str
    price: float

@dataclass(frozen=True, slots=True)
class Receipt:
    retailer: str
    purchase_date: str  # ISO date YYYY-MM-DD
    purchase_time: str  # HH:MM
    items: List[Item]
    total: float
