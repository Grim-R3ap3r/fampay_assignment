
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles.css'; 


function App() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    // Fetch videos from Flask API endpoint
    axios.get('http://localhost:5001/videos')
      .then(response => {
        console.log("response", response.data)
        setVideos(response.data);
      })
      .catch(error => {
        console.error('Error fetching videos:', error);
      });
  }, []);
  console.log("videos", videos)
  return (
    <div className="bg-gray-100 min-h-screen">
      <div className="container mx-auto py-8">
        <h1 className="text-3xl font-bold mb-4">Latest Videos</h1>
        <div className="grid gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
          {videos.map(video => (
            <div key={video._id} className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-xl font-semibold mb-2">{video.title}</h2>
              <p className="text-gray-700 mb-2">{video.description}</p>
              <p className="text-gray-600 mb-2">Published: {new Date(video.publish_datetime).toLocaleString()}</p>
              <div className="flex justify-center">
               
                  <img key={video.thumbnails[1]} src={video.thumbnails[1]} alt="Thumbnail" className="w-full h-full rounded-lg mr-2" />
               
              </div>
              <p className="text-blue-500 mt-2">
                <button>
                <a href={video.url} target="_blank" rel="noopener noreferrer">Watch Video</a>
                </button>
              
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
