import pandas as pd
import numpy as np
import re
import string
import pickle

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

with open("artifacts/model/model.pickle", "rb") as file:
    model = pickle.load(file)

with open("artifacts/corpora/stopwords/english", "r") as file:
    stwords = file.read().splitlines()

vocab = pd.read_csv("artifacts/vocabulary.txt", header=None) # if we don't write header = none, it selects first one as name of the column
tokens = vocab[0].tolist()

def remove_punctuations(text):
    if isinstance(text, str):
        return re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    else:
        return ""


def preprocess(txt):

    data = pd.DataFrame([txt], columns=["v2"]) # we should convert this to a data frame in order to apply preprocess actions
    
    data.loc[:, 'v2'] = data['v2'].str.lower()
    data.loc[:, "v2"] = data["v2"].apply(lambda x: re.sub(r"http\S+|www.\S+", "", x))
    data.loc[:, "v2"] = data["v2"].apply(remove_punctuations)
    data.loc[:, "v2"] = data["v2"].apply(lambda x: re.sub(r'\d+', '', x))
    data.loc[:, "v2"] = data["v2"].apply(
        lambda x: " ".join(word for word in x.split() if word.lower() not in stwords)
    )
    data.loc[:, "v2"] = data["v2"].apply(
        lambda x: " ".join(stemmer.stem(x) for x in x.split())
    )

    return data["v2"]


def vectorizor(data_set):
    vectorized_list = []

    for sentence in data_set:
        sentence_list = np.zeros(len(tokens))

        for i in range(len(tokens)):
            if tokens[i] in sentence.split():
                sentence_list[i] = 1

        vectorized_list.append(sentence_list)

    vectorized_list_new = np.asarray(vectorized_list, dtype=np.float32)

    return vectorized_list_new


def get_prediction(vectorized_text_list):
    predicted_result = model.predict(vectorized_text_list)
    if predicted_result == 1:
        return "spam"
    else:
        return "Not a spam"

