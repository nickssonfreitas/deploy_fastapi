import numpy as np
import os
import tempfile
from sklearn.ensemble import RandomForestClassifier
from src.ml.model import (
    inference,
    train_model,
    compute_model_metrics,
    save_model,
    load_model
)

def test_inference():
    # Dados fictícios com pelo menos 5 amostras por classe
    X_train = np.array([
        [1, 2], [3, 4], [5, 6], [7, 8], [9, 10],
        [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]
    ])
    y_train = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])  # 5 amostras por classe

    model = train_model(X_train, y_train)
    preds = inference(model, np.array([[1, 2]]))

    assert len(preds) == 1

def test_compute_model_metrics():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 0, 1, 0]

    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    assert precision == 1.0
    assert recall == 0.6666666666666666
    assert fbeta > 0.7

def test_save_and_load_model():
    model = RandomForestClassifier()
    model.fit([[1, 2], [3, 4]], [0, 1])

    with tempfile.TemporaryDirectory() as tmpdirname:
        model_path = os.path.join(tmpdirname, "test_model.pkl")
        save_model(model, model_path)
        loaded_model = load_model(model_path)

        assert loaded_model is not None
        assert isinstance(loaded_model, RandomForestClassifier)