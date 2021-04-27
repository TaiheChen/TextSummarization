import pandas as pd
import numpy as np
import requests
import json
username='taiheChen'
token='8884da6cb184444a4c3d7822fcfee4805db63040'

df = pd.read_csv('3.csv',encoding = "ISO-8859-1", low_memory=False)

allArray1 = []
allArray = []
for i in range(0,len(df)):
    allArray1.append(df.iloc[i,1])

allArray = list(set(allArray1))
print(len(allArray1))
print(len(allArray))
starArr = []
forkArr = []

for i in range(0,len(allArray)):
    if(i%100 == 0):
        print(i)
    tempUrl = allArray[i]
    response = requests.get(tempUrl, auth=(username, token))
    response = response.content

    response = json.loads(response)
    sApp = response['stargazers_count']
    fApp = response['forks_count']
    starArr.append(sApp)
    forkArr.append(fApp)

prediction_df = pd.DataFrame(index = None)

prediction_df["url"] = allArray
prediction_df["starAmount"] = starArr
prediction_df["forkAmount"] = forkArr
prediction_df.to_csv("rank2.csv",index=False )

