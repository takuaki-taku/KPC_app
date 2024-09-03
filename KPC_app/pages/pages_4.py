import streamlit as st
from PIL import Image

#画像
image = Image.open('./Data/picklepicture.jpeg')
st.image(image, width=200)
