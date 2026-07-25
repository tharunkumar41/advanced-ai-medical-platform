import tensorflow as tf

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
AUTOTUNE = tf.data.AUTOTUNE

# Mild augmentation suitable for chest X-rays
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomRotation(0.05),
    tf.keras.layers.RandomZoom(0.05),
    tf.keras.layers.RandomContrast(0.05),
])


def prepare_train(images, labels):
    images = tf.cast(images, tf.float32)
    images = data_augmentation(images, training=True)
    return images, labels


def prepare_eval(images, labels):
    images = tf.cast(images, tf.float32)
    return images, labels


def load_datasets(dataset_path):

    train_ds = tf.keras.utils.image_dataset_from_directory(
        f"{dataset_path}/train",
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="binary",
        shuffle=True,
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        f"{dataset_path}/val",
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="binary",
        shuffle=False,
    )

    test_ds = tf.keras.utils.image_dataset_from_directory(
        f"{dataset_path}/test",
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="binary",
        shuffle=False,
    )

    train_ds = (
        train_ds
        .map(prepare_train, num_parallel_calls=AUTOTUNE)
        .prefetch(AUTOTUNE)
    )

    val_ds = (
        val_ds
        .map(prepare_eval, num_parallel_calls=AUTOTUNE)
        .prefetch(AUTOTUNE)
    )

    test_ds = (
        test_ds
        .map(prepare_eval, num_parallel_calls=AUTOTUNE)
        .prefetch(AUTOTUNE)
    )

    return train_ds, val_ds, test_ds