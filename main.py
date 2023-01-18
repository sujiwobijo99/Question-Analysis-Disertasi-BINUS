import nltk

from modules.info_extraction import getNamedEntity,getphrase
from modules.determine_answer_type import determineAnswerType
from modules.get_vectors import getQueryVector

# Question Translation Library
import translators as ts
import translators.server as tss

# Stopword removal lybrary import
from gensim.parsing.preprocessing import remove_stopwords

##-----Main----
isActive = True
while isActive:
    text = str(input('Masukkan Pertanyaan: '))
    # text = "Siapa nama President Indonesia"
    text_eng = tss.google(text, to_language='en')
    print('English text original:',text_eng)
    text_eng = filtered_sentence = remove_stopwords(text_eng)
    print('Stop word processed:',text_eng)
    quest = determineAnswerType(text_eng)
    # print ("---question classified: ",quest)
    # print ("1. getNamedEntity:  ",getNamedEntity(text_eng))
    # print ("2. getphrase: ",getphrase(text_eng))
    ques = (nltk.word_tokenize(text_eng))
    qvect = getQueryVector(ques)
    print ("---question vect ",qvect)
    getNamedEntity(text_eng)
    query1 = input('do you wanna exit? yes/no:   ')
    if query1 == "yes":
        isActive = False

        