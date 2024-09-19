import streamlit as st
from PIL import Image

#画像
image = Image.open('KPC_app/Data/picklepicture.jpeg')
st.image(image, width=200)
