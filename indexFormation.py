import json


def merge_maps(old_freq, doc_freq):
    #TODO add doc_freq to old_freq lexicographically
    return old_freq

def addTokens(token_freq, file_no):
    for c in token_freq.keys():
        file_name = "data/" + c + ".json" 
        old_freq = json.loads(open(file_name).read())      
        new_freq = merge_maps(old_freq, token_freq[c])
        with open(file_name, 'w') as file_new:
            json.dump(new_freq, file_new)