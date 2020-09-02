import requests
import nltk
import time

def build_dict_normalisasi(pair):
    words = set()
    for text, opini in pair:
        for w in nltk.tokenize.word_tokenize(text):
            words.add(w)
    url = 'http://kateglo.com/api.php'
    params = {'format': 'json', 'phrase': ''}
    new_word = set()
    i = 0
    for w in words:
        if i % 10 == 0:
            print(i)
        i += 1
        params['phrase'] = w
        try:
            requests.get(url, params=params).json()
        except:
            new_word.add(w)
    return new_word

def save_dict(new_word):
    with open('normalisasi_dict.txt', 'w') as f:
        for w in new_word:
            f.write("%s\n" % w)
