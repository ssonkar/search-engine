import tokenizer
import settings


def process_query(query):
    result_urls = []
    stemmed_query = tokenizer.generateTokens(query)
    file_path = "dump/"+str(stemmed_query[0][0])+'.json'
    char_2_doc_file = settings.read_json(file_path)
    for stem in stemmed_query:
        if(char_2_doc_file.get(stem)):
            for doc_id in char_2_doc_file[stem][0]:
                result_urls.append(settings.code2url[doc_id[0]])
    return result_urls

if __name__ == "__main__":
    settings.code2url = settings.read_json("dump/bookkeeping.json")
    res = process_query('anglia')
    print(res)
    res1 = process_query('Informatics')
    res2 = process_query('Mondego')
    res3 = process_query('Irvine')
