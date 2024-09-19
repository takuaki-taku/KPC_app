import streamlit as st
st.header('Language')
st.subheader('Python')
st.text('This web app is made by python')

code = '''

import streamlit as st

st.title('Kyotanabe Pickleball Club Member app')

'''

st.code(code,language='python')
