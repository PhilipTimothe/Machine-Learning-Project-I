import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def clean_categories(categories, cutoff):
    category_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            category_map[categories.index[i]] = categories.index[i]
        else:
            category_map[categories.index[i]] = 'Other'
    return category_map

def load_data():
    salary_df = pd.read_csv("../Resources/ds_salaries.csv")
    salary_df = salary_df.drop(['salary', 'salary_currency', 'employee_residence'], axis=1)
    salary_df = salary_df[salary_df["salary_in_usd"].notnull()]