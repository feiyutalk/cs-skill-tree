from gensim.models import word2vec
import logging
sentences = word2vec.Text8Corpus('/tmp/text8')
model = word2vec.Word2Vec(sentences, size=200)
model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
