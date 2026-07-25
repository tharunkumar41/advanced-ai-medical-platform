import os
import tensorflow as tf
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau
)

from data_loader import load_datasets

# Dataset path
DATASET_PATH = r"C:\Users\kingp\OneDrive\Documents\advanced-ai-medical-platform\chest_xray"

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "pneumonia_model.keras")

# Load datasets
train_ds, val_ds, test_ds = load_datasets(DATASET_PATH)

# Load previously trained model
model = tf.keras.models.load_model(MODEL_PATH)

print("✅ Loaded existing model")

# Find EfficientNet base model
base_model = None
for layer in model.layers:
    if isinstance(layer, tf.keras.Model):
        base_model = layer
        break

if base_model is None:
    raise ValueError("EfficientNet base model not found.")

# Fine-tune last 20 layers
base_model.trainable = True

for layer in base_model.layers[:-20]:
    layer.trainable = False

# Recompile with lower learning rate
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
    loss="binary_crossentropy",
    metrics=[
        "accuracy",
        tf.keras.metrics.Precision(name="precision"),
        tf.keras.metrics.Recall(name="recall")
    ]
)

# Callbacks
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True,
    verbose=1
)

checkpoint = ModelCheckpoint(
    MODEL_PATH,
    monitor="val_accuracy",
    save_best_only=True,
    verbose=1
)

reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.2,
    patience=2,
    min_lr=1e-6,
    verbose=1
)

# Continue training
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10,
    callbacks=[
        early_stopping,
        checkpoint,
        reduce_lr
    ]
)

# Evaluate
results = model.evaluate(test_ds)

print("\n========== Fine-Tuning Results ==========")
print(f"Test Loss      : {results[0]:.4f}")
print(f"Test Accuracy  : {results[1]:.4f}")

if len(results) >= 4:
    print(f"Test Precision : {results[2]:.4f}")
    print(f"Test Recall    : {results[3]:.4f}")

print("=========================================")

# Save final model
model.save(MODEL_PATH)

print(f"\n✅ Fine-tuned model saved at:\n{MODEL_PATH}")