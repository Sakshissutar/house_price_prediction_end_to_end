import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("fixed_model.pkl","rb"))

st.title("House Price Prediction")
# Inputs
kitchen_area = st.number_input("kitchen_area")
bath_area = st.number_input("bath_area")
other_area = st.number_input("other_area")
extra_area = st.number_input("extra_area")
extra_area_count = st.number_input("extra_area_count")
year = st.number_input("year")
ceil_height = st.number_input("ceil_height")
floor_max = st.number_input("floor_max")
floor = st.number_input("floor")
total_area = st.number_input("total_area")
bath_count = st.number_input("bath_count")
rooms_count = st.number_input("rooms_count")
gas = st.selectbox("Gas", ["Yes", "No"])
hot_water = st.selectbox("hot_water", ["Yes", "No"])
central_heating = st.selectbox("central_heating", ["Yes", "No"])
extra_area_type_name = st.selectbox("extra_area_type_name", ["loggia", "balcony"])
district_name = st.selectbox("district_name", ["Moskovskij", "Nevskij","Kirovskij","Krasnoselskij","Vyborgskij","Centralnyj","Petrogradskij"])

# Predict button
if st.button("Predict"):
    data = {
        'kitchen_area': kitchen_area,
        'bath_area': bath_area,
        'other_area': other_area,
        'extra_area': extra_area,
        'extra_area_count': extra_area_count,
        'year': year,
        'ceil_height': ceil_height,
        'floor_max': floor_max,
        'floor': floor,
        'total_area': total_area,
        'bath_count': bath_count,
        'rooms_count': rooms_count,
        'gas': gas,
        'hot_water': hot_water,
        'central_heating': central_heating,
        'extra_area_type_name': extra_area_type_name,
        'district_name': district_name,
    }

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    st.success(f"Prediction: {prediction[0]}")