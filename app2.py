import streamlit as st

# Dictionary for conversion factors (relative to meters)

conversion_factors = {
    "meters": 1.00,
    "kilometers": 1000,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Feet": 0.3048,
    "Inches": 0.0254
}

def convert_length(value, from_unit, to_unit):
    """Convert length from one unit to another """
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Streamlit UI
st.title("Length Unit Converter")

st.sidebar.header("Conversion Settings")
from_unit = st.sidebar.selectbox("From Unit", list(conversion_factors.keys()))
to_unit = st.sidebar.selectbox("To Unit", list(conversion_factors.keys()))

value = st.number_input("Enter length value:", min_value=0.0, format="%.4f")

if st.button("Convert"):
    if value >=0:
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
else:
    st.error("Please enter a non-negative value")












