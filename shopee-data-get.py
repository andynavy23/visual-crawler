import requests
import streamlit as st
import pandas as pd
import re
import math

def main():
    store_id = st.text_input('Enter store_id')
    newest = 0
    header = {
        'if-none-match-': '55b03-e4abf37e9ab8c96283ee4a78ebac1f1b',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    }

    if re.match(r'([0-9]{8})', store_id) != None:
        url = "https://shopee.tw/api/v2/search_items/?by=pop&limit=30&match_id=" + store_id + "&newest=" + str(newest) + "&order=desc&page_type=shop&version=2"
        req = requests.get(url, headers = header)
        data = req.json()
        st.write('The Entered store_id is：', store_id)
        st.write('Crawler status：',req.status_code)
        st.write('Total product count：', data['total_count'])
        page_num = math.ceil(int(data['total_count']) / 30)
        st.write('Total page：', page_num)
        colnames = list(data['items'][0].keys())
        options = st.multiselect('Filter', colnames, colnames)
        st.write('First page data result：')
        dataframe = pd.DataFrame(data['items'])
        st.write(dataframe[options])
    else:
        st.write('Please enter correct store_id')

if __name__ == '__main__':
    main()