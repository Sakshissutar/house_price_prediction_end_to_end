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

st.title("House Price Prediction")
# Inputs
kitchen_area = st.number_input("Kitchen area", value=0.00, format="%.2f", step=0.01)
bath_area = st.number_input("Bath area", value=0.00, format="%.2f", step=0.01)
other_area = st.number_input("Other area", value=0.00, format="%.2f", step=0.01)
extra_area = st.number_input("Extra area", value=0.00, format="%.2f", step=0.01)
extra_area_count = st.number_input("Extra area count", value=0.00, format="%.2f", step=0.01)
year = st.number_input("Year", value=0.00, format="%.2f", step=0.01)
ceil_height = st.number_input("Ceil height", value=0.00, format="%.2f", step=0.01)
floor_max = st.number_input("Floor max", value=0.00, format="%.2f", step=0.01)
floor = st.number_input("Floor", value=0.00, format="%.2f", step=0.01)
total_area = st.number_input("Total area", value=0.00, format="%.2f", step=0.01)
bath_count = st.number_input("Bath count", value=0.00, format="%.2f", step=0.01)
rooms_count = st.number_input("Rooms count", value=0.00, format="%.2f", step=0.01)
gas = st.selectbox("Gas", ["Yes", "No"])
hot_water = st.selectbox("Hot water", ["Yes", "No"])
central_heating = st.selectbox("Central heating", ["Yes", "No"])
extra_area_type_name = st.selectbox("Extra area type name", ["loggia", "balcony"])
district_name = st.selectbox("District name", ["Moskovskij", "Nevskij","Kirovskij","Krasnoselskij","Vyborgskij","Centralnyj","Petrogradskij"])

# Predict button
if st.button("Predict Price",type="primary"):
    data = {
        'Kitchenarea': kitchen_area,
        'Batharea': bath_area,
        'Otherarea': other_area,
        'Extraarea': extra_area,
        'Extraareacount': extra_area_count,
        'Yearnumber': year,
        'Ceilheight': ceil_height,
        'Floormax': floor_max,
        'Floorcount': floor,
        'Totalarea': total_area,
        'Bathcount': bath_count,
        'Roomscount': rooms_count,
        'Gascount': gas,
        'Hotwater': hot_water,
        'Centralheating': central_heating,
        'Extraareatypename': extra_area_type_name,
        'Districtname': district_name,
    }

    df = pd.DataFrame([data])
    numeric_cols = [
    'Kitchenarea','Batharea','Otherarea','Extraarea',
    'Extraareacount','Yearnumber','Ceilheight','Floormax',
    'Floorcount','Totalarea','Bathcount','Roomscount'
    ]
    

    cat_cols = ['Gascount','Hotwater','Centralheating','Extraareatypename','Districtname']

    df[numeric_cols] = df[numeric_cols].astype(float)
    df[cat_cols] = df[cat_cols].astype(str)

    prediction = model.predict(df)

    inputs = {}

    for label in numeric_cols:
        inputs[label] = st.number_input(label, value=0.00, format="%.2f")
    
    if 0.00 in inputs.values():
        st.warning("All fields must be non-zero")
        st.stop()


    st.success(f"Prediction: {prediction[0]}")