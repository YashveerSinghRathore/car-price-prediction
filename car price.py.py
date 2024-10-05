import streamlit as st
import pickle
import numpy as np

# Load the saved model and encoders
with open('car_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('le_brand.pkl', 'rb') as file:
    le_brand = pickle.load(file)

with open('le_model.pkl', 'rb') as file:
    le_model = pickle.load(file)

with open('le_fuel_type.pkl', 'rb') as file:
    le_fuel_type = pickle.load(file)

with open('le_transmission.pkl', 'rb') as file:
    le_transmission = pickle.load(file)

st.title("Car Price Estimator")
st.image("https://miro.medium.com/v2/resize:fit:1200/0*Y7SWB-YvdAfsAUYZ.png")

# Collect user input
brand_input = st.selectbox("Select Brand", le_brand.classes_)
model_input = st.selectbox("Select Model", le_model.classes_)
car_age_input = st.number_input("Enter Car Age (years)", min_value=0, max_value=30, value=5)
milage_input = st.number_input("Enter Mileage (Miles)", min_value=0, max_value=500000, value=50000)
fuel_type_input = st.selectbox("Select Fuel Type", le_fuel_type.classes_)
transmission_input = st.selectbox("Select Transmission Type", le_transmission.classes_)

# Encode user input
brand_encoded = le_brand.transform([brand_input])[0]
model_encoded = le_model.transform([model_input])[0]
fuel_type_encoded = le_fuel_type.transform([fuel_type_input])[0]
transmission_encoded = le_transmission.transform([transmission_input])[0]

# Prepare the feature array
features = np.array([[car_age_input, milage_input, brand_encoded, model_encoded, fuel_type_encoded, transmission_encoded]])

# Predict the price
if st.button("Estimate Car Price in USD"):
    predicted_price = model.predict(features)
    st.write(f"Estimated Car Price: ${predicted_price[0]:,.2f}")
