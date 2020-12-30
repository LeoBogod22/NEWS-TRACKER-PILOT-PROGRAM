# NEWS-TRACKER-PILOT-PROGRAM


This bot monitors and scans news for certain stocks every 60 seconds. Upon receiving a new article the bot sends an SMS to the user with the title , date and text of the article. 
The bot uses https://stocknewsapi.com/ to filter and search trough articles. lThe bot receives latest stock news from the best news sources. 


The code is written in Python and is meant to run on a

[Google Compute Engine](https://cloud.google.com/compute/) 

[Cloud Natural Language API](https://cloud.google.com/natural-language/) and the
[https://stocknewsapi.com/](https://stocknewsapi.com/) provides stock stada.



The [`scanner`] function defines a callback where incoming news articles  are
handled and starts scanning for news articles
```python

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
```




Follow these steps to run the code yourself: 
 



```bash
pip  install -r requirements.txt
```


Now you can open up a terminal navigate to installed directory  and start scanning for news 

```bash
python python.py 
```


Now you are all set up!
