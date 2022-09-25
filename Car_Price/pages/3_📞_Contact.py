import streamlit as st
from PIL import Image
import requests
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="CarPrice-Contact",page_icon='car.jpg')

hide_menu_style = """
<style>
#MainMenu {visibility: hidden; }
footer {visibility: hidden; }
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: cyan;'>Hey! </br>Nice to meet y'all</br>My name is Kishan</br>------------------------------------------------</h1>", unsafe_allow_html=True)
st.info('Currently an Intern in Machine Learning domain with interest in Data Analytics.')
imagg = Image.open('kishan.jpg')
st.image(imagg, width=None)


st.write("📧Email :- itskishankumar8@gmail.com")
st.write("📱Phone :- +91 8105278387")
st.write("🔗LinkedIn :- https://www.linkedin.com/in/kishan-kumar-567249244/")