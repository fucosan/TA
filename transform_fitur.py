import numpy as np
import nltk
from bag_of_word import pos_tagger
import gensim

def transform_bag_of_words(freq_dict, data_opini):
    arr = []
    mx = 0
    for text, opini in data_opini:
        fitur = []
        for word in nltk.tokenize.word_tokenize(text):
            if len(word) > 1:
                fitur.append(freq_dict[word.lower()])
        arr.append(fitur)
        mx = max(len(fitur), mx)

    for i in range(0, len(arr)):
        for j in range(0, mx - len(arr[i])):
            arr[i].append(0.)
    return arr

def transform_pos_tagger(data_opini):
    arr = []
    for text, opini in data_opini:
        fitur = pos_tagger(text)
        arr.append(fitur)

    return arr

model_file_name = "idwiki_word2vec_200.model"
model = gensim.models.Word2Vec.load(model_file_name)
def average_word2vec(word):
    sum = 0
    vals = []
    # ini jangan lupa di cek. ada kata yang gak ada di word2_vec
    if word in model.wv.vocab:
        vals = model.wv.__getitem__(word)

    for val in vals:
        sum += val

    sum /= max(1, len(vals))
    return float(sum)

def transform_word2vec_average(data_opini):
    arr = []
    mx = 0
    for text, opini in data_opini:
        fitur = []
        for word in nltk.tokenize.word_tokenize(text):
            val = average_word2vec(word)
            fitur.append(float(val))
        mx = max(mx, len(fitur))
        arr.append(fitur)

    for i in range(0, len(arr)):
        for j in range(0, mx - len(arr[i])):
            arr[i].append(0.)

    return arr

def transform_word2vec_tfidf(data_opini, tfidf_dict):
    arr = []
    for text, opini in data_opini:
        fitur = []
        for word in nltk.tokenize.word_tokenize(text):
            val = average_word2vec(word)
            tfidf = 1.
            if word in tfidf_dict:
                tfidf = float(tfidf_dict[word])
            fitur.append(float(val) * tfidf)
        arr.append(fitur)
    return arr

def transform_label(data_opini):
    label = []
    for i in range(0, len(data_opini)):
        label.append(data_opini[i][1][0][1])
    return label
