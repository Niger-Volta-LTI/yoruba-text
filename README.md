# Yorùbá text

This repository contains fully diacritized Yorùbá text, converted to Unicode Normalization Form Composition ([NFC](http://www.macchiato.com/unicode/nfc-faq)) format, where diacritized characters are _composed_ into a single character with the following code:

```
def convert_to_NFC(filename, outfilename):
    text=''.join(c for c in unicodedata.normalize('NFC', open(filename).read()))
    with open(outfilename, 'w') as f:
        f.write(text)
```

Corpora include LagosNWU conversational corpus, bible.com and theyorubablog.com

Text has been gathered with permission from online sources, and lightly preprocessed for use in NLP, TTS, ASR applications. Note, some of the sentences may have errors, please submit a pull-request if you have corrections! 


