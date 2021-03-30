from flask import Flask, Response, request, render_template, jsonify
# basic py libs
import numpy as np
import pandas as import pd
# GIS libs
import geopandas as gpd
from shapely.geometry import Point, Polygon



# initialize the flask app
app = Flask(__name__)

#/api? request=bnb001+43.18+78.18

# route taking in json
@app.route('/api/<x>', methods=['GET', 'POST'])
def add_message(x):
    content = request.get_json(silent=True)


    # Sample JSON the BnBKey from the Json list of Gems
 """                         Example of pasted json object  
     {
        "bnb" : { 
        "bnb_id": bnb001
        "geometry": [ 
             43.16099,
            -76.33380
       ]
     }, 
        "gems" : [
            {"gem_id":xa001, "geometry": [ 42.10901 ,-75.94552] }
            {"gem_id":xa001, "geometry": [ 42.10901 ,-75.94552] }
            {"gem_id":xa001, "geometry": [ 42.10901 ,-75.94552] }
            {"gem_id":xa001, "geometry": [ 42.10901 ,-75.94552] }
            {"gem_id":xa001, "geometry": [ 42.10901 ,-75.94552] }
        ]
     }
"""

# data frame gems

  # INGESTION

    # seporate bnb KEY from rest of file 
    #    create list with Lat and long 


    # seporate gems KEYS & Create DataFrame
    
  # GIS manipulaton
    
    # convert BnB GIS # to GIS point
    geo_point = Point( bnb_geo_address )

    # convert GEMS DataFrame to Geopands
    gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.geometry))

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
            close_gems.append(row['city']) #gemID
        
    # Join all gemIDs to a string csv
    bnds_gems = ','.join(close_gems)

    # do I need to put it in to a json formate to pass back 

    return uuid


