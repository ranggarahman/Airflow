import pandas as pd
import json
from urllib.request import urlopen


def run_youtube_extract():
    box = [['Comment']]
    #data = youtube.commentThreads().list(part='snippet', videoId=videoID, maxResults = '100', textFormat='plainText').execute()

    url = 'https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyDYBkDPEJjh83znf0DTAN_tttKMZiFcynI&textFormat=plainText&part=snippet&videoId=dt_Q03HNbTk&maxResults=100'
    response = urlopen(url)
    data_json = json.loads(response.read())

    for i in data_json['items']:
        comment = i['snippet']['topLevelComment']['snippet']['textDisplay']
        box.append([comment])

    df = pd.DataFrame({'Comment': [i[0] for i in box]})
    df = df.to_json()

    return df
