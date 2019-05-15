import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
# from bs4 import BeautifulSoup as Soup
import json

def parseLog(file):
    file = sys.argv[1]
    content = []
    with open(file) as f:
        content = f.readlines()
    content = [json.loads(x.strip()) for x in content]
    # print(content)
    
    data = json.loads(json.dumps(content))
    k=0

# Preprocessing (this involve removing whitespaces, removing end words, removing link etc, lowercasing the data and tokenization)

    content_list = []
    for i in data:
        string_content = ""
        if "contents" in i:
            for all in i["contents"]:
                if "content" in all:
                    # print(str(all["content"]))
                    sample_str = str(all["content"])

                    new_str = ""
                    flag = 0
                    for i in sample_str:
                        if i == "<":
                            flag = 1
                        if i == ">":
                            flag = 0
                        if flag == 0:
                            new_str += i

                    string_content = string_content + new_str
            content_list.append(string_content)
    
    print(content_list[0])

    news_df = pd.DataFrame({'document':content_list})

    # removing everything except alphabets`
    news_df['clean_doc'] = news_df['document'].str.replace("[^a-zA-Z#]", " ")

    # removing null fields
    news_df = news_df[news_df['clean_doc'].notnull()]
    # removing short words
    news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))

    # make all text lowercase
    news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: x.lower())

    stop_words = stopwords.words('english')
    stop_words.extend(['span','class','spacing','href','html','http','title', 'stats', 'washingtonpost'])

    # tokenization
    tokenized_doc = news_df['clean_doc'].apply(lambda x: x.split())

    # remove stop-words
    tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words])
    # print(tokenized_doc)

    # de-tokenization
    detokenized_doc = []
    for i in range(len(tokenized_doc)):
        if i in tokenized_doc:
            t = ' '.join(tokenized_doc[i])
            detokenized_doc.append(t)

    # print(detokenized_doc)

