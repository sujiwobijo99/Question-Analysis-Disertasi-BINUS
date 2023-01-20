import nltk
from nltk.tree import Tree
from nltk.stem.porter import PorterStemmer

# Question Translation Library
import translators as ts
import translators.server as tss

ps = PorterStemmer()
stem = ps.stem


text = "this is a sampel enjoying word"

print (PorterStemmer(text))


