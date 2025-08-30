import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="House Price Prediction", layout="centered")
st.title("🏠 House Price Prediction App")
st.write("Enter details of the house to get estimated price.")

with st.form("house_form"):
    # User-facing inputs (only useful ones)
    bedrooms = st.number_input("Number of Bedrooms", 1, 10, 3)
    bathrooms = st.number_input("Number of Bathrooms", 1.0, 8.0, 2.0, step=0.5)
    living_area = st.number_input("Living Area (sqft)", 500, 10000, 2000, step=50)
    lot_area = st.number_input("Lot Area (sqft)", 500, 100000, 5000, step=500)
    floors = st.number_input("Number of Floors", 1, 3, 1)
    condition = st.slider("Condition of House (1=Poor → 5=Excellent)", 1, 5, 3)
    grade = st.slider("Grade of House (1–13)", 1, 13, 7)
    schools = st.slider("Number of Schools Nearby", 0, 10, 2)
    distance_airport = st.slider("Distance from Airport (km)", 1, 80, 25)
    basement_area = st.number_input("Area of the Basement (sqft)", 0, 5000, 500, step=50)
    house_area_ex = st.number_input("Area of House (Excluding Basement)", 500, 10000, 2000, step=50)
    house_age = st.number_input("House Age (years)", 0, 150, 20)
    living_area_renov = st.number_input("Living Area after Renovation (sqft)", 500, 10000, 2000, step=50)
    lot_area_renov = st.number_input("Lot Area after Renovation (sqft)", 500, 100000, 5000, step=500)
    number_of_views = st.slider("Number of Views", 0, 10, 0)
    renovated = st.selectbox("Renovated?", [0, 1])  
    waterfront = st.selectbox("Waterfront Present?", [0, 1])  

    submitted = st.form_submit_button("Predict Price")

if submitted:
    # Hidden/default values for lat/long (since user won’t enter them)
    latitude = 47.6     # Example: Seattle avg lat (or set based on dataset mean)
    longitude = -122.3  # Example: Seattle avg lon (or set based on dataset mean)

    # Build input DataFrame with all features model expects
    input_data = pd.DataFrame({
        "number of bedrooms": [bedrooms],
        "number of bathrooms": [bathrooms],
        "living area": [living_area],
        "lot area": [lot_area],
        "number of floors": [floors],
        "condition of the house": [condition],
        "grade of the house": [grade],
        "Number of schools nearby": [schools],
        "Distance from the airport": [distance_airport],
        "Area of the basement": [basement_area],
        "Area of the house(excluding basement)": [house_area_ex],
        "Lattitude": [latitude],       # hidden, defaulted
        "Longitude": [longitude],      # hidden, defaulted
        "house_age": [house_age],
        "living_area_renov": [living_area_renov],
        "lot_area_renov": [lot_area_renov],
        "number of views": [number_of_views],
        "renovated": [renovated],
        "waterfront present": [waterfront]
    })

    # Ensure feature order matches training
    input_data = input_data[model.feature_names_in_]

    # Prediction
    prediction_log = model.predict(input_data)[0]
    prediction = round(np.expm1(prediction_log), 2)

    # Category
    if prediction < 500000:
        category = "Cheap 🟢"
    elif 500000 <= prediction < 1500000:
        category = "Moderate 🔵"
    else:
        category = "Luxury 🔴"

    st.success(f"🏠 Predicted House Price: ₹ {prediction:,.0f}")
    st.info(f"💡 Category: {category}")
