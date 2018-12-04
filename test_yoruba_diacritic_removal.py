from collections import defaultdict
import unicodedata
import re

ca_fr = "Montréal, über, 12.89, Mère, Françoise, noël, 889"
yo_0= "ọjọ́ìbí 18 Oṣù Keje 1918 jẹ́ Ààrẹ Gúúsù Áfríkà"
yo_1 = "Kí ó tó di ààrẹ"


def strip_accents(string):
    return ''.join(c for c in unicodedata.normalize('NFD', string)
                   if unicodedata.category(c) != 'Mn')

def convert_to_NFC(filename, outfilename):
    text=''.join(c for c in unicodedata.normalize('NFC', open(filename).read()))
    with open(outfilename, 'w') as f:
        f.write(text)

def strip_accents_from_file(filename, outfilename):
    text=''.join(c for c in unicodedata.normalize('NFC', open(filename).read()))
    with open(outfilename, 'w') as f:
        f.write(strip_accents(text))

def getFileStats(filename):
    print("\nFilename: " + filename)
    lines = tuple(open(filename, 'r'))
    num_utts = len(lines)

    text = ''.join(c for c in unicodedata.normalize('NFC', open(filename).read()))
    words = re.findall('\w+', text)
    num_words = len(words)
    num_chars = len(re.findall(r'\S', text))

    unique_chars = set(text)
    num_uniq_chars = len(unique_chars)

    print(sorted(unique_chars))
    print("# utts      : " + str(num_utts))
    print("# chars     : " + str(num_chars))
    print("# uniq chars: " + str(num_uniq_chars))

    # unaccented word stats
    unaccented_words = 0
    for word in words:
        if word == strip_accents(word):
            unaccented_words += 1

    print("# total words: " + str(num_words))
    print("# unaccented words : " + str(unaccented_words))

    # ambiguous word stats
    ambiguity_map = defaultdict(set)
    for word in words:
        no_accents = strip_accents(word)
        ambiguity_map[no_accents].add(word)

    ambiguous_words = 0
    ambiguous_words_2 = 0
    ambiguous_words_3 = 0
    ambiguous_words_4 = 0
    ambiguous_words_5 = 0
    ambiguous_words_6 = 0
    ambiguous_words_7 = 0
    ambiguous_words_8 = 0
    ambiguous_words_9 = 0

    # fill ambiguity map
    for word in ambiguity_map:
        if len(ambiguity_map[word]) > 1:
            ambiguous_words += 1
        if len(ambiguity_map[word]) == 2:
            ambiguous_words_2 += 1
        elif len(ambiguity_map[word]) == 3:
            ambiguous_words_3 += 1
        elif len(ambiguity_map[word]) == 4:
            ambiguous_words_4 += 1
        elif len(ambiguity_map[word]) == 5:
            ambiguous_words_5 += 1
        elif len(ambiguity_map[word]) == 6:
            ambiguous_words_6 += 1
        elif len(ambiguity_map[word]) == 7:
            ambiguous_words_7 += 1
        elif len(ambiguity_map[word]) == 8:
            ambiguous_words_8 += 1
        elif len(ambiguity_map[word]) == 9:
            ambiguous_words_9 += 1

    # print ambiguity map
    for word in ambiguity_map:
        # if len(ambiguity_map[word]) == 2:
        # el
        if len(ambiguity_map[word]) == 3:
            print("# 3: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 4:
            print("# 4: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 5:
            print("# 5: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 6:
            print("# 6: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 7:
            print("# 7: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 8:
            print("# 8: " + str(ambiguity_map[word]))
        elif len(ambiguity_map[word]) == 9:
            print("# 9: " + str(ambiguity_map[word]))


    print("# unique ambiguous words : " + str(ambiguous_words))
    print("# total unique non-diacritized words : " + str(len(ambiguity_map)))

    unique_all_words = set()
    for word in words:
        unique_all_words.add(word)

    print("# total unique words : " + str(len(unique_all_words)))
    print("# ambiguous 2 words : " + str(ambiguous_words_2))
    print("# ambiguous 3 words : " + str(ambiguous_words_3))
    print("# ambiguous 4 words : " + str(ambiguous_words_4))
    print("# ambiguous 5 words : " + str(ambiguous_words_5))
    print("# ambiguous 6 words : " + str(ambiguous_words_6))
    print("# ambiguous 7 words : " + str(ambiguous_words_7))
    print("# ambiguous 8 words : " + str(ambiguous_words_8))
    print("# ambiguous 9 words : " + str(ambiguous_words_9))


# For yoruba blog (and probably bibeli)
def split_out_corpus_on_symbol(filename, outfilename, symbol=','):
    lines = tuple(open(filename, 'r'))

    min_words_to_split = 10
    min_words_in_utt = 5

    with open(outfilename, 'w') as f:
        # split out heavily comma'd text :((
        for line in lines:
            if symbol in line:
                num_words = len(line.split())
                num_commas = line.count(symbol)
                curr_comma_position = line.index(symbol)
                num_words_ahead_of_curr_comma = len(line[0:curr_comma_position].split())

                curr_line = line
                while num_commas > 0:
                    if num_words < min_words_to_split:
                        # print(curr_line.strip())
                        f.write(curr_line)
                        break
                    if num_words >= min_words_to_split:
                        if num_words_ahead_of_curr_comma >= min_words_in_utt and \
                                        len((curr_line)[curr_comma_position:].split()) >= min_words_in_utt:
                            f.write((curr_line)[0:curr_comma_position] + "\n")

                            # update vars
                            curr_line = curr_line[curr_comma_position +1:]
                            num_words = len(curr_line.split())
                            num_commas = num_commas - 1
                            if num_commas > 0:
                                curr_comma_position = curr_line.index(symbol)
                                num_words_ahead_of_curr_comma = len(curr_line[0:curr_comma_position].split())
                            else:
                                f.write(curr_line)
                        else:
                            # ignore too short comma (+= vs = on current comma position)
                            num_commas = num_commas - 1
                            if num_commas > 0: # for say 3 commas
                                curr_comma_position += curr_line[curr_comma_position +1:].index(symbol) + 1
                                num_words_ahead_of_curr_comma = len(curr_line[0:curr_comma_position].split())
                            else:
                                f.write(curr_line)
                    else:
                        f.write(curr_line)
            else:
                f.write(line)

if __name__ == "__main__":

    # test
    print(ca_fr, ": " ,strip_accents(ca_fr))
    print(yo_0, ": " , strip_accents(yo_0))
    print(yo_1, ": " ,strip_accents(yo_1))

    # getFileStats('data/LagosNWUspeech_corpus/all_transcripts.txt')
    # getFileStats('data/theyorubablog_corpus/theyorubablog_dot_com.txt')
    # getFileStats('data/BibeliYoruba_corpus/bibeli_ede_yoruba.txt')
    # getFileStats('data/BibeliYoruba_corpus/bibeli_ede_yoruba.txt')

    getFileStats('seq2seq/nmt_data/yoruba_diacritics/train/tgt-train.txt')
    getFileStats('seq2seq/nmt_data/yoruba_diacritics/test/tgt-test.txt')

    getFileStats('seq2seq/nmt_data/yoruba_diacritics/train/src-train.txt')
    getFileStats('seq2seq/nmt_data/yoruba_diacritics/test/src-test.txt')

    #
    # split_out_corpus_on_symbol('data/theyorubablog_corpus/theyorubablog_dot_com.txt')

    # strip accents
    # strip_accents_from_file('yorubaspeechcorpus/all_transcripts.txt', 'yorubaspeechcorpus/all_transcripts_no_diacritics.txt')
    # strip_accents_from_file('corpus/theyorubablog_dot_com.txt', 'corpus/theyorubablog_dot_com_no_diacritics.txt')
    strip_accents_from_file('/Users/iorife/github/yoruba-text/first_words.txt', '/Users/iorife/github/yoruba-text/first_words_ascii.txt')

    # convert from NFD to NFC
    # convert_to_NFC('data/LagosNWUspeech_corpus/all_transcripts.txt', 'data/LagosNWUspeech_corpus/all_transcripts_NFC.txt')
    # convert_to_NFC('data/theyorubablog_corpus/theyorubablog_dot_com.txt', 'data/theyorubablog_corpus/theyorubablog_dot_com_NFC.txt')
    # convert_to_NFC('data/BibeliYoruba_corpus/bibeli_ede_yoruba.txt', 'data/BibeliYoruba_corpus/bibeli_ede_yoruba_NFC.txt')
    # convert_to_NFC('data/theyorubablog_corpus/theyorubablog_dot_com_JARA.txt', 'data/theyorubablog_corpus/theyorubablog_dot_com_JARA_NFC.txt')