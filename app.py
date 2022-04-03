import csv
import requests

inputs = st.selectbox("Do you care about the stock or sentiment?", ["stock", "sentiment"]) 

if inputs == 'stock':
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo'

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            print(row)

if inputs == 'sentiment':
    url = 'https://www.alphavantage.co/query?function=CONSUMER_SENTIMENT&apikey=demo'
    r = requests.get(url)
    data = r.json()

    print(data)
