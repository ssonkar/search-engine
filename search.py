import settings
import searchForTokens
import rankPages
import heapq
from flask import Flask, jsonify, render_template
app = Flask(__name__)

def print_results(ranked_doc):
    urls =[]
    while ranked_doc:
        (score, doc_id) = heapq.heappop(ranked_doc)
        #print('score: '+str(score)+' url: '+ settings.code2url[doc_id])
        urls.append(settings.code2url[doc_id])
    return urls


@app.route('/search/<query>')
def search(query):
    _, doc_ids, query = searchForTokens.process_query(query)
    ranked_doc = rankPages.rank_docs(doc_ids, query)
    urls = print_results(ranked_doc)
    return jsonify(urls)


if __name__ == "__main__":
    settings.load_data()
    app.run(debug=True)