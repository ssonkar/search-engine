import json


def merge_maps(inverted_idx, doc_freq, doc_id):
    for token in doc_freq:
        if token not in inverted_idx:
            inverted_idx[token] = list()
        inverted_idx[token].append((doc_id, doc_freq[token]))
    return inverted_idx

def addTokens(token_freq, doc_id):
    for c in token_freq.keys():
        file_name = "dump/" + c + ".json" 
        inverted_idx = json.loads(open(file_name).read())      
        inverted_idx = merge_maps(inverted_idx, token_freq[c], doc_id)
        with open(file_name, 'w') as file_new:
            json.dump(inverted_idx, file_new)