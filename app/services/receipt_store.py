from uuid import uuid4
from typing import Dict

class ReceiptStore:
    """Thread‑safe in‑memory store for receipt points."""
    def __init__(self):
        self._data: Dict[str, int] = {}

    def add_receipt(self, points: int) -> str:
        receipt_id = str(uuid4())
        self._data[receipt_id] = points
        return receipt_id

    def get_points(self, receipt_id: str) -> int | None:
        return self._data.get(receipt_id)
