## 实战

- https://code.google.com/archive/p/word2vec/
  - 构建词汇表
  - 训练词向量
- https://github.com/dennybritz/cnn-text-classification-tf
- http://radimrehurek.com/2014/02/word2vec-tutorial/ gensim Word2Vec实战

## 训练数据集

- [First billion characters from wikipedia](http://mattmahoney.net/dc/enwik9.zip) (use the pre-processing perl script from the bottom of [Matt Mahoney's page](http://mattmahoney.net/dc/textdata.html))
- [Latest Wikipedia dump](http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2) Use the same script as above to obtain clean text. Should be more than 3 billion words.
- [WMT11 site](http://www.statmt.org/wmt11/translation-task.html#download): text data for several languages (duplicate sentences should be removed before training the models)
- [Dataset from "One Billion Word Language Modeling Benchmark"](http://www.statmt.org/lm-benchmark/1-billion-word-language-modeling-benchmark-r13output.tar.gz) Almost 1B words, already pre-processed text.
- [UMBC webbase corpus](http://ebiquity.umbc.edu/redirect/to/resource/id/351/UMBC-webbase-corpus) Around 3 billion words, more info [here](http://ebiquity.umbc.edu/blogger/2013/05/01/umbc-webbase-corpus-of-3b-english-words/). Needs further processing (mainly tokenization).
- Text data from more languages can be obtained at [statmt.org](http://statmt.org/) and in the [Polyglot project](https://sites.google.com/site/rmyeid/projects/polyglot#TOC-Download-Wikipedia-Text-Dumps).


