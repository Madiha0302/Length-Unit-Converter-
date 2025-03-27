import streamlit as st

# Dictionary for conversion factors (relative to meters)
conversion_factors = {
    "meters": 1.00,
    "kilometers": 0.001,
    "centimeters": 100,
    "millimeters": 1000,
    "miles": 0.000621371,
    "yards": 1.09361,
    "feet": 3.28084,
    "inches": 39.3701
}

def convert_length(value, from_unit, to_unit):
    """Convert length from one unit to another"""
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Streamlit UI
st.title("Length Unit Converter")

st.sidebar.header("Conversion Settings")
from_unit = st.sidebar.selectbox("From Unit", list(conversion_factors.keys()))
to_unit = st.sidebar.selectbox("To Unit", list(conversion_factors.keys()))

value = st.number_input("Enter length value:", min_value=0.0)

if st.button("Convert"):
    if value == 0:
        st.info("0 in any unit is still 0 in another unit.")
    else:
        result = round(convert_length(value, from_unit, to_unit), 4)
        st.success(f"{value} {from_unit} = {result} {to_unit}")
