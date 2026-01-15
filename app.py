import streamlit as st
import tempfile
import os

from src.inference import predict_cry_reason

st.set_page_config(page_title="Baby Cry Reason Classifier", layout="centered")

st.title("Baby Cry Reason Classifier")
st.write(
    "Upload a baby cry audio file (.wav). "
    "The system will predict the most likely reason for the cry."
)

st.warning(
    "⚠️ This is a research prototype and NOT a medical diagnostic tool."
)

uploaded_file = st.file_uploader("Upload WAV audio", type=["wav"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.audio(uploaded_file, format="audio/wav")

    if st.button("Analyze Cry"):
        with st.spinner("Analyzing audio..."):
            label, confidence = predict_cry_reason(tmp_path)

        st.success(f"Predicted Cry Reason: **{label}**")

        if confidence is not None:
            st.write(f"Confidence: **{confidence:.2f}**")

    os.remove(tmp_path)
