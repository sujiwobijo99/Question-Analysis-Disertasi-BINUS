import nltk

from modules.info_extraction import getNamedEntity, getphrase
from modules.determine_answer_type import determineAnswerType, determineAnswerTypeFactoid, defineCategory
from modules.get_vectors import getQueryVector

# Question Translation Library
import translators as ts
import translators.server as tss

# Stopword removal lybrary import
from gensim.parsing.preprocessing import remove_stopwords

# -----Main----
isActive = True
while isActive:
    text = str(input('Masukkan Pertanyaan: '))
    # text = "Siapa nama President Indonesia"
    text_eng = tss.google(text, to_language='en')
    print('English text original:', text_eng)
    stopword_exclusion = ["how much", "how big", "how old",
                          'how many', 'how often', 'how far', 'how long the way', 'how great', 'how litle', 'how far', 'how long', 'which', 'how small', 'how short', 'how old', 'how young', 'how mature']
    process_stopword = True
    for i in stopword_exclusion:
        if i in text_eng.lower():
            process_stopword = False
    if process_stopword:
        text_eng = filtered_sentence = remove_stopwords(text_eng)

    print('Stop word processed:', text_eng)
    if process_stopword:
        quest = determineAnswerType(text_eng)
    else:
        quest = determineAnswerTypeFactoid(text_eng)

    ans = defineCategory(text_eng)
    print("---question classified: ", quest)
    print("---answer category: ", ans)
    # print("1. getNamedEntity:  ", getNamedEntity(text_eng))
    # print("2. getphrase: ", getphrase(text_eng))
    ques = (nltk.word_tokenize(text_eng))
    # qvect = getQueryVector(ques)
    # print("---question vect ", qvect)
    getNamedEntity(text)
    query1 = input('do you wanna exit? yes/no:   ')
    if query1 == "yes":
        isActive = False
