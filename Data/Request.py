import requests
import pandas as pd
import json
from pandas import DataFrame

def Recipe_API():
    url = "http://openapi.foodsafetykorea.go.kr/api/f911ad16fdd74ae99534/COOKRCP01/json/1/300"
    response = requests.get(url)
    data = response.json()
    print(data)

Recipe_API()



