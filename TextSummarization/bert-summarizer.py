import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from summarizer import Summarizer
nltk.download('punkt')  # one time execution
import re
import networkx as nx
import io
import torch
df = pd.read_csv('./methodFiles/OnClick.csv',encoding = "utf-8", low_memory=False)

sentences = []
for s in df['sentences']:
    # if len(sent_tokenize(s))>10:
    sentences.append(sent_tokenize(s))

# flatten the list
sentences = [y for x in sentences for y in x if len(y) > 10]
# print(len(sentences))

# remove punctuations, numbers and special characters
clean_sentences = pd.Series(sentences).str.replace("[^a-zA-Z]", " ")

# make alphabets lowercase
clean_sentences = [s.lower() for s in clean_sentences]

nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

# function to remove stopwords
def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

# remove stopwords from the sentences
clean_sentences = [remove_stopwords(r.split()) for r in clean_sentences]
#(len(clean_sentences))
cleansentencesStr = ''
for ss in clean_sentences:
    cleansentencesStr=str(cleansentencesStr)+'. ' + str(ss)
#print(cleansentencesStr)
model = Summarizer()
result = model(cleansentencesStr, min_length=30,ratio=0.01)
#print(result)
full = ''.join(result)
print(sent_tokenize(full))