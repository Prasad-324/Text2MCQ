import nltk
from nltk.corpus import wordnet as wn

## Get Distractor

def get_distractors_wordnet(syn,word):
    distractors = []
    word = word.lower()
    orig_word = word
    if len(word.split()) > 0:
        word = word.replace(" ","_")
    hypernym = syn.hypernyms()
    if len(hypernym) == 0:
        return distractors
    for item in hypernym[0].hyponyms():
        name = item.lemmas()[0].name()
        if name == orig_word:
            continue    
        name = name.replace("_"," ")
        name = " ".join(w.capitalize() for w in name.split())
        if name is not None and name not in distractors:
            distractors.append(name)
    
    return distractors

def get_distractors_list(keyword_sentence_mapping):
    key_distractor_list = {}
    keyword_sentence_list={}
    
    for keyword in keyword_sentence_mapping:
        if len(keyword.split()) > 0:
            keyword = keyword.replace(" ","_")
        synset_use = wn.synsets(keyword,'n')
        if synset_use != []:
            distractors = get_distractors_wordnet(synset_use[0],keyword)
            if len(distractors) != 0:
                key_distractor_list[keyword] = distractors
            
    return key_distractor_list