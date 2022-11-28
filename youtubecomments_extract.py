import pandas as pd
import googleapiclient.discovery

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyDVokXN7LZbbm38ZbrYb627ZtXKv2bIzbo"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

videoID = "dt_Q03HNbTk"
box = [['Comment', 'Time', 'Reply Count']]

def youtube_comments():
    data = youtube.commentThreads().list(part='snippet', videoId=videoID, maxResults = '100', textFormat='plainText').execute()
    
    for i in data['items']:
        comment = i['snippet']['topLevelComment']['snippet']['textDisplay']
        published_at = i['snippet']['topLevelComment']['snippet']['publishedAt']
        replies = i['snippet']['totalReplyCount']
    
    box.append([comment, published_at, replies])
    totalReplyCount = i['snippet']['totalReplyCount']

    if totalReplyCount > 5:
        parent = i['snippet']['topLevelComment']['id']

        data2 = youtube.comments().list(part = 'snippet', maxResults='100', parentId = parent, textFormat = 'plainText').execute()
        for i in data2['items']:
            comment = i['snippet']['topLevelComment']['snippet']['textDisplay']
            published_at = i['snippet']['topLevelComment']['snippet']['publishedAt']
            replies = i['snippet']['totalReplyCount']
            
            box.append([comment, published_at, replies])
    
    while ("nextPageToken" in data):

        data = youtube.commentThreads().list(part='snippet', videoId=videoID, pageToken=data["nextPageToken"],
                                             maxResults='100', textFormat="plainText").execute()

        for i in data["items"]:
            comment = i['snippet']['topLevelComment']['snippet']['textDisplay']
            published_at = i['snippet']['topLevelComment']['snippet']['publishedAt']
            replies = i['snippet']['totalReplyCount']

            box.append([comment, published_at,replies])

            totalReplyCount = i["snippet"]['totalReplyCount']

            if totalReplyCount > 0:

                parent = i["snippet"]['topLevelComment']["id"]

                data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                                textFormat="plainText").execute()

                for i in data2["items"]:
                    comment = i["snippet"]["textDisplay"]
                    published_at = i["snippet"]['publishedAt']
                    replies = ''

                    box.append([comment, published_at,replies])

    df = pd.DataFrame({'Comment': [i[0] for i in box], 'Time': [i[1] for i in box],
                       'Reply Count': [i[2] for i in box]})

    df.to_csv('youtube-comments.csv', index=False, header=False)

    return "Successful! Check the CSV file that you have just created."

youtube_comments()
