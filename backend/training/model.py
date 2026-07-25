import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0


IMG_SIZE = (224, 224)


def build_model():

    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
    ])

    inputs = layers.Input(shape=(224, 224, 3))

    x = data_augmentation(inputs)

    x = tf.keras.applications.efficientnet.preprocess_input(x)

    base_model = EfficientNetB0(
        include_top=False,
        weights="imagenet",
        input_tensor=x
    )

    base_model.trainable = True

# Freeze most layers
    for layer in base_model.layers[:-20]:
        layer.trainable = False

    x = layers.GlobalAveragePooling2D()(base_model.output)

    x = layers.Dropout(0.3)(x)

    outputs = layers.Dense(
        1,
        activation="sigmoid"
    )(x)

    model = models.Model(inputs, outputs)

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model