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

def normalisasi(pair):
    mp = dict()
    with open('normalisasi_dict.txt') as myfile:
        for val in myfile:
            y = val.split()
            mp[y[0]] = ' '.join(y[1:])

    new_pair = []
    for text, opini in pair:
        new_sentence = ''
        for word in nltk.tokenize.word_tokenize(text):
            if word in mp:
                new_sentence += mp[word]
            else:
                new_sentence += word
            new_sentence += ' '
        new_pair.append([new_sentence, opini])
    return new_pair

def ina_nlp_formalizer(pair):
    url = 'http://localhost:9000/formalizer'
    js = {'string': ''}
    new_pair = []
    for text, opini in pair:
        js['string'] = text
        result = requests.post(url, json=js).json()
        new_pair.append([result['data'], opini])
    return new_pair
