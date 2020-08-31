import nltk
import requests
import re

def add_noun_phrase(kalimats):
    np_1 = find_noun_phrase(kalimats[0])
    np_2 = find_noun_phrase(kalimats[1])
    print(find_noun_phrase(kalimats[1]))
    if np_1 and not np_2:
        kalimats[1] = np_1.group(0).split(' ', 1)[0] + ' ' + kalimats[1]
    if not np_1 and np_2:
        kalimats[0] = np_1.group(0).split(' ', 1)[0] + ' ' + kalimats[0]
    return kalimats

def find_noun_phrase(kalimat):
    url = 'http://127.0.0.1:9000/postagger'
    js = {'string': kalimat}
    r = requests.post(url, json=js)
    data = r.json()
    kalimat_with_postagger = ''
    print(data['data']['map'])
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

def split_multi_aspek(mp):
    for k, v in mp.items():
        kalimats = split_kalimat(v['text'])
        if len(kalimats) > 1:
            kalimats = add_noun_phrase(kalimats)
            temp = mp[k]
            mp[k]['text'] = kalimats[0]
            mp[k]['opinions'].pop(1)
            mp[k + '-1'] = temp
            mp[k + '-1']['text'] = kalimats[1]
            mp[k + '-1']['opinions'].pop(0)
