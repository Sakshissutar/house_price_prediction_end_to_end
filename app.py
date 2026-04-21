import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import FunctionTransformer
import joblib

def to_string_func(x):
    return x.astype(str)

@st.cache_resource
def load_model():
    return joblib.load("new_model.pkl")

model = load_model()

st.title("User House Price Prediction")
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
if st.button("Predict Price",type="primary"):
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
    numeric_cols = [
    'kitchen_area','bath_area','other_area','extra_area',
    'extra_area_count','year','ceil_height','floor_max',
    'floor','total_area','bath_count','rooms_count'
    ]
    

    cat_cols = ['gas','hot_water','central_heating','extra_area_type_name','district_name']

    df[numeric_cols] = df[numeric_cols].astype(float)
    df[cat_cols] = df[cat_cols].astype(str)

    prediction = model.predict(df)

    values = []
    for label in numeric_cols:
        val = st.number_input(label, value=None, placeholder=0.0)
        values.append(val)

    if any(v is None or v == 0.0 for v in values ):
        st.warning("All fields must be non-zero")
    else:
        st.success(f"Prediction: {prediction[0]}")