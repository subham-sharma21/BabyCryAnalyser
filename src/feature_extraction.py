import librosa
import numpy as np


def extract_features(file_path, sr=16000, duration=3, n_mfcc=13):
    """
    Extract MFCC-based features from an audio file.
    Returns a fixed-length feature vector.
    """

    # Load audio
    y, orig_sr = librosa.load(file_path, sr=None)

    # Resample if needed
    if orig_sr != sr:
        y = librosa.resample(y, orig_sr=orig_sr, target_sr=sr)

    # Trim silence
    y, _ = librosa.effects.trim(y)

    # Fix audio length
    target_len = sr * duration
    if len(y) < target_len:
        y = np.pad(y, (0, target_len - len(y)))
    else:
        y = y[:target_len]

    # MFCCs
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)

    # Delta features
    mfcc_delta = librosa.feature.delta(mfcc)
    mfcc_delta2 = librosa.feature.delta(mfcc, order=2)

    # Aggregate statistics
    features = np.concatenate(
        [
            np.mean(mfcc, axis=1),
            np.var(mfcc, axis=1),
            np.mean(mfcc_delta, axis=1),
            np.var(mfcc_delta, axis=1),
            np.mean(mfcc_delta2, axis=1),
            np.var(mfcc_delta2, axis=1),
        ]
    )

    return features
