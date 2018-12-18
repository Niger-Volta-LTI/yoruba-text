#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from math import log
import sys
import unicodedata

alphabet = [unicodedata.normalize('NFC', i) for i in ['à', 'a', 'á', 'b', 'd', 'è', 'e', 'é', 'ẹ̀', 'ẹ', 'ẹ́', 'f', 'g', 'h', 'ì', 'i', 'í', 'j', 'k', 'l', 'm', 'ǹ', 'n', 'ń', 'ò', 'o', 'ó', 'ọ̀', 'ọ', 'ọ́', 'p', 'r', 's', 'ṣ', 't', 'ù', 'u', 'ú', 'w', 'y']]
non_alphabet = [unicodedata.normalize('NFC', i) for i in ['c', 'q', 'z', 'x', 'ô', '$', '£', '€']] # wanted characters also tend to be misrecognized as this

BENCHMARK_DISTRIBUTION = {
        'ẹ̀': 0.017865667050438204,
        'k': 0.02662882297949834,
        'ọ́': 0.01736755771770233,
        'à': 0.04515754345824863,
        't': 0.03703340937052727,
        'i': 0.04551109913228849,
        'w': 0.03414015150655122,
        'ọ': 0.03570621016159287,
        'n': 0.09531802714077343,
        'm': 0.023553871725876665,
        'á': 0.03559551919876268,
        'j': 0.015647114298713294,
        'ú': 0.028431920505600713,
        'ì': 0.03988588635346063,
        'é': 0.016850150289473034,
        's': 0.026479171710671993,
        'ù': 0.012201129850604881,
        'r': 0.03996162227539708,
        'í': 0.06868119363471142,
        'è': 0.012417414166134932,
        'y': 0.018419850094607792,
        'h': 0.004911547364221704,
        'ó': 0.024114972955223142,
        'f': 0.013278546163152724,
        'a': 0.03211967731989086,
        'o': 0.023326299845058008,
        'e': 0.009532166832363687,
        'p': 0.014145868115328785,
        'ò': 0.015813878972977206,
        'l': 0.03426322237969794,
        'ẹ': 0.011146288668634248,
        'ẹ́': 0.013032768531868577,
        'u': 0.010313193527333314,
        'ọ̀': 0.011368398824313257,
        'ṣ': 0.012050750351759914,
        'd': 0.014969132151378354,
        'b': 0.03661176418974647,
        'g': 0.02225616583269636,
        'c': 1.2015798948375112e-05,
        'ń': 0.0038789171978189717,
        'z': 3.6411865045994215e-07,
        'm̀': 3.6411865045994215e-07,
        'ṣ́': 3.6411865045994215e-07,
        'ǹ': 1e-05,
        'q': 1e-05,
        'ô': 1e-05,
        '$': 1e-05,
        '£': 1e-05,
        '€': 1e-05
}

marks = ['́','̀' ]
def character_distribution(filepath):
    all_chars = defaultdict(lambda : 10**(-5))
    corpus_file = open(filepath)
    for line in corpus_file:
        line += ' ' #one space to buffer the lookahead
        line = unicodedata.normalize('NFC', line)
        for pos in range(len(line)-1):
            curr_letter = line[pos].lower()
            if curr_letter in alphabet + non_alphabet:
                if line[pos+1] in marks:
                    curr_letter += line[pos+1]
                    pos +=1
                all_chars[curr_letter] = 1 if curr_letter not in all_chars else all_chars[curr_letter] + 1
    total = sum(all_chars.values())
    for word,freq in all_chars.items():
        all_chars[word] = freq/total
    return all_chars

def distance_score(old, new):
    # Rough measure of how far away this dataset is from the distribution of well marked yoruba.
    # Inspiration from KL_score.
    result = 0
    char_missing = False
    for i in alphabet:
        if i not in new:
            print("Warning: this dataset does not have {}!".format(i))
            char_missing = True
        result += abs(log(new[i]/old[i]))
    for i in non_alphabet:
        if i in new:
            result += 5*max(log(new[i]/old[i]), 0) #penalize more for having more bad_characters
    if not char_missing:
        print("no yoruba characters missing in this dataset!")
    return result

def get_score(filepath):
    file_distribution = character_distribution(filepath)
    #print(sorted( ((v,k) for k,v in file_distribution.items()), reverse=True))
    benchmark_distribution = defaultdict(lambda : 10**(-5))
    for k,v in BENCHMARK_DISTRIBUTION.items():
        benchmark_distribution[k]=v
    print("this dataset's distance from a reasonable distribution is {}".format(distance_score(benchmark_distribution, file_distribution)))
    print("if this is a large dataset and you have a score above ~100 or there are several marked characters missing, this dataset is low quality")


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        get_score(file_name)
    except:
        print("you must specify a filepath")

