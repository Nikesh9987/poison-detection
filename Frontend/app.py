import streamlit as st
import joblib
import os

# ==========================
# Load trained model safely
# ==========================

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "toxic_detection_model.pkl"
)

model = joblib.load(MODEL_PATH)

# ==========================
# Page config
# ==========================

st.set_page_config(
    page_title="Poison Detection",
    layout="wide"
)

st.title(" Poison Detection System")

st.write(
    "Enter forensic observations to detect probable toxic substances."
)

# ==========================
# P1 — Clinical Symptoms
# ==========================

cns = st.multiselect(
    "CNS Symptoms",
    [
        "confusion",
        "coma",
        "delirium",
        "anxiety",
        "seizure",
        "headache"
    ]
)

cvs = st.multiselect(
    "CVS Symptoms",
    [
        "tachycardia",
        "bradycardia",
        "hypotension",
        "cardiac arrest"
    ]
)

resp = st.multiselect(
    "Respiratory Symptoms",
    [
        "dyspnoea",
        "respiratory failure",
        "tachypnoea",
        "pulmonary edema"
    ]
)

gi = st.multiselect(
    "GI Symptoms",
    [
        "vomiting",
        "nausea",
        "abdominal pain",
        "diarrhea"
    ]
)

other = st.multiselect(
    "Other/Systemic Symptoms",
    [
        "fever",
        "cyanosis",
        "burning sensation",
        "renal failure"
    ]
)

# ==========================
# P2 — Odour
# ==========================

odour = st.selectbox(
    "Odour",
    [
        "Unknown",
        "None",
        "Petroleum",
        "Garlic",
        "Sweet",
        "Bitter Almond"
    ]
)

# ==========================
# P3 — Route
# ==========================

route = st.selectbox(
    "Route of Exposure",
    [
        "Ingestion",
        "Inhalation",
        "Injection",
        "Dermal",
        "Unknown"
    ]
)


# P4 — Timeline


timeline = st.radio(
    "Symptom Onset Timeline",
    [
        "Rapid",
        "Acute",
        "Subacute",
        "Delayed",
        "Chronic"
    ]
)


# P5 — Sample Type


sample = st.multiselect(
    "Available Sample Type",
    [
        "Blood",
        "Urine",
        "Gastric Lavage",
        "Hair",
        "Nails",
        "Viscera"
    ]
)


# Prediction


if st.button(" Predict Toxic Substance"):

    symptoms = (
        " ".join(cns)
        + " "
        + " ".join(cvs)
        + " "
        + " ".join(resp)
        + " "
        + " ".join(gi)
        + " "
        + " ".join(other)
        + " "
        + odour
    )

    prediction = model.predict([symptoms])[0]

    st.success(
        f"Predicted Toxic Substance: {prediction}"
    )

    st.info(f"""
Confidence Level: HIGH

Route of Exposure:
{route}

Timeline:
{timeline}

Recommended Sample:
{', '.join(sample)}
""")

    st.warning(
        "This is a preliminary forensic decision-support output. "
        "Confirmatory laboratory testing is required."
    )