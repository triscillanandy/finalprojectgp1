import streamlit as st
import pickle
import numpy as np

import warnings
warnings.filterwarnings('ignore')

def load_model():
    with open('salary_prediction_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

rfr = data["model"]
le_education = data["le_education"]
le_job = data["le_job"]

def show_predict_page():
    st.title("Job Salary Prediction")
    st.write(""" We need some information to predict the salary""")

    education_levels = (
        "High School",
        "Bachelor's",
        "Master's",
        "PhD",
    )
    job_titles = [
    "Software Engineer",
    "Data Scientist",
    "Software Engineer Manager",
    "Data Analyst",
    "Senior Project Engineer",
    "Product Manager",
    "Full Stack Engineer",
    "Marketing Manager",
    "Back end Developer",
    "Senior Software Engineer",
    "Front end Developer",
    "Marketing Coordinator",
    "Junior Sales Associate",
    "Financial Manager",
    "Marketing Analyst",
    "Software Developer",
    "Operations Manager",
    "Human Resources Manager",
    "Director of Marketing",
    "Web Developer",
    "Research Director",
    "Product Designer",
    "Content Marketing Manager",
    "Sales Associate",
    "Senior Product Marketing Manager",
    "Director of HR",
    "Research Scientist",
    "Marketing Director",
    "Sales Director",
    "Senior Data Scientist",
    "Junior HR Generalist",
    "Junior Software Developer",
    "Receptionist",
    "Director of Data Science",
    "Sales Manager",
    "Digital Marketing Manager",
    "Junior Marketing Manager",
    "Junior Software Engineer",
    "Human Resources Coordinator",
    "Senior Research Scientist",
    "Senior Human Resources Manager",
    "Senior HR Generalist",
    "Junior Web Developer",
    "Junior Sales Representative",
    "Financial Analyst",
    "Sales Executive",
    "Sales Representative",
    "Front End Developer",
    "Junior HR Coordinator",
    "Junior Data Analyst"
]


    education_level = st.selectbox("Education Level", education_levels)
    job_title = st.selectbox("Job Title", job_titles)
    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")
    if ok:
        # Encode the selected education level and job title
        education_encoded = le_education.transform([education_level])[0]
        job_encoded = le_job.transform([job_title])[0]

        # Create features array for prediction
        X = np.array([[education_encoded, job_encoded, experience]])
        X = X.astype(float)

        # Predict the salary
        salary = rfr.predict(X)

        # Display the predicted salary
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

# Run the app
if __name__ == '__main__':
    show_predict_page()
