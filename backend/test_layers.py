import os
import tensorflow as tf

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "models",
    "pneumonia_model.keras"
)

model = tf.keras.models.load_model(MODEL_PATH)

print("\nModel Layers:\n")

for layer in model.layers:
    print(layer.name)