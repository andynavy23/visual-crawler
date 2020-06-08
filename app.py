import streamlit as st
import requests
import base64
from bs4 import BeautifulSoup
import pandas as pd

# download file
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download csv file</a>'
    return href

text = st.text_input('請輸入日期( 例如: 2020-01-01 ): ')
if text:
    url = 'https://edapromoter.000webhostapp.com/mobo.php?d=' + text
    page = requests.get(url=url)
    soup = BeautifulSoup(page.content, 'html.parser')
    columns = [i.text for i in soup.find_all('tr')[0].find_all('th')]
    rows = []
    row = []
    num = 1
    for i in soup.find_all('td'):
        row.append(i.text)
        num = num + 1
        if num == 26:
            rows.append(row)
            row = []
            num = 1
    df = pd.DataFrame(data=rows, columns=columns)
    st.write('表格抓取如下：')
    st.dataframe(data=df, width=2400, height=1200)
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
