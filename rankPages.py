import searchForTokens
import settings
import tokenizer
import math
import heapq


def calculate_cosine_sim(doc_vec, query):
    wt = 0.0
    score = 0.0
    product = 0.0
    for key in doc_vec:
        tfidf = (1 + math.log(doc_vec[key])) * math.log((settings.total_files/settings.doc_freq[key]))
        wt = wt+ tfidf**2
        if key in query:
           product = product + tfidf**2
    ## add query tfidf
    return product 

def rank_docs(doc_ids, query):
    ordered_results = []
    for doc_id in doc_ids:
        file = settings.read_zip("data/webpages.zip", doc_id)
        doc_vec = settings.read_json("file_tf/"+doc_id+".json")
        score = calculate_cosine_sim(doc_vec, query)
        heapq.heappush(ordered_results, (-score, doc_id))
    return ordered_results
        
def print_results(ranked_doc):
    while ranked_doc:
        (score, doc_id) = heapq.heappop(ranked_doc)
        print('score: '+str(score)+' url: '+ settings.code2url[doc_id])

if __name__ == "__main__":
    settings.code2url = settings.read_json("dump/bookkeeping.json")
    settings.doc_freq = settings.read_json("file_df/file_df.json")
    settings.total_files = 2500
    query = 'Artificial Intelligence'
    _, doc_ids, query = searchForTokens.process_query(query)
    ranked_doc = rank_docs(doc_ids, query)
    print_results(ranked_doc)
        