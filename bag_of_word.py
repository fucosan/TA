import nltk
from nltk.probability import FreqDist
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import requests

def frequency_distribution(pair):
    fdist = FreqDist()
    for text, opini in pair:
        for word in nltk.tokenize.word_tokenize(text):
            fdist[word] += 1
    return fdist

def tf_idf_dict(pair):
    vectorizer = TfidfVectorizer()
    list_kalimat = []
    for text, opini in pair:
        list_kalimat.append(text)
    x = vectorizer.fit_transform(list_kalimat)
    dict_idf = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))
    return dict_idf

def pos_tagger(kalimat):
    # return [Noun, verb, adjective, adverb]
    url = 'http://localhost:9000/postagger'
    js = {'string': kalimat}
    r = requests.post(url, json=js).json()
    result = [0, 0, 0, 0]
    for tag in r['data']['list']:
        if tag[0] == 'N':
            result[0] += 1
        elif tag[0] == 'V':
            result[1] += 1
        elif tag[0] == 'J':
            result[2] += 1
        elif tag[0] == 'R':
            result[3] += 1
    for i in range(0, 4):
        result[i] /= max(1, len(r['data']['list']))

    return result


def show_table(fdist):
    table_fdist = pd.DataFrame(list(fdist.items()), columns=['Token', 'Frekuensi'])
    table_fdist = table_fdist.sort_values(by=['Frekuensi'], ascending=False)
    return table_fdist

def save_data_opini(data_opini, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(data_opini))
    print(filename + " saved")

def open_data_opini(filename):
    data_opini = []
    with open(filename, 'r') as f:
        data_opini = json.loads(f.read())
    return data_opini
