from sqlalchemy.orm import Session
from app.database.models import Prediction

def create_prediction(
    db: Session,
    filename: str,
    prediction: str,
    confidence: float,
    report: str
):
    new_prediction = Prediction(
        filename=filename,
        prediction=prediction,
        confidence=confidence,
        report=report
    )

    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    return new_prediction