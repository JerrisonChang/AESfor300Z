# from .. helperscripts import read_docx
import pandas as pd
import numpy as np
from collections import defaultdict
from gensim.utils import simple_preprocess
from gensim import corpora, models, similarities
from gensim.parsing.preprocessing import STOPWORDS

df_train = pd.read_csv('./classifiers/content_hw1/hw1_train_structured.csv')
df_test = pd.read_csv('./classifiers/content_hw1/hw1_test_structured.csv')

documents = df_train['essay body'].to_list()
# print(documents)

def predict_new_essay_score(index: 'lsi index',lsi_model: 'gensim lsi model', dictionary: 'gensim dictionary', essay_body:str, stopwords: set, score_Series: 'pd series') -> int:

    query_bow = dictionary.doc2bow([token for token in simple_preprocess(essay_body) if token not in stopwords])
    # print(query_bow)
    query_lsi = lsi_model[query_bow]
    # print(query_lsi)
    sims = index[query_lsi]
    # print(essay_body[:100])
    top_five = sorted(enumerate(sims), key= lambda item: -item[1])[:10]
    print(top_five)
    scores_of_top_five = [score_Series[i] for i, score in top_five if score != 0]
    print(scores_of_top_five, 'average: ', sum(scores_of_top_five)/len(scores_of_top_five))
    result = sum(scores_of_top_five)/len(scores_of_top_five)
    return round(result)

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
lsi_model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=200) # tweak num_topics
corpus_lsi = lsi_model[corpus_tfidf]
index = similarities.MatrixSimilarity(corpus_lsi)

new_queries = str(df_test['essay body'].to_list()[0])
# query_bow = dictionary.doc2bow([token for token in simple_preprocess(new_queries) if token not in STOPWORDS])
# query_lsi = lsi_model[query_bow]
# sims = index[query_lsi]

# top_five = sorted(enumerate(sims), key= lambda item: -item[1])[:10]
# print(top_five)
# scores_of_top_five = [df_train['content'][i] for i, score in top_five]
# print(scores_of_top_five, 'average: ', sum(scores_of_top_five)/len(scores_of_top_five))
# print(predict_new_essay_score(index, lsi_model, dictionary,new_queries,STOPWORDS, df_train['content']))

new_scores = df_test['essay body'].apply(lambda x: predict_new_essay_score(index, lsi_model, dictionary, str(x), STOPWORDS, df_train['content']))
df_test.insert(2,'predict score', new_scores)

df_test.to_csv('./classifiers/content_hw1/lsi_predict.csv')