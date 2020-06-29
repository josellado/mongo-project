from pymongo import MongoClient
import folium
import pandas as pd
import matplotlib
import numpy as np
import pandas as pd
import os
import requests
import json
from pandas.io.json import json_normalize
import re
from dotenv import load_dotenv
load_dotenv()

def transformToGeoPoint(s):
    if np.isnan(s.latitude) or np.isnan(s.longitude):
        return None
    return {
        "type":"Point",
        "coordinates":[s.longitude, s.latitude]
    }
    

def geocode(address):
    res = requests.get(f"https://geocode.xyz/{address}", params={"json":1})
    data = res.json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }