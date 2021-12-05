# Create a single text file from the original_text (downloaded dir) with the following command: 
#
# 1) find .  -name '*.orig' -exec cat {} \; > yorubaspeechcorpus.txt
# 2) sed 's/.*"\(.*\)".*/\1/g' < yorubaspeechcorpus.txt > all_transcripts.txt

The original Lagos-NWU text resides in the sibling directory `original_text`. This is the 
raw downloaded text with few small enhancements to correct broken accents (with 
no base character) or other irregularities found over the course of using the text
for ASR tasks.