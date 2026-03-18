import streamlit as st
import joblib
import pandas as pd
import re

# Load model
model = joblib.load("salary_model.pkl")

def clean_text(text):
    text = str(text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    return text.lower()

# UI
st.title("💼 Salary Predictor")
st.write("Enter job details to estimate salary")

desc = st.text_area("Job Description")

location = st.text_input("Location")

size = st.selectbox(
    "Company Size",
    [
        "1 to 50 employees",
        "51 to 200 employees",
        "201 to 500 employees",
        "501 to 1000 employees",
        "1001 to 5000 employees",
        "5001 to 10000 employees",
        "10000+ employees",
        "Unknown"
    ]
)

seniority = st.selectbox("Seniority", ["junior", "senior"])

title = st.text_input("Job Title")

if st.button("Predict Salary"):
    
    if not desc.strip():
        st.error("Please enter a job description.")
    else:
        data = pd.DataFrame([{
            "clean_description": clean_text(desc),
            "Location": location if location else "Unknown",
            "Size": size,
            "seniority": seniority,
            "Job Title": title if title else "Unknown"
        }])
        
        prediction = model.predict(data)[0]
        
        st.success(f"💰 Predicted Salary: ${int(prediction):,}")
        
        if location and "india" in location.lower():
            st.warning("Model trained mostly on US data. Prediction may be less accurate.")