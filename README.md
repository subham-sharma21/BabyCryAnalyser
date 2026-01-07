# Baby Cry Reason Classification System

An end-to-end machine learning system that classifies infant cry audio into probable causes such as hunger, discomfort, pain, tiredness, and burping using acoustic signal processing and classical ML models.

> ⚠️ This project is a research prototype and is **not** a medical diagnostic tool.

---

## Problem Statement

Infant cries contain acoustic patterns that correlate with different physiological or emotional needs.  
The goal of this project is to analyze short cry audio clips and predict the most likely reason for the cry using audio feature extraction and supervised learning.

---

## Dataset

- Source: Kaggle – Infant Cry Dataset
- Total samples: ~457
- Classes:
  - belly_pain
  - burping
  - discomfort
  - hungry
  - tired

### Dataset Challenges

- Severe class imbalance (some classes have <10 samples)
- High acoustic overlap between cry types
- Short, noisy audio samples

These limitations strongly influence model performance and are explicitly acknowledged.

---

## System Architecture

Audio Input (.wav)
│
▼
Audio Preprocessing (resample · trim · pad)
│
▼
Feature Extraction(MFCC + Δ + ΔΔ)
│
▼
Feature Scaling(StandardScaler)
│
▼
Classifier(Logistic Regression / SVM)
│
▼
Prediction + Confidence

---

## Feature Engineering

- MFCCs (Mel-Frequency Cepstral Coefficients)
- Delta MFCCs (first-order temporal derivatives)
- Delta-Delta MFCCs (second-order derivatives)
- Statistical aggregation (mean, variance)

Final feature vector size: **78**

This captures both spectral and temporal cry characteristics.

---

## Modeling Approach

- Baseline: Logistic Regression with class weighting
- Final Model: Support Vector Machine (RBF kernel, class-balanced)
- Evaluation:
  - Confusion matrix
  - Macro F1-score
  - Minority class recall (prioritized over raw accuracy)

Accuracy is intentionally **not** treated as the primary metric due to class imbalance.

---

## Results (Summary)

- Eliminated majority-class collapse using class weighting
- Achieved meaningful recall on minority classes despite limited data
- Demonstrated correct ML behavior under real-world constraints

The model performance is data-limited, not pipeline-limited.

---

## Inference Application

A Streamlit app is provided to:

- Upload cry audio (.wav)
- Run inference using a locked v1 model
- Display predicted cry reason and confidence score

---

## Ethical Considerations

- Not intended for medical or clinical use
- Results may vary across infants and environments
- Dataset bias and small sample sizes are explicitly acknowledged

---

## Tech Stack

- Python
- librosa
- scikit-learn
- Streamlit
- NumPy, Pandas

---

## Future Work

- Data augmentation for minority classes
- Cross-validation across multiple splits
- CNN-based spectrogram models (v2)
- Mobile-friendly frontend

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

