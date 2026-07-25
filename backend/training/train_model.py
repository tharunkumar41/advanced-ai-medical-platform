import os
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

from data_loader import load_datasets
from model import build_model

# Dataset path
DATASET_PATH = r"C:\Users\kingp\OneDrive\Documents\advanced-ai-medical-platform\chest_xray"

# Model save path
MODEL_DIR = "../models"
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "pneumonia_model.keras")

# Load datasets
train_ds, val_ds, test_ds = load_datasets(DATASET_PATH)

# Build model
model = build_model()

# Callbacks
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

checkpoint = ModelCheckpoint(
    MODEL_PATH,
    monitor="val_accuracy",
    save_best_only=True
)

# Train
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10,
    callbacks=[early_stopping, checkpoint]
)

# Evaluate
loss, accuracy = model.evaluate(test_ds)

print(f"\nTest Accuracy: {accuracy:.4f}")
print(f"Test Loss: {loss:.4f}")

# Save final model
model.save(MODEL_PATH)

print(f"\nModel saved to: {MODEL_PATH}")