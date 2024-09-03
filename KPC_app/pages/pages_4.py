import streamlit as st
from PIL import Image

#画像
image = Image.open('./data/picklepicture.jpeg')
st.image(image, width=200)
