from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

import requests
import json
# Init
import winsound
import sqlite3
duration = 1000  # milliseconds
freq = 440  # Hz
import pyfiglet
import time

data = ["AAPL","SQ","PLTR","MSFT","Z","QQQ","SPY","ARKK","TSLA","GME","BABA"]
data_arr = [];

account = "AC2d0b627ca95af759b041f4f22964ef96"
token = "df11d630b6d2a22400901cbd18d34f26"
client = Client(account, token)

class scanarr:
    def __init__(self, title, text, sentiment):
        self.title = title
        self.text = text
        self.sentiment = sentiment

data_arr.append(scanarr('title', 'text', 'sentiment'))

# Ouput the News Description.
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text +' ff /n')

def menu():
    ascii_banner = pyfiglet.figlet_format("NEWS TRACKER PILOT PROGRAM")
    print(ascii_banner)

    for i in data:
        print(i)

    print (' would you like to add stocks to monitor ')
    a = input()

    if a == 'yes':
        print (' Enter stock ticker symbol ')
        b = input()
        data.append(b)
        print (data )
        print("would you like to start monitoring news for these stocks ? type Y/N ")
        c = input()
    if c == 'Y':
        print("starting monitoring for " , data)
        main()
    if c == 'N':
        system.exit()

# get connection to appropriate database
def scanner(resp_data):
    ret = True

    for arr in data_arr:
        if arr.title == resp_data['title']:
            ret = False
        if arr.text == resp_data['text']:
            ret = False

    if ret:
        data_arr.append(scanarr(resp_data['title'], resp_data['text'], resp_data['sentiment']))

    return ret

def main():
    while True:
        data_str = ",".join(data)
        url =  f"https://stocknewsapi.com/api/v1?tickers={data_str}&items=5&date=today&token=myapikey"
        response = requests.get(url)
        if len(response.json()['data'])== 0:
            print("no data")
        else:
            for i in range( len( response.json()['data'] )):

                #winsound.Beep(freq, duration)

                if scanner(response.json()['data'][i]):
                    winsound.Beep(freq, duration)
                    jprint(response.json()['data'][i]['date'] +  '******************************************************************        '' title : ' + response.json()['data'][i]['title'] + "************************** news******************************* " +  response.json()['data'][i]['text'] +  " *********************sentiment************************* " + response.json()['data'][i]['sentiment'] )

                    try:
                        client.messages.create(to="13476070665", from_="+12513103994",
                                               body='Date : ' + response.json()['data'][i]['date'] + '/n' +
                                                    'Title : ' + response.json()['data'][i]['title'] + '/n' +
                                                    'New : ' + response.json()['data'][i]['text'] + '/n' +
                                                    'Sentiment' + response.json()['data'][i]['sentiment'] + '/n')
                        print(client.http_client.last_response.status_code)

                    except TwilioRestException as e:
                        print(e)

        time.sleep(60)

main()
