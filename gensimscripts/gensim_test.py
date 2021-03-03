import pprint
# from helperscripts import read_docx
from gensim.utils import simple_preprocess
from gensim import corpora, models, similarities
from collections import defaultdict
if __name__== "__main__":
    text_corpus = [
        "Human machine interface for lab abc computer applications",
        "A survey of user opinion of computer system response time",
        "The EPS user interface management system",
        "System and human system engineering testing of EPS",
        "Relation of user perceived response time to error measurement",
        "The generation of random binary unordered trees",
        "The intersection graph of paths in trees",
        "Graph minors IV Widths of trees and well quasi ordering",
        "Graph minors A survey",
    ]

    stop_words = set('for a of the and to in'.split(' '))
    texts = [[token for token in simple_preprocess(document) if token not in stop_words] for document in text_corpus]

    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1

    processed_corpus = [[token for token in text if frequency[token]>1] for text in texts]
    pprint.pprint(processed_corpus)

    dictionary = corpora.Dictionary(processed_corpus)
    print(dictionary)

    bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
    pprint.pprint(bow_corpus)

    tfidf = models.TfidfModel(bow_corpus)    
    
    corpus_tfidf = tfidf[bow_corpus]
    # print(corpus_tfidf)

    lsi_model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2)
    corpus_lsi = lsi_model[corpus_tfidf]
    # print(corpus_lsi)

    for doc, as_text in zip(corpus_lsi, text_corpus):
        print(doc, as_text)

    # test query 
    new_query = "graph theory is interesting"
    query_bow = dictionary.doc2bow(simple_preprocess(new_query))
    query_lsi = lsi_model[tfidf[query_bow]]
    print(query_lsi)

    # index it
    index = similarities.MatrixSimilarity(corpus_lsi)
    print(list(enumerate(index[query_lsi])))