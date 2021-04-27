import pandas as pd
import numpy as np
import requests
import json
import types

username='taiheChen'
token='8884da6cb184444a4c3d7822fcfee4805db63040'
url = "https://api.github.com/repos/siyamed/android-shape-imageview/issues"
res = requests.get(url, auth=(username,token))
response = res.content


response = json.loads(response)
star = response[0]
star = star['title']

print(star)

