 #tf_idf (to vectorize raw data)

    from sklearn.feature_extraction.text import TfidfVectorizer

    # tfidf vectorizer of scikit learn
    vectorizer = TfidfVectorizer(stop_words=stop_words,max_features=10000, max_df = 0.5,
                                    use_idf = True,
                                    ngram_range=(1,3))

    X = vectorizer.fit_transform(detokenized_doc)

    print(X.shape) # check shape of the document-term matrix

    terms = vectorizer.get_feature_names()
    # print(terms)

