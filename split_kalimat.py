import nltk
import requests
import re

def add_noun_phrase(kalimats):
    np_1 = find_noun_phrase(kalimats[0])
    np_2 = find_noun_phrase(kalimats[1])
    if np_1 and not np_2:
        kalimats[1] = np_1.group(0).split(' ', 1)[0] + ' ' + kalimats[1]
    if not np_1 and np_2:
        kalimats[0] = np_2.group(0).split(' ', 1)[0] + ' ' + kalimats[0]
    return kalimats

def find_noun_phrase(kalimat):
    url = 'http://127.0.0.1:9000/postagger'
    js = {'string': kalimat}
    r = requests.post(url, json=js)
    data = r.json()
    kalimat_with_postagger = ''
    for k, v in data['data']['map']:
        kalimat_with_postagger += k + ' ' + v + ' '
    regex = re.compile(r'(?:(?:\w+ DT )?(?:\w+ JJ )*)?\w+ (?:N[NP]|PRN)')
    result = re.search(regex, kalimat_with_postagger)
    return result

def split_kalimat(kalimat):
    konjungsi = ['tapi', 'namun', 'hanya', 'cuma', 'cuman', 'walaupun', 'walau', 'meskipun']
    hasil = []
    list_kalimat = nltk.tokenize.word_tokenize(kalimat)
    for i in range(1, len(list_kalimat)):
        for c in konjungsi:
            if list_kalimat[i] == c:
                kalimat_1 = ' '.join(list_kalimat[:i])
                kalimat_2 = ' '.join(list_kalimat[i + 1 - len(list_kalimat):])
                hasil.append(kalimat_1)
                hasil.append(kalimat_2)
                return hasil
    hasil.append(kalimat)
    return hasil


def split_multi_aspek(pair):
    new_pair = []
    for text, opini in pair:
        try:
            kalimat = split_kalimat(text)
            if len(kalimat) > 1 and len(opini) > 1:
                kalimat = add_noun_phrase(kalimat)
                for i in range(0, len(kalimat)):
                    new_pair.append([kalimat[i], [opini[i]]])
            else:
                new_pair.append([text, opini])
        except:
            print("there something error")
    return new_pair
