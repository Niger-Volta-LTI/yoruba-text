# iroro - create single text file with 
#
# 1) find .  -name '*.orig' -exec cat {} \; > yorubaspeechcorpus.txt
# 2) sed 's/.*"\(.*\)".*/\1/g' < yorubaspeechcorpus.txt > all_transcripts.txt

LAGOS-NWU YORUBA SPEECH CORPUS
==============================

This directory tree contains a Yoruba speech corpus developed by the
University of Lagos (Lagos, Nigeria) and the North-West University
(Vanderbijlpark, South Africa).

The corpus is subdivided into directories for male and female speakers
with a sub-directory for each speaker. In each speaker's sub-directory
two text files with orthographic transcriptions and a subdirectory
containing audio recordings is present. This is briefly described below:

"recordings"
   -- This subdirectory contains RIFF-WAVE 16-bit PCM recordings, one
      file per utterance, corresponding to the labelled transcription
      in the orthographic transcription files.

"utts.data"
   -- This is a UTF-8 encoded Unicode text file containing labelled
      orthographic transcriptions found in the corresponding
      "recordings" sub-directory. Transcriptions here DO NOT CONTAIN
      diacritics related to tone and are represented in Unicode NFC
      form (i.e. using no combining characters).

"utts.data.orig"
   -- This is a UTF-8 encoded Unicode text file containing labelled
      orthographic transcriptions found in the corresponding
      "recordings" sub-directory. Transcriptions here ALSO CONTAIN
      diacritics related to tone and are represented in Unicode NFD
      form (i.e. all diacritics, including UNDOTs are represented
      using separate "combining characters").


---------------------
Notes on development:
---------------------

This corpus was recorded in Lagos, Nigeria for the purpose of speech
recognition research. A source text-corpus was gathered from the web,
news magazines, literature and student reports written in Standard
Yoruba, with a subset selected for phonetic coverage. The selected
subset was recorded using a microphone connected to a laptop computer
in a normal office environment. Originally, the corpus contained
recordings for 36 speakers (18 male and 18 female), however the
quality of some sessions were compromised by "power line noise" and
were discarded as a result. Remaining utterances were also subjected
to a process of verifying the correctness of transcriptions.

The corpus has been used broadly for the purpose of fundamental
frequency analyses in the following work:

[1] D.R. van Niekerk and E. Barnard, "Tone realisation in a Yorùbá
speech recognition corpus," in Proceedings of the Workshop on Spoken
Language Technologies for Under-resourced languages (SLTU), Cape Town,
South Africa, May 2012.

[2] D.R. van Niekerk and E. Barnard, "Generating fundamental frequency
contours for speech synthesis in Yorùbá," in Proceedings of the 14th
Annual Conference of the International Speech Communication
Association (Interspeech), pp 1027-1031, Lyon, France, September 2013.

[3] D.R. van Niekerk and E. Barnard, "Predicting utterance pitch
targets in Yorùbá for tone realisation in speech synthesis," in Speech
Communication, vol. 56, pp 229-242, 2014.

[4] D.R. van Niekerk, "Tone realisation for speech synthesis of
Yorùbá," Ph.D. thesis, North-West University, Vaal Triangle Campus,
Vanderbijlpark, South Africa, May 2014.


-------------
Known issues:
-------------
 
- Due to the recording conditions employed, a significant amount of
  reverb is present in some recordings which might need to be
  addressed appropriately depending on the nature of application.
