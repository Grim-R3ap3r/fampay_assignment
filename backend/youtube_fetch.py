import requests
import datetime
import time
from pymongo import MongoClient

# Define a list to store multiple API keys
YOUTUBE_API_KEYS = [
    'AIzaSyA7p5bNb6vhBHQOCnKid1RHTyGaosvL3To',  
    'AIzaSyBGBS9pOCjUGqUnvBV7ZYqFgVisPiAf0ss',
    'AIzaSyBx5ot2SZGO0P8aAZQK1k0HVSDLF7fN_A0',
]
SEARCH_QUERY = 'physics'

def fetch_youtube_data(mongo):
    current_api_key_index = 0
    while True:
        try:
            api_key = YOUTUBE_API_KEYS[current_api_key_index]
            mongo.db.videos.drop()

            response = requests.get(
                f'https://www.googleapis.com/youtube/v3/search?key={api_key}&part=snippet&type=video&order=date&maxResults=50&q={SEARCH_QUERY}'
            )
           
            if response.status_code == 403 and 'quotaExceeded' in response.text:
                # Quota exceeded for current API key, try the next one
                current_api_key_index = (current_api_key_index + 1) % len(YOUTUBE_API_KEYS)
                continue

            data = response.json()
            videos = data.get('items', [])
            for video in videos:
                video_data = {
                    'search_query': SEARCH_QUERY,
                    'title': video['snippet']['title'],
                    'description': video['snippet']['description'],
                    'publish_datetime': datetime.datetime.strptime(video['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                    'thumbnails': [thumbnail['url'] for thumbnail in video['snippet']['thumbnails'].values()],
                    'url': f"https://www.youtube.com/watch?v={video['id']['videoId']}"  
                }
                # Insert into MongoDB
                mongo.db.videos.insert_one(video_data)
            time.sleep(1000)  # Fetch every 1000 seconds
        except Exception as e:
            print(f"An error occurred: {e}")



