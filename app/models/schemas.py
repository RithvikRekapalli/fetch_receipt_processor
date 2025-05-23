from pydantic import BaseModel, Field, constr
from typing import List

# Helpers
MoneyStr = constr(pattern=r"^\d+\.\d{2}$")
IsoDate  = constr(pattern=r"^\d{4}-\d{2}-\d{2}$")
IsoTime  = constr(pattern=r"^\d{2}:\d{2}$")

class ItemSchema(BaseModel):
    shortDescription: str = Field(..., min_length=1)
    price: MoneyStr

class ReceiptSchema(BaseModel):
    retailer: str
    purchaseDate: IsoDate
    purchaseTime: IsoTime
    items: List[ItemSchema]
    total: MoneyStr

class ReceiptIDResponse(BaseModel):
    id: str

class PointsResponse(BaseModel):
    points: int
