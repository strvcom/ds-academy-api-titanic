#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Web application for STRV DS Academy purpose; written in streamlit.

Run by calling the following comand from your terminal: streamlit run scripts/web_app.py
"""

import os
import pickle

import pandas as pd
import streamlit as st

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../titanic/model.pickle"
)

# set page title
st.set_page_config(page_title="Titanic survival model")

def load_model(model_path: str):
    with open(model_path, "rb") as input_file:
        model = pickle.load(input_file)

    return model

def main():
    # load model
    model = load_model(MODEL_PATH)

    # add title
    st.write("""
    # 🛳️ Titanic survival model
    """)

    # define inputs
    pass_class = st.selectbox(
        "Passanger's class.",
        (1, 2, 3)
    )
    pass_gender = st.selectbox(
        "Passanger's gender.",
        (
            "Male",
            "Female",
            "Non-binary",
            "Transgender",
            "Intersex",
            "Preferred not to say",
        )
    )
    pass_age = st.number_input(
        "Passanger's age.",
        min_value=0,
        max_value=100
    )
    pass_sib_sp_cnt = st.number_input(
        "Number of passanger's siblings/spouses.",
        min_value=0,
        max_value=10
    )
    pass_par_child_cnt = st.number_input(
        "Number of passanger's children/parents.",
        min_value=0,
        max_value=10
    )
    pass_fare = st.number_input(
        "Passanger's fare.",
        min_value=0,
        max_value=600,
    )

    # get input data frame
    passenger_to_predict = pd.DataFrame([
        {
            "class": pass_class,
            "age": pass_age,
            "sib_sp_cnt": pass_sib_sp_cnt,
            "par_child_cnt": pass_par_child_cnt,
            "fare": pass_fare,
            "is_male": int(pass_gender == "Male"),
        },
    ])

    # return survival probability
    survival_proba = model.predict_proba(passenger_to_predict)[0][0] * 100

    st.write(f"""
    ##### Survival probability of passanger is: {survival_proba:,.2f} %
    """)

if __name__ == "__main__":
    main()
