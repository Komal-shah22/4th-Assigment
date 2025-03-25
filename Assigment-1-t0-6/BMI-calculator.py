import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 🟡"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight ✅"
    elif 25 <= bmi < 29.9:
        return "Overweight 🟠"
    else:
        return "Obese 🔴"

# Streamlit UI
st.title("💪 BMI Calculator 📊")

st.write("Enter your weight and height to calculate your Body Mass Index (BMI).")

# User input fields
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=1.0, step=0.1)

# Calculate and display BMI
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        st.success(f"🎯 Your BMI is **{bmi}**")
        st.info(f"📌 Category: **{category}**")
    else:
        st.error("⚠️ Please enter valid weight and height values.")
