import streamlit as st 
import pickle 
import numpy as np 
import sklearn


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Student Result Prediction Tool")
st.write("Enter the required details to predict the result of the Student.")

Student_ID = st.number_input("Enter the Student ID", value=1)

Attendance_Percentage = st.number_input("Enter the Attendance Percentage of Student", min_value=0, max_value=100,value=50)

Homework_Percentage = st.number_input("Enter the Homework Percentage of Student", min_value=0, max_value=100,value=50)

MidTerm_Score = st.number_input("Enter the MidTerm Score of Student", min_value=0, max_value=100,value=50)

Study_Hours = st.number_input("Enter the Study Hours of Student", min_value=0, max_value=24,value=1)

if st.button("Predict Result"):
    prediction = model.predict([[ 
        Student_ID,
        Attendance_Percentage,
        Homework_Percentage,
        MidTerm_Score,
        Study_Hours
    ]])

    label_map = {
        1 za  : "Pass",
        0 : "Fail"
    }

    result = label_map[prediction[0]]

    if result == "Pass":
        st.success(f"The candidate is **{result}**")
    else:
        st.error(f"The candidate is **{result}**")