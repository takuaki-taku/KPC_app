import streamlit as st
from PIL import Image
import datetime


st.title('Kyotanabe Pickleball Club')
st.caption('これは京田辺ピックルボールクラブメンバーアプリです。')

st.subheader('Description')
st.text('これはPythonで京田辺ピックルボールクラブのメンバー管理を円滑に行うために作ったものです。テスト用です。')
st.text('This is the app for member of Kyotanabe Pickleball Club. It is just for test')

code = '''

import streamlit as st

st.title('Kyotanabe Pickleball Club Member app')

'''

st.code(code,language='python')

#画像
image = Image.open('picklepicture.jpeg')
st.image(image, width=200)


with st.form(key='profile_form'):
    #テキストボックス
    name = st.text_input('name')
    address = st.text_input('address')

    #ラジオボタン
    age_category = st.radio(
            'ages',
            ('Child(Under18)', 'Adult(Over18)'))
    
    #複数選択
    hobby = st.multiselect(
        'hobby',
        ('Playing sports', 'Reading books', 'Programming','Anime・Movies', 'Fishing', 'Cooking') )

    #チェックボックス
    mail_subscribe = st.checkbox('Subscribe the mail magazine')

    #スライダー
    height = st.slider('Height', min_value=110, max_value=210)

    #日付
    start_date = st.date_input(
        'Startdate',
        datetime.date(2024,9,1))

    #カラーピッカー
    color = st.color_picker('themecolor', '#00f900')

    #ボタン
    submit_btn = st.form_submit_button('send')
    cancel_btn = st.form_submit_button('cancel')


    if submit_btn:
        st.text(f'Welcome!{name}san! We sent book to {address}')
        st.text(f'Ages:{age_category}')
        st.text(f'Hobby:{",".join(hobby)}')

