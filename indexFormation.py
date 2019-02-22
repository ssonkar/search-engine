import json
import settings

def merge_maps(inverted_idx, doc_freq, doc_id):
    for token in doc_freq:
        if not inverted_idx.get(token):
            inverted_idx[token] = []
        inverted_idx[token].append((doc_id, doc_freq[token]))
    return inverted_idx

# Dicey implementation
def merge_files(inverted_idx_on_file, docs_freq):
    for token in docs_freq:
        if not inverted_idx_on_file.get(token):
            inverted_idx_on_file[token] = list()
        inverted_idx_on_file[token].append(docs_freq[token])
    return inverted_idx_on_file


def addTokens(token_freq, doc_id, file_mod):
    for c in token_freq.keys():
        merge_maps(settings.buffer_dict[c], token_freq[c], doc_id)
    
    if file_mod == settings.batch_size-1:
        for c in settings.buffer_dict.keys():
            file_name = "dump/" + c + ".json" 
            with open(file_name, 'r+') as file_new:
                inverted_idx_on_file = json.loads(file_new.read())
                file_new.close()
            inverted_idx_on_file = merge_files(inverted_idx_on_file, settings.buffer_dict[c])
            with open(file_name, 'w') as file_new:
                json.dump(inverted_idx_on_file, file_new)
                file_new.close()
        token_freq[c] = {}
        settings.reset_buffer()

## Unimplemented
def read_chunks(zipfname):
    import zipfile
    import os
    import tokenizer
    import json
    files = 0
    with zipfile.ZipFile(zipfname) as z:
        for filename in z.namelist():
            if not filename[-1] == '/' and '.tsv' not in filename and '.json' not in filename:
                print('Reading File ' + filename)
                tokenizer.parserMain(z.read(filename), filename[filename.index("/")+1:], (files % settings.batch_size))
                files +=1 
            elif '.json' in filename:
                json_data = z.read(filename)
                settings.code2url = json.loads(json_data.decode("utf-8"))


if __name__ == "__main__":
    settings.init()
    read_chunks("dump/chunks/webpages.zip")