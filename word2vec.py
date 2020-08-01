import gensim
from gensim.models import word2vec
import csv
import pprint
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import json

model = gensim.models.Word2Vec.load('./ja/ja.bin')
data = []
name = []
count = 0
with open('./words.csv') as f:
    for row in csv.reader(f):
        try:
            data.append(model[row[0]])
            name.append(row[0])
            count+=1
        except:
            continue

pca = PCA(n_components=2)
pca.fit(data)
data_pca = pca.transform(data)

length_data = len(data_pca)

json_string = []
i = 0
while i < length_data:
    json_string.append({'word': name[i], 'x': data_pca[i][0], 'y': data_pca[i][1]})
    i += 1

fw = open('./word.json', 'w')
json.dump(json_string, fw, indent=4)
