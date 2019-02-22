import tokenizer
import settings


def process_query(query):
    result_urls = []
    stemmed_query = tokenizer.generateTokens(query)
    file_path = "dump/"+str(stemmed_query[0][0])+'.json'
    result_json = settings.read_json(file_path)
    for stem in stemmed_query:
        if(result_json.get(stem)):
            if(result_json[stem] != []):
                for doc_id in result_json[stem]:
                    result_urls.append(settings.code2url[doc_id[0]])
    return result_urls

if __name__ == "__main__":
    res1 = process_query('Informatics')
    res2 = process_query('Mondego')
    res3 = process_query('Irvine')
