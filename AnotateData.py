import xml.etree.ElementTree as ET

class AnotateData:
    def __init__(self, filename):
        self.filename = filename

    def Import_Xml(self):
        self.tree = ET.parse(self.filename)
        self.root = self.tree.getroot()

    def Write_to_file(self, outputfile):
        self.tree.write(outputfile)

    def udah_ada_isi(self, mid):
        for sen in self.root.iter('sentence'):
            sid = sen.attrib
            if sid == mid:
                for opini in sen.iter('Opinion'):
                    if opini.attrib['category'] != "":
                        return True
                    else:
                        return False

    def find_category(self, num):
        cat = {}
        cat[1] = "Dosen#Mengajar"
        cat[2] = "Dosen#Umum"
        cat[3] = "Perkuliahan"
        cat[4] = "Nilai"
        cat[5] = "Layanan"
        cat[6] = "Sarpras"
        cat[7] = "NoAspect"
        cat[8] = "Bingung"
        return cat[num]

    def find_polarity(self, num):
        pol = {}
        pol[1] = "Positif"
        pol[2] = "Negatif"
        pol[3] = "Netral"
        return pol[num]


if __name__ == "__main__":
    filename = './data/anotate/2019.xml'
    op = {}
    op['category'] = ""
    op['polarity'] = ""
    d1 = AnotateData(filename)
    d1.Import_Xml()
    lanjut = "y"
    for sen in d1.root.iter('sentence'):
        txt = sen.find('text').text
        sid = sen.attrib
        if d1.udah_ada_isi(sid) is False and lanjut == "y":
            print(txt)
            val = input("berapa opini: ")
            c = ET.Element("Opinion", op)
            ops = sen.find('Opinions')
            for o in range(1, int(val)):
                ops.insert(o, c)
            for opini in sen.iter('Opinion'):
                c = int(input("category: "))
                p = int(input("polarity: "))
                opini.attrib['category'] = d1.find_category(c)
                opini.attrib['polarity'] = d1.find_polarity(p)
            d1.tree.write('./data/anotate/2019.xml')
            ll = input("masih mau lanjut(y/n): ")
            lanjut = ll
