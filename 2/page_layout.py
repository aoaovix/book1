import streamlit as st

layout ='centered'
# laout = 'wide'
st.set_page_config(layout=layout)

st.markdown(f'### {layout}')
numbers = ':blue[0]123456789'*10
st.markdown(numbers)