from pprint import pprint

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

map_dict = dict()
# Load data
df = pd.read_csv("processed_data-eng-final.csv", delimiter=",", names=["id", "text", "processed_text"])
df = df.iloc[440:480]
tokens_list = list()
for index, row in df.iterrows():
    tokens = row["processed_text"].split(',')
    tokens_list.append(tokens)
    for token in tokens:
        if token not in map_dict:
            map_dict[token] = {f"{index}": 1}
        else:
            if f"{index}" not in map_dict[token]:
                map_dict[token][f"{index}"] = 1
            else:
                map_dict[token][f"{index}"] += 1

for key, val in map_dict.items():
    map_dict[key] = sorted(val.items(), key=lambda x: x[1], reverse=True)

pprint(map_dict)


def store_in_csv():
    df = pd.DataFrame(columns=["token", "doc_id", "frequency"])
    for key, val in map_dict.items():
        for doc_id, frequency in val:
            df = df._append({"token": key, "doc_id": doc_id, "frequency": frequency}, ignore_index=True)
    df.to_csv("inverted_index.csv", index=False)

store_in_csv()