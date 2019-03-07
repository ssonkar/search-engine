import settings
import searchForTokens
import rankPages
import heapq

def print_results(ranked_doc):
    while ranked_doc:
        (score, doc_id) = heapq.heappop(ranked_doc)
        print('score: '+str(score)+' url: '+ settings.code2url[doc_id])


if __name__ == "__main__":
    settings.load_data()
    query = 'Mondego'
    _, doc_ids, query = searchForTokens.process_query(query)
    ranked_doc = rankPages.rank_docs(doc_ids, query)
    print_results(ranked_doc)