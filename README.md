# Yorùbá text

This repository contains fully diacritized Yorùbá text, converted to Unicode Normalization Form Composition ([NFC](http://www.macchiato.com/unicode/nfc-faq)) format, where diacritized characters are _composed_ into a single character with the following code:

```
def convert_to_NFC(filename, outfilename):
    text=''.join(c for c in unicodedata.normalize('NFC', open(filename).read()))
    with open(outfilename, 'w') as f:
        f.write(text)
```

### Sources:

 * [Lagos-NWU conversational corpus](https://rma.nwu.ac.za/index.php/lagos-nwu-yoruba-speech.html)
 * [Bíbélì Mímọ́ ní Èdè Yorùbá Òde-Òní](https://www.bible.com/bible/911/GEN.1.BMY)
 * [The Yorùbá blog](http://www.theyorubablog.com/)
 * [Asubiaro, T., Adegbola, T. et al. (2018). A Word-Level Language Identification Strategy for Resource-Scarce Languages](https://github.com/Toluwase/Word-Level-Language-Identification-for-Resource-Scarce-)
 * [Òwe Yorùbá](http://yoruba.unl.edu/yoruba1.html)
 * [Ìwé Ti Mọ́mọ́nì](https://www.churchofjesuschrist.org/study/scriptures/bofm/title-page?lang=yor)
 * [Kùránì (Qur'an) Mímọ́](http://www.islamicbookstore.com/b7433.html)
 
 #### Sources yet to be scraped and cleaned
 * [BBC Yorùbá](https://www.bbc.com/yoruba)
 * [Yorùbá for Academic Purpose](http://yorubaforacademicpurpose.blogspot.com/2015/12/english-yoruba.html)
 * [Yobá mọ oduá](http://yobamoodua.blogspot.com/)
 * [Àwa Ẹlẹ́rìí Jèhófà](https://www.jw.org/yo/)
 * [Orí Kìíní](http://www.coerll.utexas.edu/yemi/pdfs/yy_ch1.pdf)
 * [Iwé ti Nicé](http://www.marysrosaries.com/Yoruba_prayers.html)
 * [Alákọ̀wé](https://alakoweyoruba.wordpress.com)
 * [Èdè Yorùbá Rẹwà](https://deskgram.org/edeyorubarewa?next_id=AQA-hhLOHTv02hOmeFZYMwuXESc0pSjLfeoqBnn9c8E9PqjS2Cc377K8LwCs9TJ_nQxTdctbrw6eANdrITY5DtJ4N7HhCD00geW4pnB7Z2bLLw)
 * [Ìmọ̀_Ẹ̀rọ](https://yo.wikipedia.org/wiki/%C3%8Cm%E1%BB%8D%CC%80_%E1%BA%B8%CC%80r%E1%BB%8D)
 * [ọ̀rọ̀yorùbá](https://oroyoruba.blogspot.com)
 * [Wikipedia](https://yo.wikipedia.org/wiki/Koisaanu)
 * [Poetry of Ọláńrewájú Adépọ̀jù](https://news.clas.ufl.edu/the-transition-from-yoruba-metaphysics-to-islamic-aesthetics-in-olanrewaju-adepojus-poetry/)
 
#### Social Media sources:
 * https://twitter.com/yobamoodua
 * https://twitter.com/yoruba_proverbs
 * https://www.facebook.com/oweyoruba

Text has been gathered with permission from online sources, and lightly preprocessed for use in NLP, TTS, ASR applications. Note, some of the sentences may have errors, please submit a pull-request if you have corrections! 


## Resources
 * https://clas.uiowa.edu/dwllc/allnet/yoruba-language-and-culture-resources
 * https://glosbe.com/yo/en


## Bibtex
If you want to cite this repo in your work, please use:

```
@misc{Orife_yoruba-text_2018,
author = {Orife, Iroro and Fasubaa, Timilehin and Wahab, Olamilekan},
month = {1},
title = {{yoruba-text}},
url = {https://github.com/Niger-Volta-LTI/yoruba-text},
year = {2018}
}
```
