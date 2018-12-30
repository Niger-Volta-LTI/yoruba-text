import test_yoruba_diacritic_removal as text_utils
import re

# create file with cat chapters/* > bibeli_ede_yoruba.txt
# manually remapped '.)'-> ')' and '..'->'.'
fp = open("bibeli_ede_yoruba.raw.txt")
data = fp.read()
data = re.sub("[\(].*?[\)]", "", data)  # remove stuff in parens

# 1) split on periods, remove single/double quotes, line break on ;?
with open("bibeli_ede_yoruba.raw1.txt", 'w', encoding='utf-8') as f:
    for utt in data.split('.'):
        utt = utt.replace(';', '\n').replace('?', '\n') # break on ;?
        utt = utt.replace('“', '').replace('”', '').replace('‘', '').replace('’', '')  # remove quotes
        f.write(utt.strip(" ") + "\n")

# 2) smart split lines at ":"
text_utils.split_out_corpus_on_symbol('bibeli_ede_yoruba.raw1.txt',
                                      'bibeli_ede_yoruba.raw2.txt',
                                      ':')

# 3) finally remove last-remaining :, ,
lines = tuple(open("bibeli_ede_yoruba.raw2.txt", 'r'))
with open("bibeli_ede_yoruba.txt", 'w', encoding='utf-8') as f:
    for line in lines:
        utt = line.replace(':', '').replace('.', '')
        f.write(utt.strip(" "))
