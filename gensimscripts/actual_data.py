#%%
# from .. helperscripts import read_docx
import pandas as pd
import numpy as np
from collections import defaultdict
from gensim.utils import simple_preprocess
from gensim import corpora, models, similarities
from gensim.parsing.preprocessing import STOPWORDS
#%%
df_train = pd.read_csv('./classifiers/content_hw1/hw1_train_structured.csv')
df_test = pd.read_csv('./classifiers/content_hw1/hw1_test_structured.csv')

documents = df_train['essay body'].to_list()
# print(documents)

tokenized_documents = [[token for token in simple_preprocess(str(document)) if token not in STOPWORDS] for document in documents]

frequency = defaultdict(int)
for doc in tokenized_documents:
    for token in doc:
        frequency[token] += 1

corpus = [[token for token in doc if frequency[token] > 3] for doc in tokenized_documents]
dictionary = corpora.Dictionary(corpus)
corpus_bow = [dictionary.doc2bow(doc) for doc in corpus]
tfidf = models.TfidfModel(corpus_bow)
corpus_tfidf = tfidf[corpus_bow]
lsi_model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10) # tweak num)topics
corpus_lsi = lsi_model[corpus_tfidf]
index = similarities.MatrixSimilarity(corpus_lsi)
#%%
new_queries = df_test['essay body'].to_list()[1]
query_bow = dictionary.doc2bow([token for token in simple_preprocess(new_queries) if token not in STOPWORDS])
query_lsi = lsi_model[query_bow]
sims = index[query_lsi]

top_five = sorted(enumerate(sims), key= lambda item: -item[1])[:10]
# print(top_five)
scores_of_top_five = [df_train['content'][i] for i, score in top_five]
print(scores_of_top_five)

