# LSA(Latent semantic analysis)

    from sklearn.decomposition import TruncatedSVD
    from sklearn.utils.extmath import randomized_svd

    U, Sigma, VT = randomized_svd(X, 
                                  n_components=5,
                                  n_iter=100,
                              random_state=122)

    # Singular Value decomposition(SVD) is used to decompose matrix obtained from tf_idf
    # svd_model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, random_state=122)

    # svd_model.fit(X)
    
    # print(U.shape)

    for i, comp in enumerate(VT):
        terms_comp = zip(terms, comp)
        sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
        print("Concept "+str(i)+": ")
        for t in sorted_terms:
            print(t[0])
        print(" ")

#Using umap visualizing result in more than 3d

    import umap

    X_topics=U*Sigma
    embedding = umap.UMAP(n_neighbors=25, min_dist=0.5, random_state=12).fit_transform(X_topics)

    plt.figure(figsize=(7,5))
    plt.scatter(embedding[:, 0], embedding[:, 1], 
    c = clusters,
    s = 10, # size
    edgecolor='none'
    )
    plt.show()


if __name__ == "__main__":
    parseLog(sys.argv[1])
