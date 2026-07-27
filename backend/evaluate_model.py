"""
Model Evaluation Script
------------------------
Computes performance metrics (accuracy, precision, recall, F1, ROC-AUC,
confusion matrix) for the trained pneumonia detection model on the test set.

Usage:
    python evaluate_model.py

Requires:
    pip install scikit-learn matplotlib seaborn --break-system-packages
    (tensorflow, numpy already in requirements.txt)

Expects the following folder layout (already present in this repo):
    chest_xray/test/NORMAL/*.jpeg
    chest_xray/test/PNEUMONIA/*.jpeg
    backend/models/pneumonia_model.keras

Label convention (matches training/data_loader.py and app/services/ai_service.py):
    NORMAL    = 0
    PNEUMONIA = 1
    prediction >= 0.5  ->  PNEUMONIA
    
    
To see the Evaluation results, check the console output and the generated files in backend/evaluation_results/:
"""

import os
import numpy as np
import tensorflow as tf
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    roc_curve,
)
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Config — adjust paths only if your folders are laid out differently
# ---------------------------------------------------------------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "pneumonia_model.keras")
TEST_DIR = os.path.join(os.path.dirname(__file__), "..", "chest_xray", "test")
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "evaluation_results")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_test_data():
    """Loads the test set the same way training/data_loader.py does,
    so results reflect exactly what the deployed model sees."""
    test_ds = tf.keras.utils.image_dataset_from_directory(
        TEST_DIR,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode="binary",
        shuffle=False,  
    )
    class_names = test_ds.class_names  # e.g. ['NORMAL', 'PNEUMONIA']
    return test_ds, class_names


def preprocess(images, labels):
    images = tf.cast(images, tf.float32)
    images = tf.keras.applications.efficientnet.preprocess_input(images)
    return images, labels


def run_evaluation():
    print(f"Loading model from: {MODEL_PATH}")
    model = tf.keras.models.load_model(MODEL_PATH)

    print(f"Loading test data from: {TEST_DIR}")
    test_ds, class_names = load_test_data()
    print(f"Classes detected: {class_names}")

    eval_ds = test_ds.map(preprocess)

    # Collect true labels and predicted probabilities
    y_true = []
    y_prob = []

    for images, labels in eval_ds:
        preds = model.predict(images, verbose=0).flatten()
        y_prob.extend(preds.tolist())
        y_true.extend(labels.numpy().flatten().tolist())

    y_true = np.array(y_true)
    y_prob = np.array(y_prob)
    y_pred = (y_prob >= 0.5).astype(int)

    # -----------------------------------------------------------------
    # Metrics
    # -----------------------------------------------------------------
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    roc_auc = roc_auc_score(y_true, y_prob)
    cm = confusion_matrix(y_true, y_pred)
    report = classification_report(y_true, y_pred, target_names=class_names)

    # -----------------------------------------------------------------
    # Print summary
    # -----------------------------------------------------------------
    print("\n" + "=" * 50)
    print("MODEL PERFORMANCE METRICS")
    print("=" * 50)
    print(f"Test samples : {len(y_true)}")
    print(f"Accuracy     : {accuracy:.4f}")
    print(f"Precision    : {precision:.4f}")
    print(f"Recall       : {recall:.4f}")
    print(f"F1 Score     : {f1:.4f}")
    print(f"ROC-AUC      : {roc_auc:.4f}")
    print("\nConfusion Matrix:")
    print(f"                Predicted NORMAL   Predicted PNEUMONIA")
    print(f"Actual NORMAL          {cm[0][0]:<18} {cm[0][1]}")
    print(f"Actual PNEUMONIA       {cm[1][0]:<18} {cm[1][1]}")
    print("\nFull Classification Report:")
    print(report)
    print("=" * 50)

    # -----------------------------------------------------------------
    # Save text report to file
    # -----------------------------------------------------------------
    report_path = os.path.join(OUTPUT_DIR, "metrics_report.txt")
    with open(report_path, "w") as f:
        f.write("MODEL PERFORMANCE METRICS\n")
        f.write("=" * 50 + "\n")
        f.write(f"Test samples : {len(y_true)}\n")
        f.write(f"Accuracy     : {accuracy:.4f}\n")
        f.write(f"Precision    : {precision:.4f}\n")
        f.write(f"Recall       : {recall:.4f}\n")
        f.write(f"F1 Score     : {f1:.4f}\n")
        f.write(f"ROC-AUC      : {roc_auc:.4f}\n\n")
        f.write("Confusion Matrix:\n")
        f.write(str(cm) + "\n\n")
        f.write("Classification Report:\n")
        f.write(report)
    print(f"\nSaved metrics report -> {report_path}")

    # -----------------------------------------------------------------
    # Confusion matrix plot
    # -----------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(cm, cmap="Blues")
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")
    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(cm[i][j]), ha="center", va="center",
                     color="white" if cm[i][j] > cm.max() / 2 else "black")
    fig.colorbar(im)
    fig.tight_layout()
    cm_path = os.path.join(OUTPUT_DIR, "confusion_matrix.png")
    fig.savefig(cm_path, dpi=150)
    plt.close(fig)
    print(f"Saved confusion matrix plot -> {cm_path}")

    # -----------------------------------------------------------------
    # ROC curve plot
    # -----------------------------------------------------------------
    fpr, tpr, _ = roc_curve(y_true, y_prob)
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    ax2.plot(fpr, tpr, label=f"ROC curve (AUC = {roc_auc:.4f})")
    ax2.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Random guess")
    ax2.set_xlabel("False Positive Rate")
    ax2.set_ylabel("True Positive Rate")
    ax2.set_title("ROC Curve")
    ax2.legend(loc="lower right")
    fig2.tight_layout()
    roc_path = os.path.join(OUTPUT_DIR, "roc_curve.png")
    fig2.savefig(roc_path, dpi=150)
    plt.close(fig2)
    print(f"Saved ROC curve plot -> {roc_path}")

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "roc_auc": roc_auc,
        "confusion_matrix": cm.tolist(),
    }


if __name__ == "__main__":
    run_evaluation()