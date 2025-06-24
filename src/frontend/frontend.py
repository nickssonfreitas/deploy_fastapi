import streamlit as st
import requests

st.title("Income Prediction App")

age = st.number_input("Age", value=37)
workclass = st.text_input("Workclass", value="Private")
education = st.text_input("Education", value="HS-grad")
education_num = st.number_input("Education-num", value=10)
marital_status = st.text_input("Marital-status", value="Married-civ-spouse")
occupation = st.text_input("Occupation", value="Prof-specialty")
relationship = st.text_input("Relationship", value="Husband")
race = st.text_input("Race", value="White")
sex = st.text_input("Sex", value="Male")
capital_gain = st.number_input("Capital-gain", value=0)
capital_loss = st.number_input("Capital-loss", value=0)
hours_per_week = st.number_input("Hours-per-week", value=40)
native_country = st.text_input("Native-country", value="United-States")

if st.button("Predict"):
    data = {
        "age": age,
        "workclass": workclass,
        "education": education,
        "education-num": education_num,
        "marital-status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "sex": sex,
        "capital-gain": capital_gain,
        "capital-loss": capital_loss,
        "hours-per-week": hours_per_week,
        "native-country": native_country
    }

    response = requests.post("http://api:8000/data/", json=data)
    result = response.json()

    st.write("Prediction Result:", result["result"])