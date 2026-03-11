import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("House Price Prediction App")

st.write("Enter house details to predict price")

# Input fields
overallqual = st.number_input("Overall Quality", min_value=1, max_value=10)

grlivarea = st.number_input("Living Area (sq ft)")

garagecars = st.number_input("Garage Capacity")

totalarea = st.number_input("Total Area")

houseage = st.number_input("House Age")

# Prediction button
if st.button("Predict Price"):

    input_data = np.array([[overallqual, grlivarea, garagecars, totalarea, houseage]])

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")