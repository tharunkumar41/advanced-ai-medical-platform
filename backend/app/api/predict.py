from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.database.crud import create_prediction
from app.services.ai_service import predict_disease
from app.services.gradcam_service import generate_gradcam
from app.services.llm_service import generate_report

import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/predict")
async def predict(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Save uploaded image
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # AI Prediction
    result = predict_disease(file_path)

    prediction = result["prediction"]
    confidence = result["confidence"]

    # Generate Grad-CAM
    # Generate Grad-CAM
    gradcam_path = generate_gradcam(file_path)
    gradcam_url = "/" + gradcam_path.replace("\\", "/")

    # Generate AI Medical Report
    report = generate_report(
        prediction,
        confidence
    )

    # Save prediction history
    create_prediction(
        db,
        file.filename,
        prediction,
        confidence,
        report
    )

    # Return response
    return {
    "filename": file.filename,
    "prediction": prediction,
    "confidence": confidence,
    "report": report,
    "gradcam_image": gradcam_url
}