import pandas as pd
import numpy as np
import requests
#import DataFrame
username='taiheChen'
token='8884da6cb184444a4c3d7822fcfee4805db63040'

#-------------------------------------------------------------

df = pd.read_csv('nameAndApiOnly.csv',encoding = "ISO-8859-1", low_memory=False)
validArr = []
methodsArr = []
df2 = pd.read_csv('Android_methods.csv')
for i in range(0,30):
    methodsArr.append(df2.iloc[i,0])
finalArr = []
#---------------------------------------------------------------
try:
    for i in range(0,316522):#316522
        if (i%100 == 0):
            print(i)
            print(len(finalArr))
        temp = str(df.iloc[i,1])
        url = temp+'/issues'
        response = requests.get(url, auth=(username,token))
        content = response.content

        if(len(content)>200):
            print(content)
            for j in range(0,30):
                #print(methodsArr[j])
                #print(content)
                if methodsArr[j].encode() in content:
                    finalArr.append(temp)
                    j=29

finally:
    prediction_df = pd.DataFrame(index = None)
    prediction_df["id"] = [i for i in range(0, len(finalArr))]
    prediction_df["output"] = finalArr
    prediction_df.to_csv("3.csv",index=False )

