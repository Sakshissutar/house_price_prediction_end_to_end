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

st.title("ITMO House Price Prediction")
# Inputs
kitchen_area = st.number_input("Kitchen area", value=0.00, format="%.2f", step=0.01)
bath_area = st.number_input("Bath area", value=0.00, format="%.2f", step=0.01)
other_area = st.number_input("Other area", value=0.00, format="%.2f", step=0.01)
extra_area = st.number_input("Extra area", value=0.00, format="%.2f", step=0.01)
extra_area_count = st.number_input("Extra area count", value=0.00, format="%.2f", step=0.01)
year = st.number_input("Year", value=0.00, format="%.2f", step=0.01)
ceil_height = st.number_input("Ceil height", value=0.00, format="%.2f", step=0.01)
floor_max = st.number_input("Floor max", value=0.00, format="%.2f", step=0.01)
floor = st.number_input("Floor count", value=0.00, format="%.2f", step=0.01)
total_area = st.number_input("Total area", value=0.00, format="%.2f", step=0.01)
bath_count = st.number_input("Bath count", value=0.00, format="%.2f", step=0.01)
rooms_count = st.number_input("Rooms count", value=0.00, format="%.2f", step=0.01)
gas = st.selectbox("Gas count", ["Yes", "No"])
hot_water = st.selectbox("Hot water", ["Yes", "No"])
central_heating = st.selectbox("Central heating", ["Yes", "No"])
extra_area_type_name = st.selectbox("Extra area type name", ["loggia", "balcony"])
district_name = st.selectbox("District name", ["Moskovskij", "Nevskij","Kirovskij","Krasnoselskij","Vyborgskij","Centralnyj","Petrogradskij"])

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

    if any(data[col] <= 0 for col in numeric_cols):
        st.warning("All fields must be non-zero and positive")
        st.stop()
    
    cat_cols = ['gas','hot_water','central_heating','extra_area_type_name','district_name']

    df[numeric_cols] = df[numeric_cols].astype(float)
    df[cat_cols] = df[cat_cols].astype(str)

    prediction = model.predict(df)



    st.success(f"Prediction: {prediction[0]}")