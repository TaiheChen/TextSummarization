import pandas as pd
import numpy as np
import requests
import json
from langdetect import detect
username='taiheChen'
token='8884da6cb184444a4c3d7822fcfee4805db63040'

df = pd.read_csv('AllonClick.csv',encoding = "ISO-8859-1", low_memory=False)
df2 = pd.read_csv('Android_methods.csv')
issueNumber = []
urlArr = []
thirdCol = []
methodAppeared = []
methodsArr = []
titleArr = []
bodyArr = []
engCount = 0
flag = 0
for i in range(0,30):
    methodsArr.append(df2.iloc[i,0])

allArray = []
for i in range(0,len(df)):   #select # of lines
    allArray.append(df.iloc[i,0])

for i in range(0,len(allArray)):
    flag = 0
    print(i)
    print(allArray[i])
    checkJ = 0
    url = str(allArray[i])+'/issues'
    res = requests.get(url, auth=(username, token))
    responseCon = res.content
    response = json.loads(responseCon)
    issuesAccount = len(response)
    for j in range(0,issuesAccount):
        issue = response[j]
        title = issue['title']
        body = issue['body']
        for k in range(0,30):
            if methodsArr[k] in title or methodsArr[k] in body:
                title = title.strip('\r')
                title = title.replace('\n', '.')
                title = title.replace('?', '.')
                title = title.replace(',', '.')
                title = title.replace('，', '.')
                title = title.replace('。', '.')
                title = title.replace('？', '.')
                title = title.replace('；', '.')
                title = title.replace('`', '.')
                title = title.replace("'", ' ')

                body = body.replace('.',' ')
                body = body.replace('\r','.')
                body = body.replace('\n', '.')
                body = body.replace('?', '.')
                body = body.replace(',', '.')
                body = body.replace('，', '.')
                body = body.replace('。', '.')
                body = body.replace('？', '.')
                body = body.replace('；', '.')
                body = body.replace('`', '.')
                body = body.replace('--', '.')
                body = body.replace('.....', '.')
                body = body.replace('....', '.')
                body = body.replace('...', '.')
                body = body.replace('..', '.')
                body = body.replace('.', '.')
                body = body.replace("'", ' ')
                body = body.replace('"', ' ')
                body = title + '. '+ body
                if body and detect(body) == 'en':
                    engCount = engCount+1
                    urlArr.append(allArray[i])
                    issueNumber.append(j)
                    methodAppeared.append(methodsArr[k])
                    titleArr.append(title)
                    bodyArr.append(body)
                flag = flag+1
                break
        if flag>100:
            break

print('--@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print(engCount)
prediction_df = pd.DataFrame(index = None)
prediction_df["url"] = urlArr
prediction_df["issue#"] = issueNumber
prediction_df["methodName"] = methodAppeared
#prediction_df["title"] = titleArr
prediction_df["body"] = bodyArr

prediction_df.to_csv("onclickInclude.csv",index=False,encoding='utf_8_sig' )

