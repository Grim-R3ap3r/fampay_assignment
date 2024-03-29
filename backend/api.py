
from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)   
CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27018/fampay'
mongo = MongoClient(app.config['MONGO_URI'])

@app.route('/videos', methods=['GET'])
def get_videos():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    search_query = request.args.get('search_query', 'physics') 
    videos = mongo.db.videos.find({'search_query': search_query}).sort('publish_datetime', -1).skip((page - 1) * per_page).limit(per_page)
    video_list = []
    for video in videos:
        video['_id'] = str(video['_id'])
        video_list.append(video)
    return jsonify(video_list)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

