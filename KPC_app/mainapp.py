import streamlit as st
from PIL import Image

st.title('Kyotanabe Pickleball Club')
st.caption('これは京田辺ピックルボールクラブメンバーアプリです。')

st.subheader('Description')
st.text('これはPythonで京田辺ピックルボールクラブのメンバー管理を円滑に行うために作ったものです。テスト用です。')
st.text('This is the app for member of Kyotanabe Pickleball Club. It is just for test')

#画像
image = Image.open('./data/picklepicture.jpeg')
st.image(image, width=200)

