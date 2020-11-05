import requests

def stemmer(pair):
    """
    using inanlp for steamming every token
    """
    url = 'http://localhost:9000/stemmer'
    js = {'string': ''}
    new_pair = []
    for text, opini in pair:
        js['string'] = text
        result = requests.post(url, json=js).json()
        new_pair.append([result['data'], opini])
    return new_pair
