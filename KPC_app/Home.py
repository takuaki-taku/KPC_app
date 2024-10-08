import streamlit as st
from PIL import Image
import pandas as pd

st.title('Kyotanabe Pickleball Club')
st.caption('これは京田辺ピックルボールクラブメンバーアプリです。')

st.subheader('Description')
st.text('これはPythonで京田辺ピックルボールクラブのメンバー管理を円滑に行うために作ったものです。テスト用です。')
st.text('This is the app for member of Kyotanabe Pickleball Club. It is just for test')


#画像
image = Image.open('KPC_app/Data/KPClogo.png')
st.image(image, width=200)

#データ分析関連
st.subheader('メンバーの増加率')
df = pd.read_csv('KPC_app/Data/averagetemp.csv', index_col='month')
st.line_chart(df)

