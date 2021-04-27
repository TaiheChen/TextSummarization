import pandas as pd
import numpy as np
import requests
import json
from langdetect import detect
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

df = pd.read_csv('noNAN4Body.csv',encoding = "utf-8", low_memory=False)

methodName = 'doInBackground'

includedLines = []
includedbodies = []
sentences = []

for i in range(0,len(df)):
    if df.iloc[i,0] == methodName:
        includedLines.append(i)
        includedbodies.append(df.iloc[i,1])

print(len(includedbodies))
for s in includedbodies:
    sentences.append(sent_tokenize(s))


# flatten the list
sentences = [y for x in sentences for y in x if len(y) > 10]

prediction_df = pd.DataFrame(index = None)
prediction_df["sentences"] = sentences


prediction_df.to_csv("./methodFiles/doInBackground.csv",index=False,encoding='utf_8_sig' )

