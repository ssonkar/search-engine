import tokenizer
import globals
import zipfile
import settings.py
from nltk.stem.porter import*


def process_query(query):
    result_urls = []
    stemmer = PorterStemmer()
    stemmed_query = stemmer.stem(query)
    file_path = "data/"+str(stemmed_query[0])+'.json'
    result_json = settings.read_json(file_path)
    if(result_json.get(stemmed_query)):
        for doc_id, freq in result_json[stemmed_query]:
            result_paths.append(settings.code2url[doc_id])
    return result_urls
