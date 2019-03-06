import tokenizer
import settings
import time

def process_query(query):
    start_time = time.time()
    result_urls = []
    stemmed_query = tokenizer.generateTokens(query)
    file_path = "dump/"+str(stemmed_query[0][0])+'.json'
    char_2_doc_file = settings.read_json(file_path)
    for stem in stemmed_query:
        if(char_2_doc_file.get(stem)):
            for doc_id in char_2_doc_file[stem]:
                result_urls.append(settings.code2url[doc_id[0]])
    print("--- %s seconds ---" % (time.time() - start_time))
    print('Pages with '+query+' :')
    idx = 1
    for webpage in result_urls:
        idx+=1
    print('Returned :' +str(idx)+' pages')
    return result_urls

if __name__ == "__main__":
    settings.code2url = settings.read_json("dump/bookkeeping.json")
    res1 = process_query('Informatics')
    settings.write_as_file('analytics/Informarics.txt', res1, 'w+')
    res2 = process_query('Mondego')
    settings.write_as_file('analytics/Mondego.txt', res2, 'w+')
    res3 = process_query('Irvine')
    settings.write_as_file('analytics/Irvine.txt', res3, 'w+')
    
