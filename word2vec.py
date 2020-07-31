import gensim
import sys
word = sys.argv[1]
model = gensim.models.Word2Vec.load('./ja/ja.bin')
print(model[word])