import streamlit as st
import requests
import pandas as pd

def pchome():
    search_name = st.text_input('Enter search_name')
    page_num = 1
    if search_name != '':
        url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=' + search_name + '&page=' + str(page_num) + '&sort=sale/dc'
        req = requests.get(url)
        data = req.json()
        st.write('The Entered search_name is：', search_name)
        st.write('Crawler status：',req.status_code)
        st.write('Total product count：', data['totalRows'])
        st.write('Total page：', data['totalPage'])
        colnames = list(data['prods'][0].keys())
        options = st.multiselect('Filter', colnames, colnames)
        st.write('First page data result：')
        dataframe = pd.DataFrame(data['prods'])
        st.write(dataframe[options])
    else:
        st.write('Please enter search_name')

if __name__ == '__main__':
    pchome()
