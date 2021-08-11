# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# https://developers.google.com/explorer-help/guides/code_samples#python


# Module Dependencies
import os
import json
import csv
from dotenv import load_dotenv
import googleapiclient.discovery


API_key=os.getenv('API_key')
video_ID=os.getenv('video_ID')


# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = API_key

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

request = youtube.commentThreads().list(
    part = "id,snippet",
    maxResults = 100,
    order = "time",
    videoId = video_ID,
)
response = request.execute()
    
# print(response)

comments=[]
for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
    comments.append([comment.strip(),1])
    
# print(comments)

with open("data.csv", 'a', encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerows(comments)

print("Comments Scrapped Successfully...")





