from fastapi import APIRouter, HTTPException
from app.models.schemas import ReceiptSchema, ReceiptIDResponse, PointsResponse
from app.models.entities import Receipt, Item
from app.core.processor import ReceiptProcessor
from app.services.receipt_store import ReceiptStore

router = APIRouter()
processor = ReceiptProcessor()
store = ReceiptStore()

@router.post("/receipts/process", response_model=ReceiptIDResponse, status_code=201)
async def process_receipt(receipt_in: ReceiptSchema):
    # Transform schema to domain entity
    receipt = Receipt(
        retailer=receipt_in.retailer,
        purchase_date=receipt_in.purchaseDate,
        purchase_time=receipt_in.purchaseTime,
        items=[Item(short_description=i.shortDescription, price=float(i.price)) for i in receipt_in.items],
        total=float(receipt_in.total)
    )
    points = processor.calculate_points(receipt)
    receipt_id = store.add_receipt(points)
    return {"id": receipt_id}

@router.get("/receipts/{receipt_id}/points", response_model=PointsResponse)
async def get_points(receipt_id: str):
    points = store.get_points(receipt_id)
    if points is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return {"points": points}
