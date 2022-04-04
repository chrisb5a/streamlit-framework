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
    df = df[-10:] 
        #datas['x'] = datas['x'].dt.strftime('%Y-%m-%d')
        
    c = alt.Chart(df).mark_circle().encode(x='time',
        y='close')
    st.altair_chart(c, use_container_width = True)
    
else:

    if str(st.session_state.choice) == 'sentiment' :
        url = 'https://www.alphavantage.co/query?function=CONSUMER_SENTIMENT&apikey=demo'
        r = requests.get(url)
        data = r.json()

        x1 = []
        y = []
        for i in range(len(data['data'])):
            #x.append(datetime.strptime(data['data'][i]['date'], '%Y-%m-%d'))
            x1.append(data['data'][i]['date'])
            y.append(data['data'][i]['value'])
        datas = pd.DataFrame({'x1':x1,'y':y}) 
        #datas['x'] = datas['x'].dt.strftime('%Y-%m-%d')
        datas['x1'] = datas['x1'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
        datas = datas[-10:]
        c = alt.Chart(datas).mark_circle().encode(
        x='x1',
        y='y')
        
        st.altair_chart(c, use_container_width = True)
        #st.write(datas)

        
    else:
        
        st.write('write sentiment or stock!')
