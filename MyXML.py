import xml.etree.ElementTree as ET
import nltk

"""
this class load xml data, transform it into pair data structure (text, opini),
rebuild id of every sentence, and create summary of data
"""
class MyXML:
    def __init__(self, path):
        self.path = path
        self.tree = ET.parse(path)
        self.root = self.tree.getroot()
        self.data = []
        self.mp = {}
        self.pair = []
        for text in self.root.iter('text'):
            self.data.append(text.text)

    def get_child(self):
        l = []
        for child in self.root.iter('Opinions'):
            v = []
            for c in child:
                v.append(c.attrib)
            l.append(v)
        return l


    def get_attribut_by_tag(self, tag, attr=None):
        s = []
        if attr is None:
            for mtag in self.root.iter(tag):
                s.append(mtag.attrib)
        else:
            for mtag in self.root.iter(tag):
                s.append(mtag.attrib[attr])
        return s

    def group_data_by_polarity(self):
        polarity = self.get_attribut_by_tag('Opinion', attr='polarity')
        mp = {}
        for p in polarity:
            if p in mp:
                mp[p] += 1
            else:
                mp[p] = 1
        return mp

    def summary_detail(self):
        data = self.get_attribut_by_tag('Opinion')
        mp = {}
        for p in data:
            aspek = p['category']
            polarity = p['polarity']
            if aspek not in mp:
                mp[aspek] = {}

            if polarity in mp[aspek]:
                mp[aspek][polarity] += 1
            else:
                mp[aspek][polarity] = 1
        return mp

    def summary_data(self):
        """ print summary data """
        print("jumlah kalimat :" + str(len(self.data)))
        polarity = self.get_attribut_by_tag('Opinion', attr='polarity')
        aspek = self.get_attribut_by_tag('Opinion', attr='category')
        print("label polaritas : " + str(set(polarity)))
        print("label Aspek : " + str(set(aspek)))
        print(self.group_data_by_polarity())
        print(self.summary_detail())

    def rebuild_id(self):
        """give / rebuild sentences with unique id and format
        tahun-review-sentence"""
        tahun = self.root.attrib['id']
        for i in range(0, len(self.root)):
            for j in range(0, len(self.root[i])):
                self.root[i][j].set('id', tahun + str(i) + str(j))

        self.tree.write(self.path)

    def set_mp(self):
        for sentence in self.root.iter('sentence'):
            data = {}
            data['text'] = sentence.find('text').text
            x = []
            for opini in sentence.find('Opinions'):
                category = opini.attrib['category']
                polarity = opini.attrib['polarity']
                x.append([category, polarity])
            data['opinions'] = x
            mid = sentence.get('id')
            self.mp[mid] = data

    def get_mp(self):
        if not bool(self.mp):
            self.set_mp()
        return self.mp

    def add_space(self, text):
        """
        adding space after period if it have not
        it will take a long time, i guess
        """
        for i in range(0, len(text)):
            if text[i] == '.' or text[i] == ',':
                if i < len(text) - 1 and text[i + 1] != ' ':
                    text = text[:i+1] + " " + text[i + 1:]
        return text

    def set_pair(self):
        for sentence in self.root.iter('sentence'):
            x = []
            text = sentence.find('text').text
            text = self.add_space(text)
            x.append(text)
            y = []
            for opini in sentence.find('Opinions'):
                category = opini.attrib['category']
                polarity = opini.attrib['polarity']
                y.append([category, polarity])
            x.append(y)
            self.pair.append(x)

    def get_pair(self):
        if not bool(self.pair):
            self.set_pair()
        return self.pair

    def save_data(self, filename):
        self.tree.write(filename)
