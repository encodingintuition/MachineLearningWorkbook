# imports
from flask import Flask, Response, request, render_template, jsonify
import numpy as np

# initialize the flask app
app = Flask(__name__)

@app.route("/")
def home():
    return """
    
        <html>
        <script src='https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.js'></script>
        <link href='https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.css' rel='stylesheet' />

            <body>

            <h1>This is a hard-coded page!</h1>
            
            <div id='map' style='width: 400px; height: 300px;'></div>
            
            <script>
                 mapboxgl.accessToken = 'pk.eyJ1IjoiZW5jb2RpbmdpbnR1aXRpb24iLCJhIjoiY2tpajgyNDUxMDA1YTJ3bzE1ZnY1bXNwbCJ9.TQdJw7s4h0B-Pit2kKm-9g';
                 var map = new mapboxgl.Map({
                 container: 'map', // container ID
                 style: 'mapbox://styles/encodingintuition/ckmmp7p3e1ik217ql167s9a2h', // style URL
                 center: [-73.92332, 43.77172], // starting position [lng, lat]
                  zoom: 9 // starting zoom

                 });
            </script>

                
                
            </body>
        </html>
    """

app.run(debug=True)