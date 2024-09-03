import streamlit as st

#画像
image = Image.open('./data/picklepicture.jpeg')
st.image(image, width=200)

code = '''

import streamlit as st

st.title('Kyotanabe Pickleball Club Member app')

'''

st.code(code,language='python')