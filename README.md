## Fampay assignment  <img height="50px" width="50px" src="https://github.com/Grim-R3ap3r/fampay_assignment/assets/62543734/cd29dba7-87e0-4114-a8d1-19a95095c84e" /> 

### Project Goal
#### To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Tasks

1. ✅ Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of vid eos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

2. ✅ A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.


## Bonus Points

- ✅ Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.

- ✅ Make a dashboard to view the stored videos with filters and sorting options (optional)


### Screenrecording of the Dashboard
[Screencast from 29-03-24 04:22:07 PM IST.webm](https://github.com/Grim-R3ap3r/fampay_assignment/assets/62543734/1d01aeb4-521e-4de8-bb7e-2e2e608a4351)


## Local Setup

### Backend

```bash
# start mongodb server (in Linux)
sudo systemctl start mongod

#check the status of the mongodb server
sudo systemctl status mongod

mongo mongodb://localhost:27018 (My default port is 27018 so I need to specify the port) or if your default port is 27018 run 
mongo

# Navigate to the backend directory
cd backend

# Run the backend server using nodemon
# to fetch data from youtube API data v3, run the server 
python3 app.py

#to make the api server up and running
python3 api.py
```

## Frontend
```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

## Screenshots of response

##### GET Request to https://localhost:5001/videos?page=2 with search_query = 'travel'
![image](https://github.com/Grim-R3ap3r/fampay_assignment/assets/62543734/0acb467b-c80c-4659-a3b5-a867e4bc0897)




#### Response from the GET Request - After pagination (10 results per query) & Reverse chronological ordered results
```bash
[
  {
    "_id": "6606c123c94298be26657fc6",
    "description": "Spend 4 Days in Bali (really only 2 days since 2 were spent travelling) with us for Levi's 2nd birthday. Get 3 months FREE on ...",
    "publish_datetime": "Thu, 28 Mar 2024 13:40:16 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/xNlmTcbZcPg/default.jpg",
      "https://i.ytimg.com/vi/xNlmTcbZcPg/mqdefault.jpg",
      "https://i.ytimg.com/vi/xNlmTcbZcPg/hqdefault.jpg"
    ],
    "title": "BALI FAMILY VACATION TRAVEL VLOG (for Levi&#39;s birthday!)",
    "url": "https://www.youtube.com/watch?v=xNlmTcbZcPg"
  },
  {
    "_id": "6606c123c94298be26657fc7",
    "description": "",
    "publish_datetime": "Thu, 28 Mar 2024 13:37:13 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/sFbZQ6vtv5Q/default.jpg",
      "https://i.ytimg.com/vi/sFbZQ6vtv5Q/mqdefault.jpg",
      "https://i.ytimg.com/vi/sFbZQ6vtv5Q/hqdefault.jpg"
    ],
    "title": "flight ✈️ കേറി പോയാലോ #travel",
    "url": "https://www.youtube.com/watch?v=sFbZQ6vtv5Q"
  },
  {
    "_id": "6606c123c94298be26657fc8",
    "description": "All ORGANISED USA ROAD TRIP EPISODES: http://bit.ly/TDUSATrip Bhai Bhabi's YouTube Channel: https://bit.ly/2U6s3jS Join ...",
    "publish_datetime": "Thu, 28 Mar 2024 13:30:11 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/LQCJ--k7UXE/default.jpg",
      "https://i.ytimg.com/vi/LQCJ--k7UXE/mqdefault.jpg",
      "https://i.ytimg.com/vi/LQCJ--k7UXE/hqdefault.jpg"
    ],
    "title": "Naye Ghar Ki Kitchen Final Kardi..",
    "url": "https://www.youtube.com/watch?v=LQCJ--k7UXE"
  },
  {
    "_id": "6606c123c94298be26657fc9",
    "description": "travel #luarbiasa #nangis.",
    "publish_datetime": "Thu, 28 Mar 2024 13:23:33 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/olrVssuI-uk/default.jpg",
      "https://i.ytimg.com/vi/olrVssuI-uk/mqdefault.jpg",
      "https://i.ytimg.com/vi/olrVssuI-uk/hqdefault.jpg"
    ],
    "title": "Ditinggal Pas Sayang-sayangnya 💔😳 #travel #luarbiasa #nangis",
    "url": "https://www.youtube.com/watch?v=olrVssuI-uk"
  },
  {
    "_id": "6606c123c94298be26657fca",
    "description": "Traveller Exclusive - Merch: https://newpostcard.creator-spring.com/",
    "publish_datetime": "Thu, 28 Mar 2024 13:00:46 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/qGAB0ITpvx0/default.jpg",
      "https://i.ytimg.com/vi/qGAB0ITpvx0/mqdefault.jpg",
      "https://i.ytimg.com/vi/qGAB0ITpvx0/hqdefault.jpg"
    ],
    "title": "Koreans love Radioactive Juice #travel #foodlover",
    "url": "https://www.youtube.com/watch?v=qGAB0ITpvx0"
  },
  {
    "_id": "6606c123c94298be26657fcb",
    "description": "",
    "publish_datetime": "Thu, 28 Mar 2024 13:00:24 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/V-zD3gAiYEM/default.jpg",
      "https://i.ytimg.com/vi/V-zD3gAiYEM/mqdefault.jpg",
      "https://i.ytimg.com/vi/V-zD3gAiYEM/hqdefault.jpg"
    ],
    "title": "Singapore Layover😏 #song #love #trending #trending #life #viral #explore #shortsvideo #travel #fyp",
    "url": "https://www.youtube.com/watch?v=V-zD3gAiYEM"
  },
  {
    "_id": "6606c123c94298be26657fcc",
    "description": "Pichavaram Mangrove forest tour in Telugu || World's 2nd Largest Mangrove forest || Tamilnadu #trending #viral #travel ...",
    "publish_datetime": "Thu, 28 Mar 2024 12:30:37 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/pC6hKhwtBRA/default.jpg",
      "https://i.ytimg.com/vi/pC6hKhwtBRA/mqdefault.jpg",
      "https://i.ytimg.com/vi/pC6hKhwtBRA/hqdefault.jpg"
    ],
    "title": "Pichavaram  World&#39;s 2nd Largest Mangrove forest  Tamilnadu#trending #viral #travel #mangrove #forest",
    "url": "https://www.youtube.com/watch?v=pC6hKhwtBRA"
  },
  {
    "_id": "6606c123c94298be26657fcd",
    "description": "நண்பர்களுக்கு வணக்கம், Follow Me : https://www.youtube.com/@ShortsVloggs Bus Timing & Shorts Vlogs ...",
    "publish_datetime": "Thu, 28 Mar 2024 12:29:00 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/GzbLdTLQRm8/default.jpg",
      "https://i.ytimg.com/vi/GzbLdTLQRm8/mqdefault.jpg",
      "https://i.ytimg.com/vi/GzbLdTLQRm8/hqdefault.jpg"
    ],
    "title": "💢Chennai Madhavaram MMBT To Salem TNSTC NIGHT ANGLE Bus⁉️ #shorts #travel #bus",
    "url": "https://www.youtube.com/watch?v=GzbLdTLQRm8"
  },
  {
    "_id": "6606c123c94298be26657fce",
    "description": "英國皇室秘聞#梁洛施戒指#李澤楷#李嘉誠#凱特王妃戒指#鑽石冷知識#鑽石4C #凱特王妃患癌#凱特王妃化療#凱特王妃#凱特王妃 ...",
    "publish_datetime": "Thu, 28 Mar 2024 11:42:02 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/9r3-Mc-mFas/default.jpg",
      "https://i.ytimg.com/vi/9r3-Mc-mFas/mqdefault.jpg",
      "https://i.ytimg.com/vi/9r3-Mc-mFas/hqdefault.jpg"
    ],
    "title": "Smart Travel《英國王室秘聞》梁洛施疑戴3000W美元/過億戒指，穿上婚紗X李澤楷，李嘉誠擔憂？ 鑽石冷知識：何謂和深入瞭解 4C + 1C？#凱特王妃戒指 #英國皇室秘聞 #凱特王妃患癌",
    "url": "https://www.youtube.com/watch?v=9r3-Mc-mFas"
  },
  {
    "_id": "6606c123c94298be26657fcf",
    "description": "කඳුයාය මැද දන්න කන්දක් තියෙනවද බලමු... ⛰️ travel moments වටේටම වගා බිම්..#shorts ...",
    "publish_datetime": "Thu, 28 Mar 2024 10:21:33 GMT",
    "search_query": "travel",
    "thumbnails": [
      "https://i.ytimg.com/vi/RwvKp11E3uk/default.jpg",
      "https://i.ytimg.com/vi/RwvKp11E3uk/mqdefault.jpg",
      "https://i.ytimg.com/vi/RwvKp11E3uk/hqdefault.jpg"
    ],
    "title": "කඳුයාය මැද දන්න කන්දක් තියෙනවද බලමු... ⛰️  travel moments වටේටම වගා බිම්..#shorts #travel #srilanka",
    "url": "https://www.youtube.com/watch?v=RwvKp11E3uk"
  }
]
```
