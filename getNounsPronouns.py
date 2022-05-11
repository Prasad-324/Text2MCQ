import string
import traceback
import pke
import nltk
from nltk.corpus import stopwords

def get_noun_pronoun(text):
    out=[]
    try:
        extractor = pke.unsupervised.MultipartiteRank()
        pos = {'NOUN'}
        stoplist = list(string.punctuation)
        stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
        stoplist += stopwords.words('english')
        extractor.load_document(input=text,stoplist=stoplist)
        extractor.candidate_selection(pos=pos)
       
        extractor.candidate_weighting(alpha=1.1,
                                      threshold=0.75,
                                      method='average')
        keyphrases = extractor.get_n_best(n=30)
        

        for val in keyphrases:
            out.append(val[0])
    except:
        out = []
        traceback.print_exc()

    return out


