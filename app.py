import csv
import requests
import streamlit as st
import altair as alt
from datetime import datetime
import pandas as pd

st.title('sentiment vs stock')

#inputs = st.selectbox("Do you care about the stock or sentiment?", ("stock", "sentiment")) 
#inputs = st.text_input("Do you care about the stock or sentiment?")
st.text_input("Do you care about the stock or sentiment?", key = "choice")
#st.write('ok', st.session_state.choice == 'sentiment', st.session_state.choice)

if st.session_state.choice == 'stock' :
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo'

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
    df = pd.DataFrame(my_list[1:])
    df.rename(columns = {0:'time',1:'open', 2:'high',3:'low',4:'close',4:'volume', 5:'close'})
    
    
else:

    if str(st.session_state.choice) == 'sentiment' :
        url = 'https://www.alphavantage.co/query?function=CONSUMER_SENTIMENT&apikey=demo'
        r = requests.get(url)
        data = r.json()

        x = []
        y = []
        for i in range(len(data['data'])):
            x.append(datetime.strptime(data['data'][i]['date'], '%Y-%m-%d'))
            y.append(data['data'][i]['value'])
        datas = pd.DataFrame({'x':pd.to_datetime(x),'y':y}) 
        c = alt.Chart(datas.reset_index()).mark_line().encode(
        x='index:T',
        y='value:Q')
        
        st.line_chart(datas)

        
    else:
        
        st.write('write sentiment or stock!')
