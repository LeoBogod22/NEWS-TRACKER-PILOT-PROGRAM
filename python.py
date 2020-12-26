from newsapi import NewsApiClient
import requests
import json
# Init
import winsound
import sqlite3
duration = 1000  # milliseconds
freq = 440  # Hz
import pyfiglet


import time

data = []

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
    if input == 'Y':
        main()


    if input == 'N':

        system.exit()




def main():

    data = ["FB","AMZN","NFLX"]

    url = "https://stocknewsapi.com/api/v1"

    payload = {
    "tickers": ','.join(data),
    "items": 50,
    "date": "last7days",
    "token": "riowwpicibtsyyo5u9omjajoikcm54wkemwrbroj",
    }

    response = requests.get(url, params=payload)
    if len(response.json()['data'])== 0:

        print("no data")

    else:
        for i in range( len( response.json()['data'] )):
            jprint(response.json()['data'][i]['date'] +  '          title : ' + response.json()['data'][i]['title'] + " news " +  response.json()['data'][i]['text'] +  " sentiment " + response.json()['data'][i]['sentiment'] )
            winsound.Beep(freq, duration)


    time.sleep(3000)


main()
