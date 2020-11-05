import nltk
import requests
import re

def add_noun_phrase(kalimats):
    np = [] # contain noun phrase or zero
    for sen in kalimats:
        x = find_noun_phrase(sen)
        np.append(x)

    for i in range(0, len(np)):
        if i > 0:
            if not np[i] and np[i - 1]:
                list_kalimat = nltk.tokenize.word_tokenize(kalimats[i])
                list_kalimat.insert(1, np[i - 1].group(0).split(' ', 1)[0])
                kalimats[i] = ' '.join(list_kalimat)
            continue
        if i < len(np) - 1:
            if np[i + 1] and not np[i]:
                z = 1 if i > 0 else 0
                list_kalimat = nltk.tokenize.word_tokenize(kalimats[i])
                list_kalimat.insert(z, np[i + 1].group(0).split(' ', 1)[0])
                kalimats[i] = ' '.join(list_kalimat)

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

def is_valid_sentence(sentence):
    """
    check if sub sentences between conjungtion is valid sentence or not
    """
    num_of_word = len([word for word in sentence if word.isalpha()])
    if num_of_word == 0:
        return False
    if num_of_word == 1:
        rl = 'http://127.0.0.1:9000/postagger'
        js = {'string': kali}
        r = requests.post(url, json=js)
        data = r.json()
        if dasta['data']['list'] == 'JJ':
            return True
        if data['data']['list'][0] == 'N':
            if "saya" in sentence:
                return False
            return True
    # more than one word
    return True


def split_kalimat(kalimat):
    konjungsi = ['tetapi', 'tapi', 'namun', 'hanya', 'cuma', 'cuman', 'walaupun', 'walau', 'meskipun']
    hasil = []
    #kalimat = re.sub(r'^\"', r'', kalimat)
    #kalimat = re.sub(r'^\'', r'', kalimat)
    list_kalimat = nltk.tokenize.word_tokenize(kalimat)
    sent_so_far = []
    for i in range(0, len(list_kalimat)):
        if list_kalimat[i] in konjungsi:
            if is_valid_sentence(sent_so_far):
                hasil.append(' '.join(sent_so_far))
            sent_so_far = []
        sent_so_far.append(list_kalimat[i])

    if is_valid_sentence(sent_so_far):
        hasil.append(' '.join(sent_so_far))

    return hasil

def split_multi_aspek(pair):
    new_pair = []
    for text, opini in pair:
        try:
            kalimat = split_kalimat(text)
            if len(kalimat) > 1:
                kalimat = add_noun_phrase(kalimat)
                if len(kalimat) != len(opini):
                    print("tidak sama")
                for i in range(0, len(kalimat)):
                    new_pair.append([kalimat[i], [opini[i]]])
            else:
                new_pair.append([text, opini])
        except:
            print("there something error")
    return new_pair
