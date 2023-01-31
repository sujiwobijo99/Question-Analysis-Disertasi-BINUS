import nltk

from modules.info_extraction import getNamedEntity,getphrase
from modules.determine_answer_type import determineAnswerType
from modules.determine_answer_type import defineCategory
from modules.get_vectors import getQueryVector

# Question Translation Library
import translators as ts
import translators.server as tss

# Stopword removal lybrary import
from gensim.parsing.preprocessing import remove_stopwords

# Evaluation import
from evaluation import evaluate, evaluate_question

import csv


dt = []
gt = []
with open("./datasets.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter=';')
  for row in csvreader:
    data = row[0]
    gt_data = []
    dt.append(data)
    gt_data.append(row[1])
    gt_data.append(row[2])
    gt.append(gt_data) 
# print(dt)
# print(gt)

rslt = []
for text in dt:
    qa_pair = []
    # text = str(input('Masukkan Pertanyaan: '))
    # text = "Siapa nama President Indonesia"
    text_eng = tss.google(text, to_language='en')
    # print('English text original:',text_eng)
    text_eng = filtered_sentence = remove_stopwords(text_eng)
    # print('Stop word processed:',text_eng)
    quest = determineAnswerType(text_eng)
    ans = defineCategory(text_eng)
    # print ("---question classified: ",quest)
    # print ("---answer category: ",ans)
    # print ("1. getNamedEntity:  ",getNamedEntity(text_eng))
    # print ("2. getphrase: ",getphrase(text_eng))
    ques = (nltk.word_tokenize(text_eng))
    qvect = getQueryVector(ques)
    # print ("---question vect ",qvect)
    getNamedEntity(text_eng)
    qa_pair.append(quest)
    qa_pair.append(ans)
       
    rslt.append(qa_pair)

# print(rslt)

# evaluate(rslt,gt)

evaluate_question(rslt,gt)