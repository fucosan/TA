import pandas as pd
import nltk
import re
import xml.dom.minidom
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape
from time import gmtime, strftime, localtime
import os
import errno

links = ['../data/raw/2017.xlsx', '../data/raw/2016.xlsx']
datas = {}


def load_data():
    """
    this function will load all data and change it ito data frame
    """
    for link in links:
        d = pd.read_excel(link)
        d = pd.DataFrame(data=d)
        datas[link] = d


def remove_an_necessary_column():
    """
    Remove an important columns like Email, Name,  Nim, Timestamp
    etc.
    """
    remove_list = ['NIM', 'Email', 'Timestamp']
    for k, v in datas.items():
        x = v
        for rl in remove_list:
            if rl in v.columns:
                x = x.drop(columns=[rl])
        datas[k] = x


def merge_data():
    """
    merge data into one list
    """
    for k, v in datas.items():
        datas[k] = v.stack().tolist()

def compare_2017_and_2016(s1, s2):
    if isinstance(s1, str) == False:
        return False

    if isinstance(s2, str) == False:
        return False

    list_s1 = nltk.word_tokenize(s1)
    list_s2 = nltk.word_tokenize(s2)
    mn_sz = min(len(list_s1), len(list_s2))
    cnt = 0
    for i in range(0, mn_sz):
        if list_s1 == list_s2:
            cnt+= 1
    if cnt / mn_sz >= 0.9:
        return True
    return False

def remove_2017_and_2016():
    """
    remove review if there is the same review from 2017 and 2016
    """
    res = []
    for r2017 in datas['../data/raw/2017.xlsx']:
        ok = 1;
        for r2016 in datas['../data/raw/2016.xlsx']:
            if compare_2017_and_2016(r2017, r2016) == True:
                ok = 0
                break
        if ok == 1:
            res.append(r2017)

    return res

def case_fold():
    """
    turn all letter into lower case
    """
    for k, v in datas.items():
        x = []
        for sen in v:
            x.append(sen.lower())
        datas[k] = x


def remove_short_reviews():
    for k, v in datas.items():
        x = []
        for sen in v:
            q = re.sub(r'\W+', ' ', sen)
            token = set(nltk.word_tokenize(q))
            if len(token) > 2:
                x.append(escape(sen))
        datas[k] = x


def remove_redundant_review():
    for k, v in datas.items():
        sen_with_no_space = set()
        sen_with_space = []
        for sen in v:
            sz = len(sen_with_no_space)
            s = re.sub(r'\w+', '', sen)
            sen_with_no_space.add(s)
            sz2 = len(sen_with_no_space)
            if sz2 > sz:
                sen_with_space.append(sen)
        datas[k] = sen_with_space


def kalimat_xml(myid, s):
    x = f"""
    <sentence id="{myid}">
          <text>{s}</text>
          <Opinions>
            <Opinion category="" polarity="" />
         </Opinions>
    </sentence>"""
    return x


def review_xml(kalimat):
    x = f"""
    <Review>{kalimat}
    </Review>"""
    return x


def all_reviews_xml(r):
    x = f"""<?xml version="1.0" encoding="UTF-8"?>
    <Reviews>{r}
    </Reviews>
    """
    return x


def parse_into_xml():
    for k, v in datas.items():
        tahun = 'T' + re.sub('\D', '', k) + '-'
        r = """"""
        for review in v:
            R = tahun + 'R' + str(v.index(review)) + '-'
            s = nltk.sent_tokenize(review)
            kal = """"""
            for kalimat in s:
                myid = R + 'S' + str(s.index(kalimat))
                kal += kalimat_xml(myid, kalimat)
            r += review_xml(kal)
        x = all_reviews_xml(r)
        ##x = ET.fromstring(x)
        x = xml.dom.minidom.parseString(x)
        x = x.toprettyxml()
        datas[k] = x


def save_data():
    folder_name = './data/' + strftime("%d-%b-%Y-%H:%M:%S", localtime())+ "/"
    for k, v in datas.items():
        filename = re.sub('\D', '', k)
        filename = folder_name + filename + '.xml'
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(filename, "w") as f:
            f.write(v)
        #f = open(k, "w+")
        #f.write(v)
