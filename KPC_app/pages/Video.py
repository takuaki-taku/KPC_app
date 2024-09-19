import streamlit as st

st.header('草内小学校体育館でピックルボール')
st.text('草内小学校でピックルボールをプレーしている動画です。')

#動画
video_file = open('KPC_app/Data/picklevideo1.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)

