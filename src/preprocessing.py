import os
import pandas as pd
from src.feature_extraction import extract_features

DATA_DIR = "data/raw"
OUTPUT_PATH = "data/processed/features.csv"

def build_feature_dataset():
    rows = []

    for label in os.listdir(DATA_DIR):
        label_dir = os.path.join(DATA_DIR, label)
        if not os.path.isdir(label_dir):
            continue

        for file in os.listdir(label_dir):
            if file.lower().endswith(".wav"):
                file_path = os.path.join(label_dir, file)
                try:
                    features = extract_features(file_path)
                    rows.append([file, label] + features.tolist())
                except Exception as e:
                    print("Failed:", file_path)

    feature_count = len(rows[0]) - 2
    columns = ["filename", "label"] + [f"f{i}" for i in range(feature_count)]

    df = pd.DataFrame(rows, columns=columns)
    df.to_csv(OUTPUT_PATH, index=False)

    print("Feature dataset saved to:", OUTPUT_PATH)
    print("Shape:", df.shape)
    print(df["label"].value_counts())

if __name__ == "__main__":
    build_feature_dataset()
