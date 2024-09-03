import pandas as pd
import nltk 

from nltk import word_tokenize
from nltk import pos_tag



def determine_tense_input(sentence):
    text = word_tokenize(sentence)
    tagged = pos_tag(text)

    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == "MD"]) 
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]]) 
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN","VHN"]]) 
    return(tense)


phrases = ["it all ends tonight", "i will get internship", "i made a yummy sandwich", "i used to have suicidal thoughts"]

test = list(map(determine_tense_input, phrases))

print(test)

