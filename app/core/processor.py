from typing import List
from app.models.entities import Receipt
from app.core.rules import default_rules, ScoringRule

class ReceiptProcessor:
    """Aggregates scoring rules and computes total points."""
    def __init__(self, rules: List[ScoringRule] | None = None):
        self.rules = rules or default_rules()

    def calculate_points(self, receipt: Receipt) -> int:
        return sum(rule.apply(receipt) for rule in self.rules)
