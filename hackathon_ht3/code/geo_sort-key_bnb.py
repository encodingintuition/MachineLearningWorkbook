from flask import Flask, Response, request, render_template, jsonify
# basic py libs
import numpy as np
import pandas as pd
import json
# GIS libs
import geopandas as gpd
from shapely.geometry import Point, Polygon




# initialize the flask app
app = Flask(__name__)

#/api? request=bnb001+43.18+78.18

# route taking in json
@app.route('/data')
def data():
    latitude = request.args.get('lat')
    longitude = request.args.get('long')
    #bnb_id = request.args.get('bnbid')
    print(latitude)
    print(longitude)



    # Sample JSON the BnBKey from the Json list of Gems


    # INGESTION
    # longitude = -73.9233
    # latitude = 43.7717

    bnb_geo_address = [ float(longitude),float(latitude) ]
  

    # Data for GEMS hard coded 
    data = {'gem_id': [1001, 1002,1003,1004,1005,1006],
        'latitude': [43.771663, 43.779007, 43.747417, 43.747417, 43.771755, 43.779534],
        'longitude': [-73.930204, -73.95124, -73.851914, -73.851914, -73.924258, -73.950862]
       }

    df = pd.DataFrame(data = data)
    
  # GIS manipulaton
    
    # convert BnB GIS # to GIS point
    geo_point = Point( bnb_geo_address )

    # convert GEMS DataFrame to Geopands
    gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.longitude, df.latitude))

    # Increase radius of gis point to incude more area
    geo_pointB = geo_point.buffer(.1) 
    
    # loop of Masking 
    c = 0
    close_gems = []

    # loop through rows in dataframe
    for i, row in gdf.iterrows():
        # Check if GEM is in radius 
        if geo_pointB.contains(row['geometry']):
              print('yes')
              # create list of geo points 
              close_gems.append(row['gem_id'])
        
    # Join all gemIDs to into a JSON
    json_gems = json.dumps(close_gems)
    return json_gems

app.run(debug=True)

