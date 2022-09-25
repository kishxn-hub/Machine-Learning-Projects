import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="CarPrice-About",page_icon='car.jpg')

hide_menu_style = """
<style>
#MainMenu {visibility: hidden; }
footer {visibility: hidden; }
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: cyan;'>CAR PRICE PREDICTOR APPLICATION</br>------------------------------------------------</h1>", unsafe_allow_html=True)
def load_lottiefile(filepath: str):
    with open(filepath, "r")as f:
        return json.load(f)

lottie_coding=load_lottiefile("carpic.json")

st_lottie(
    lottie_coding,
    speed=2,
    reverse=False,
    loop=True,
    quality="high",
    height = 0,
    width = 600
)
namee=st.session_state["my_input"]
st.header("Helloo "+str(namee)+" !!")
st.markdown("<h5 style='text-align: left; color: white;'><h4>Thank you for visiting my application.</h4></br>"
            "<h5>Car Price predictor application is an application that is used to predict the current price of a car."
            " With the help of Linear Regression algorithm which is one of the Machine Learning algorithms I developed a model that predicts the output based on the given inputs.</br></br>"
            "Below are the inputs that my model takes:- </br>"
            "1. Name of the comapny.</br>"
            "2. Name of the car model.</br>"
            "3. Year of purchase.</br>"
            "4. Type of fuel.</br>"
            "5. Total number of kilometers driven.</br></br>"
            "Based on these inputs my model will generate the current approximated price. </h5>", unsafe_allow_html=True)
