import TokenizeSentences
import getNounsPronouns
import getSentencesfromKeywords
import getDistractors
import random
import re

def main(text):
    
    sentences = TokenizeSentences.tokenize_sentences(text)    
    
    noun_pro = getNounsPronouns.get_noun_pronoun(text)
    
    keyword_sentence_mapping = getSentencesfromKeywords.get_sentences_from_keyword(noun_pro,sentences)
    
    keywords_distractors_list = getDistractors.get_distractors_list(keyword_sentence_mapping)
    
    keyword_sentence_list={}
    
    for word in keyword_sentence_mapping:
        if word in keywords_distractors_list:
            keyword_sentence_list[word] = keyword_sentence_mapping[word]
            
        """index=1
        for key in keywords_distractors_list:
            sentence = keyword_sentence_mapping[key][0]
            pattern = re.compile(key, re.IGNORECASE)
            output = pattern.sub( " _______ ", sentence)
            print ("%s)"%(index),output)
            choices = [key.capitalize()] + keywords_distractors_list[key]
            top4choices = choices[:4]
            random.shuffle(top4choices)
            optionchoices = ['a','b','c','d']
            for idx,choice in enumerate(top4choices):
                print ("\t",optionchoices[idx],")"," ",choice)
            index = index + 1
        """

    return sentences,noun_pro,keyword_sentence_mapping,keywords_distractors_list,keyword_sentence_list