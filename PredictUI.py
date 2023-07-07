import numpy as np
import pickle
import streamlit as st


def load_model():
    with open("Resources/salaries_pred_model.pkl", "rb") as file:
        model_data = pickle.load(file)
    return model_data


model_data = load_model()

regressor = model_data["model"]
experience_level = model_data["experience_level"]
job_title = model_data["job_title"]
company_location = model_data["company_location"]
company_size = model_data["company_size"]


def show_prediction_page():
    st.title("Data Science Salary Predictions")

    st.write("""### Input selection needed to predict salary""")

    experience_levels = ("Executive", "Senior Executive", "Mid Level", "Entry Level")

    experience_l_map = {
        "Executive": "EX",
        "Senior Executive": "SE",
        "Mid Level": "MI",
        "Entry Level": "EN",
    }

    job_titles = (
        "Data Engineer",
        "Data Scientist",
        "Data Analyst",
        "Machine Learning Engineer",
    )

    remote_ratios = (100, 0)

    company_locations = ("United States", "Great Britain")

    company_locations_map = {
        "United States": "US",
        "Great Britain": "GB",
    }

    company_sizes = ("Large", "Medium", "Small")

    company_sizes_map = {"Large": "L", "Medium": "M", "Small": "S"}

    experience_l = st.selectbox("Experience Level", experience_levels)
    job_t = st.selectbox("Job Title", job_titles)
    remote = st.selectbox("Remote Percentage", remote_ratios)
    company_l = st.selectbox("Company Location", company_locations)
    company_s = st.selectbox("Company Size", company_sizes)

    calculate = st.button("Caluculate Salary Prediction")
    if calculate == True:
        X = np.array(
            [
                [
                    experience_l_map[experience_l],
                    job_t,
                    remote,
                    company_locations_map[company_l],
                    company_sizes_map[company_s],
                ]
            ]
        )
        X[:, 0] = experience_level.transform(X[:, 0])
        X[:, 1] = job_title.transform(X[:, 1])
        X[:, 3] = company_location.transform(X[:, 3])
        X[:, 4] = company_size.transform(X[:, 4])
        X = X.astype("int64")

        salary = regressor.predict(X)
        st.subheader(f"Predicted salary is ${salary[0]:.2f}")
