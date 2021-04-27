import pandas as pd
import numpy as np
import requests
import json
username='taiheChen'
token='8884da6cb184444a4c3d7822fcfee4805db63040'

df = pd.read_csv('rank1fork1.csv',encoding = "ISO-8859-1", low_memory=False)
df2 = pd.read_csv('Android_methods.csv')
issueNumber = []
urlArr = []
thirdCol = []
methodAppeared = []
methodsArr = []
textArr = []
ppText = []
pText = []
awText = []
awawText = []
for i in range(0,30):
    methodsArr.append(df2.iloc[i,0])

allArray = []
for i in range(0,len(df)):
    allArray.append(df.iloc[i,0])

for i in range(0,len(allArray)):
    print(i)
    print(allArray[i])
    checkJ = 0
    url = str(allArray[i])+'/issues'
    res = requests.get(url, auth=(username, token))
    responseCon = res.content
    response = json.loads(responseCon)
    issuesAccount = len(response)
    for j in range(0,issuesAccount):
        #print(j)
        issue = response[j]
        title = issue['title']
        body = issue['body']
        for k in range(0,30):
            if methodsArr[k] in title:
                print(j)
                methodAppeared.append(methodsArr[k])
                urlArr.append(allArray[i])
                issueNumber.append(j)
                thirdCol.append('title')
                textArr.append(title)
                ppText.append('111')
                pText.append('111')
                awText.append('111')
                awawText.append('111')
                k=29
                break
            if methodsArr[k] in body:
                print(j)
                body = body.strip('\r')
                body = body.replace('\n', ',')
                body = body.replace('?', ',')
                body = body.replace(',,', ',')
                body = body.replace(',,,', ',')
                body = body.replace(',,,,', ',')

                urlArr.append(allArray[i])
                issueNumber.append(j)
                methodAppeared.append(methodsArr[k])
                thirdCol.append('body')

                spl = body.split(',')
                for x in range(0,len(spl)):
                    if methodsArr[k] in spl[x]:
                        ind = x
                        textArr.append(spl[x])
                        if (x==0):
                            ppText.append('999')
                            pText.append('999')
                        if(x==1):
                            ppText.append('999')
                            pText.append(spl[x-1])
                        if (x>1):
                            ppText.append(spl[x - 2])
                            pText.append(spl[x - 1])
                        if((len(spl)-x)==1):
                            awText.append('999')
                            awawText.append('999')
                        if((len(spl)-x)==2):
                            awawText.append('999')
                            awText.append(spl[x + 1])
                        if ((len(spl) - x) > 2):
                            awawText.append(spl[x+2])
                            awText.append(spl[x + 1])
                        break
                k=29
                break
        #if checkJ == 1:
            #break
        #thirdCol.append('body')
print(len(ppText))
print(len(pText))
print(len(textArr))
print(len(awText))
print(len(awawText))
prediction_df = pd.DataFrame(index = None)
prediction_df["url"] = urlArr
prediction_df["issue#"] = issueNumber
prediction_df["position"] = thirdCol
prediction_df["methodName"] = methodAppeared
prediction_df["pptext"] = ppText
prediction_df["ptext"] = pText
prediction_df["text"] = textArr
prediction_df["awtext"] = awText
prediction_df["awawtext"] = awawText
prediction_df.to_csv("new4.csv",index=False )

