# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session

# from app.database.dependencies import get_db
# from app.database.models import Prediction

# router = APIRouter()

# @router.get("/history")
# def history(db: Session = Depends(get_db)):
#     predictions = db.query(Prediction).order_by(Prediction.id.desc()).all()

#     return predictions

# backend/app/api/history.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.dependencies import get_db
from app.database.models import Prediction
from app.database.schemas import PredictionOut

router = APIRouter()

@router.get("/history", response_model=List[PredictionOut])
def history(db: Session = Depends(get_db)):
    predictions = db.query(Prediction).order_by(Prediction.id.desc()).all()
    return predictions