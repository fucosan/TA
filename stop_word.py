import requests

def stop_word(pair):
    url = 'http://127.0.0.1:9000/stopwords'
    js = {'string': ''}
    new_pair = []
    for text, opini in pair:
        js['string'] = text
        result = requests.post(url, json=js).json()
        new_pair.append([result['data'], opini])
    return new_pair
