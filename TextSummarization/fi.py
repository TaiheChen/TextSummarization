import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')  # one time execution
import re
import networkx as nx
import io

df = pd.read_csv('./methodFiles/OnClick.csv',encoding = "utf-8", low_memory=False)

sentences = []
for s in df['sentences']:
    # if len(sent_tokenize(s))>10:
    sentences.append(sent_tokenize(s))

# flatten the list
sentences = [y for x in sentences for y in x if len(y) > 10]

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
# print(len(clean_sentences))
word_embeddings = {}
f = open('glove.6B.100d.txt', encoding='utf-8')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    word_embeddings[word] = coefs
f.close()

sentence_vectors = []
for i in clean_sentences:
    if len(i) != 0:
        v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()]) / (len(i.split()) + 0.001)
    else:
        v = np.zeros((100,))
    sentence_vectors.append(v)
# print(sentence_vectors[0])
# print(len(sentence_vectors))

# similarity matrix（all zeros)
sim_mat = np.zeros([len(sentences), len(sentences)])

from sklearn.metrics.pairwise import cosine_similarity

for i in range(len(sentences)):
    print(i)
    for j in range(len(sentences)):
        if i != j:
            sim_mat[i][j] = cosine_similarity(sentence_vectors[i].reshape(1, 100), sentence_vectors[j].reshape(1, 100))[0, 0]

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)
print(scores)
ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

# Specify number of sentences to form the summary
sn = 4

# Generate summary
for i in range(sn):
    print(ranked_sentences[i][1])

print('finish')
