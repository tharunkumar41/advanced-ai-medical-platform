import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the trained model only once when the application starts
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "models",
    "pneumonia_model.keras"
)

model = tf.keras.models.load_model(MODEL_PATH)
IMG_SIZE = (224, 224)


def predict_disease(image_path: str):
    # Load image
    img = image.load_img(image_path, target_size=IMG_SIZE)

    # Convert to array
    img_array = image.img_to_array(img)

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Apply EfficientNet preprocessing
    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)

    # Predict
    prediction = model.predict(img_array, verbose=0)[0][0]

    if prediction >= 0.5:
        label = "PNEUMONIA"
        confidence = float(prediction)
    else:
        label = "NORMAL"
        confidence = float(1 - prediction)

    return {
        "prediction": label,
        "confidence": round(confidence * 100, 2)
    }