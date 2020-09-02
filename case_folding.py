import re
import string
def case_folding_and_remove_number(pair):
    for i in range(0, len(pair)):
        pair[i][0] = pair[i][0].lower() # case folding
        pair[i][0] = re.sub(r"\d+", "", pair[i][0]) # removing number
        pair[i][0] = pair[i][0].replace('/', ' ')
        pair[i][0] = pair[i][0].replace(',' ', ')
        pair[i][0] = pair[i][0].replace('-', ' ')
        pair[i][0] = pair[i][0].translate(str.maketrans("","", string.punctuation)) # removing punctuation
    return pair
