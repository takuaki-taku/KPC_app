import streamlit as st

#動画
video_file = open('KPC_app/Data/picklevideo1.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)

