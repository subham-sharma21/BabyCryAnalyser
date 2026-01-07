import pandas as pd
import joblib
from sklearn.svm import SVC

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

DATA_PATH = "data/processed/features.csv"
MODEL_PATH = "models/baseline_model.pkl"


def train_baseline_model():
    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["filename", "label"])
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = SVC(
    kernel="rbf",
    class_weight="balanced",
    probability=True,
    C=1.0,
    gamma="scale"
)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    
    joblib.dump(
        {
            "scaler": scaler,
            "model": model,
            "feature_version": "mfcc+delta+delta2",
            "model_type": "SVM",   # or LogisticRegression
            "version": "v1"
        },
        MODEL_PATH
    )
    print("Model saved to:", MODEL_PATH)


if __name__ == "__main__":
    train_baseline_model()
