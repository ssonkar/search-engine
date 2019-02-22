import tokenizer
import settings


def process_query(query):
    result_urls = []
    stemmed_query = tokenizer.generateTokens(query)
    file_path = "data/"+str(stemmed_query[0][0])+'.json'
    result_json = settings.read_json(file_path)
    if(result_json.get(stemmed_query)):
        for doc_id, freq in result_json[stemmed_query]:
            result_urls.append(settings.code2url[doc_id])
    return result_urls

if __name__ == "__main__":
    res1 = process_query('Informatics')
    res2 = process_query('Mondego')
    res3 = process_query('Irvine')
