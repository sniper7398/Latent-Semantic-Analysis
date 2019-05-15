#clustering of preprocessed data using K means algorithm
    from sklearn.cluster import KMeans

    num_clusters = 5 #no of cluster are predefined 

    km = KMeans(n_clusters=num_clusters)

    km.fit(X)

    clusters = km.labels_.tolist()
