from pydantic import BaseModel, Field, constr
from typing import List

# Helpers
MoneyStr   = constr(pattern=r"^\d+\.\d{2}$")
IsoDate    = constr(pattern=r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")
IsoTime    = constr(pattern=r"^(?:[01]\d|2[0-3]):[0-5]\d$")        # 00:00-23:59


class ItemSchema(BaseModel):
    shortDescription: str = Field(..., min_length=1)
    price: MoneyStr

class ReceiptSchema(BaseModel):
    retailer: str
    purchaseDate: IsoDate
    purchaseTime: IsoTime
    items: list[ItemSchema]
    total: MoneyStr

class ReceiptIDResponse(BaseModel):
    id: str

class PointsResponse(BaseModel):
    points: int


