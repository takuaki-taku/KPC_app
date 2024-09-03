import streamlit as st

#画像
image = Image.open('./data/picklepicture.jpeg')
st.image(image, width=200)