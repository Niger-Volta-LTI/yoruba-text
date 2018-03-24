# Yorùbá text

This repository contains fully diacritized Yorùbá text, converted to Unicode Normalization Form Composition ([NFC](http://www.macchiato.com/unicode/nfc-faq)) format, where diacritized characters are _composed_ into a single character with the following code:

```
def convert_to_NFC(filename, outfilename):
    text=''.join(c for c in unicodedata.normalize('NFC', open(filename).read()))
    with open(outfilename, 'w') as f:
        f.write(text)
```

### Web sources:

 * [Lagos-NWU conversational corpus](https://rma.nwu.ac.za/index.php/lagos-nwu-yoruba-speech.html)
 * [Bíbélì Mímọ́ ní Èdè Yorùbá Òde-Òní](https://www.bible.com/bible/911/GEN.1.BMY)
 * [The Yorùbá blog](http://www.theyorubablog.com/)
 * [Yorùbá for Academic Purpose](http://yorubaforacademicpurpose.blogspot.com/2015/12/english-yoruba.html)
 * [Yobá mọ oduá](http://yobamoodua.blogspot.com/)
 * [Àwa Ẹlẹ́rìí Jèhófà](https://www.jw.org/yo/)
 * http://www.coerll.utexas.edu/yemi/pdfs/yy_ch1.pdf
 
#### Social Media sources:
 * https://twitter.com/yobamoodua
 * https://www.facebook.com/oweyoruba

Text has been gathered with permission from online sources, and lightly preprocessed for use in NLP, TTS, ASR applications. Note, some of the sentences may have errors, please submit a pull-request if you have corrections! 


## Resources
 * https://clas.uiowa.edu/dwllc/allnet/yoruba-language-and-culture-resources