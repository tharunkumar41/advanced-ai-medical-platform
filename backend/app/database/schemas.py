# backend/app/database/schemas.py  (new file)
from pydantic import BaseModel
from datetime import datetime

class PredictionOut(BaseModel):
    id: int
    filename: str
    prediction: str
    confidence: float
    report: str
    created_at: datetime

    class Config:
        from_attributes = True   # allows Pydantic to read from ORM objects