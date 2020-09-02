import re
import string
def case_folding_and_remove_number(pair):
    for i in range(0, len(pair)):
        pair[i][0] = pair[i][0].lower()
        pair[i][0] = re.sub(r"\d+", "", pair[i][0])
        pair[i][0] = pair[i][0].translate(str.maketrans("","", string.punctuation))
    return pair
