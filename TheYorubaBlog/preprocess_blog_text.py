import test_yoruba_diacritic_removal as text_utils

# smart split lines at ","
text_utils.split_out_corpus_on_symbol('theyorubablog_dot_com.raw.txt',
                                      'theyorubablog_dot_com.txt',
                                      ',')