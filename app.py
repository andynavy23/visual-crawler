import streamlit as st
from shopee_crawler import shopee
from pchome_crawler import pchome

platform_list = ('', 'Shopee', 'PChome')
platform_selectbox = st.sidebar.selectbox('Choose one platform', platform_list)

if platform_selectbox == 'Shopee':
    shopee()
elif platform_selectbox == 'PChome':
    pchome()
else:
    st.header('Choose one platform to see crawler result')