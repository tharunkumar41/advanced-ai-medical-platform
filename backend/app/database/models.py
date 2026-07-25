from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .db import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    prediction = Column(String)
    confidence = Column(Float)
    report = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)