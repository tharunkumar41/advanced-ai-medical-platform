import os
import cv2
import numpy as np
import tensorflow as tf

# Load model once
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "models",
    "pneumonia_model.keras"
)
print("GRADCAM MODEL PATH:", MODEL_PATH)
print("MODEL EXISTS:", os.path.exists(MODEL_PATH))

model = tf.keras.models.load_model(MODEL_PATH)

LAST_CONV_LAYER = "top_conv"


def generate_gradcam(image_path):
    # Read original image
    original = cv2.imread(image_path)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

    # Preprocess image
    img = cv2.resize(original, (224, 224))
    img = img.astype(np.float32)
    img = tf.keras.applications.efficientnet.preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    # Grad-CAM model
    grad_model = tf.keras.models.Model(
        inputs=model.inputs,
        outputs=[
            model.get_layer(LAST_CONV_LAYER).output,
            model.output
        ]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img)

        # Binary classification
        loss = predictions[:, 0]

    grads = tape.gradient(loss, conv_outputs)

    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_outputs = conv_outputs[0]

    heatmap = tf.reduce_sum(
        conv_outputs * pooled_grads,
        axis=-1
    )

    heatmap = tf.maximum(heatmap, 0)
    heatmap /= tf.reduce_max(heatmap) + 1e-8

    heatmap = heatmap.numpy()

    # Resize heatmap to original image size
    heatmap = cv2.resize(
        heatmap,
        (original.shape[1], original.shape[0])
    )

    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )

    heatmap = cv2.cvtColor(
        heatmap,
        cv2.COLOR_BGR2RGB
    )

    # Overlay
    superimposed = cv2.addWeighted(
        original,
        0.6,
        heatmap,
        0.4,
        0
    )

    # Save Grad-CAM image
    save_dir = os.path.join(
        os.path.dirname(image_path),
        "gradcam"
    )

    os.makedirs(save_dir, exist_ok=True)

    filename = os.path.basename(image_path)

    output_path = os.path.join(
        save_dir,
        filename
    )

    cv2.imwrite(
        output_path,
        cv2.cvtColor(superimposed, cv2.COLOR_RGB2BGR)
    )

    return output_path