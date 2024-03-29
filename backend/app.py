from flask import Flask
from pymongo import MongoClient
from youtube_fetch import fetch_youtube_data
import threading

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27018/fampay'
mongo = MongoClient(app.config['MONGO_URI'])

# Start background task
thread = threading.Thread(target=fetch_youtube_data, args=(mongo,))
thread.daemon = True
thread.start()

if __name__ == '__main__':
    app.run(debug=True)
