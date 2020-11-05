import nltk
from nltk.probability import FreqDist
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import requests
#import functools # pakai fungsi reduce

def frequency_distribution(pair):
    """
   take pair (text, opini) and make frequency distribution for each token
    """
    fdist = FreqDist()
    for text, opini in pair:
        for word in nltk.tokenize.word_tokenize(text):
            fdist[word] += 1
    return fdist

def tf_idf_dict(pair):
    """
    create tfidf dictionary for each token
    """
    vectorizer = TfidfVectorizer()
    list_kalimat = []
    for text, opini in pair:
        list_kalimat.append(text)
    x = vectorizer.fit_transform(list_kalimat)
    dict_idf = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))
    return dict_idf

def pos_tagger(kalimat):
    """
    take sentence and return list of probability for each postag in this array
    [Noun, verb, adjective, adverb]
    """
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
    # print(result)
    # print(r['data']['list'])
    #sum = functools.reduce(lambda a,b : a+b, result)
    for i in range(0, 4):
        result[i] /= max(1, len(r['data']['list']))
        #result[i] /= max(1, sum)

    return result


def show_table(fdist):
    """
    take dictionory and show them in pandas data frame
    """
    table_fdist = pd.DataFrame(list(fdist.items()), columns=['Token', 'Frekuensi'])
    table_fdist = table_fdist.sort_values(by=['Frekuensi'], ascending=False)
    return table_fdist

def save_data_opini(data_opini, filename):
    """
    it just save data so that we don't need to iterate the prosess from the start when
    do some testing and training because the prosess may take some time to get it done
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(data_opini))
    print(filename + " saved")

def open_data_opini(filename):
    """
    it's doing what the name tell
    """
    data_opini = []
    with open(filename, 'r') as f:
        data_opini = json.loads(f.read())
    return data_opini
