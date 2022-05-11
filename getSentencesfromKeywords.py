from flashtext import KeywordProcessor

def get_sentences_from_keyword(keywords,sentences):
    keyword_processor = KeywordProcessor()
    keyword_sentences = {}
    for word in keywords:
        keyword_sentences[word]=[]
        keyword_processor.add_keyword(word)
    for sentence in sentences:
        keywords_found = keyword_processor.extract_keywords(sentence)
        for key in keywords_found:
            keyword_sentences[key].append(sentence)
    
    for key in keyword_sentences.keys():
        values=keyword_sentences[key]
        values=sorted(values,key=len,reverse=True)
        keyword_sentences[key]=values
    return keyword_sentences

