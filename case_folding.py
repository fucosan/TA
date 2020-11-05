import re
import string

def case_folding_and_remove_number_perkalimat(kalimat):
    """
    case folding, remove number, format sent, and change some character
    """
    kalimat = kalimat.lower() # case folding
    kalimat = re.sub(r"\d+", "", kalimat) # removing number
    kalimat = kalimat.replace('/', ' ')
    kalimat = kalimat.replace(',', ', ')
    kalimat = kalimat.replace('-', ' ')
    kalimat = kalimat.translate(str.maketrans("","", string.punctuation)) # removing punctuation
    return kalimat

def case_folding_and_remove_number(pair):
    """
    this function actualy do more than the name
    it does  removing punctionation, and and other stuff
    """
    for i in range(0, len(pair)):
        pair[i][0] = case_folding_and_remove_number_perkalimat(pair[i][0])
    return pair
