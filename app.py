import csv
import requests
import streamlit as st

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
        for row in my_list:
            st.write(row)
  else:

    if str(st.session_state.choice) == 'sentiment' :
        url = 'https://www.alphavantage.co/query?function=CONSUMER_SENTIMENT&apikey=demo'
        r = requests.get(url)
        data = r.json()

        st.write(data)
     else:
        
        st.write('write sentiment or stock!')
