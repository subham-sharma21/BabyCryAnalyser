import joblib
import numpy as np
from src.feature_extraction import extract_features

MODEL_PATH = "models/baseline_model.pkl"

_artifact = joblib.load(MODEL_PATH)
_scaler = _artifact["scaler"]
_model = _artifact["model"]


def predict_cry_reason(audio_path):
    features = extract_features(audio_path)
    features = features.reshape(1, -1)

    features_scaled = _scaler.transform(features)
    prediction = _model.predict(features_scaled)[0]

    confidence = None
    if hasattr(_model, "predict_proba"):
        confidence = float(np.max(_model.predict_proba(features_scaled)))

    return prediction, confidence
