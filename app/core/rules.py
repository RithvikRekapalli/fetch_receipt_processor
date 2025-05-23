from abc import ABC, abstractmethod
from datetime import datetime, time
from math import ceil
import re
from typing import List
from app.models.entities import Receipt

class ScoringRule(ABC):
    """Abstract base class for scoring rules."""
    @abstractmethod
    def apply(self, receipt: Receipt) -> int:
        """Return points for this rule."""
        raise NotImplementedError

class RetailerNameRule(ScoringRule):
    def apply(self, receipt: Receipt) -> int:
        return len(re.findall(r'[A-Za-z0-9]', receipt.retailer))

class RoundTotalRule(ScoringRule):
    def apply(self, receipt: Receipt) -> int:
        return 50 if receipt.total.is_integer() else 0

class QuarterTotalRule(ScoringRule):
    def apply(self, receipt: Receipt) -> int:
        return 25 if (receipt.total * 100) % 25 == 0 else 0

class PairItemRule(ScoringRule):
    def apply(self, receipt: Receipt) -> int:
        return (len(receipt.items) // 2) * 5

class ItemDescriptionRule(ScoringRule):
    def apply(self, receipt: Receipt) -> int:
        points = 0
        for item in receipt.items:
            if len(item.short_description.strip()) % 3 == 0:
                points += ceil(item.price * 0.2)
        return points

class DayOddRule(ScoringRule):
    def apply(self, receipt: Receipt) -> int:
        day = int(receipt.purchase_date.split('-')[2])
        return 6 if day % 2 else 0

class AfternoonRule(ScoringRule):
    def apply(self, receipt: Receipt) -> int:
        t = datetime.strptime(receipt.purchase_time, '%H:%M').time()
        return 10 if time(14, 0) < t < time(16, 0) else 0

def default_rules() -> List[ScoringRule]:
    return [
        RetailerNameRule(),
        RoundTotalRule(),
        QuarterTotalRule(),
        PairItemRule(),
        ItemDescriptionRule(),
        DayOddRule(),
        AfternoonRule()
    ]
