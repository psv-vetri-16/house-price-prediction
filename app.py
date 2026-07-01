import streamlit as st
import pickle

with open("model.pkl", "rb") as f:
    model = model.load(f)

st.title("🏠 House Price Prediction")

area = st.number_input("Enter Area (Sq Ft)", min_value=100)

if st.button("Predict Price"):
    prediction = model.predict([[area]])
    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")