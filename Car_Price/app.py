import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="CarPrice-Home",page_icon='car.jpg')

hide_menu_style = """
<style>
#MainMenu {visibility: hidden; }
footer {visibility: hidden; }
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: cyan;'>Hey !!,</br>My name is Kishan and</br>Welcome to my Web Application !!</br>------------------------------------------------</h1>", unsafe_allow_html=True)
def load_lottiefile(filepath: str):
    with open(filepath, "r")as f:
        return json.load(f)

lottie_coding=load_lottiefile("hello.json")

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="high",
    height = 0,
    width = 450
)
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

st.markdown("<h4 style='text-align: left; color: white;'></br></br>Please provide your name below:-</h4>", unsafe_allow_html=True)
my_input = st.text_input(" ")
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input