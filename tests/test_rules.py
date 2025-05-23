from app.core.processor import ReceiptProcessor
from app.models.entities import Receipt, Item

def test_sample_receipt_1():
    receipt = Receipt(
        retailer="Target",
        purchase_date="2022-01-01",
        purchase_time="13:01",
        items=[
            Item("Mountain Dew 12PK", 6.49),
            Item("Emils Cheese Pizza", 12.25),
            Item("Knorr Creamy Chicken", 1.26),
            Item("Doritos Nacho Cheese", 3.35),
            Item("   Klarbrunn 12-PK 12 FL OZ  ", 12.00)
        ],
        total=35.35
    )
    points = ReceiptProcessor().calculate_points(receipt)
    assert points == 28

def test_sample_receipt_2():
    receipt = Receipt(
        retailer="M&M Corner Market",
        purchase_date="2022-03-20",
        purchase_time="14:33",
        items=[Item("Gatorade", 2.25) for _ in range(4)],
        total=9.00
    )
    points = ReceiptProcessor().calculate_points(receipt)
    assert points == 109
