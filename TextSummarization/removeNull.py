import pandas as pd
import numpy as np
import requests
import json
from langdetect import detect
# -*- coding: utf-8 -*-
df = pd.read_csv('processedIncludingVoid.csv',encoding = "utf-8", low_memory=False)
bodyArr = []
titleArr = []
totalArr=[]
methodArr=[]
print(type(str(df.iloc[5,4])))

for i in range(0,len(df)):   #select # of lines
    bodyArr.append(df.iloc[i,4])
    titleArr.append(df.iloc[i,5])

    if str(bodyArr[i]) != 'nan' and detect(bodyArr[i]) == 'en':
        methodArr.append(df.iloc[i, 2])
        body =str(titleArr[i]) + '. ' + str(bodyArr[i])
        body = body.replace("'", ' ')
        body = body.replace('"', ' ')
        body = body.replace('<', ' ')
        body = body.replace('>', ' ')
        body = body.replace('(', ' ')
        body = body.replace(')', ' ')
        body = body.replace('?', '.')
        body = body.replace('!', '.')
        body = body.replace(':', ' ')
        body = body.replace('：', ' ')
        body = body.replace(';', ',')
        totalArr.append(body)


prediction_df = pd.DataFrame(index = None)
prediction_df["method"] = methodArr
prediction_df["body"] = totalArr
print(totalArr[2])

prediction_df.to_csv("noNAN4Body.csv",index=False,encoding='utf_8_sig' )