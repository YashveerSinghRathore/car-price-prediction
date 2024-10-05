# Import the necessary libraries
import streamlit as st
import pickle
import numpy as np

# Load the saved model using pickle
with open('car_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Car Price Estimator")

# Input fields for the car features
year = st.number_input("Year of the Car", 1990, 2024, step=1)
mileage = st.number_input("Mileage of the Car (in KM)", 0, 500000, step=500)
make = st.selectbox("Make of the Car", ["BMW", "Mercedes-Benz", "Toyota", "Honda", "Ford"])

# Convert the car's year to age
car_age = 2024 - year

# Process user input to match model's expectations
# One-hot encoding example for 'Make' (assuming 'BMW', 'Mercedes-Benz', etc. were in the original model)
make_mapping = {
    "BMW": [1, 0, 0, 0, 0],
    "Mercedes-Benz": [0, 1, 0, 0, 0],
    "Toyota": [0, 0, 1, 0, 0],
    "Honda": [0, 0, 0, 1, 0],
    "Ford": [0, 0, 0, 0, 1],
}

# Button to trigger prediction
if st.button("Estimate Car Price"):
    # Prepare the feature vector (age, mileage, make encoding)
    features = [car_age, mileage] + make_mapping[make]
    features = np.array(features).reshape(1, -1)
    
    # Use the loaded model to make a prediction
    predicted_price = model.predict(features)
    
    # Display the predicted price
    st.write(f"Estimated Car Price: ${predicted_price[0]:,.2f}")
