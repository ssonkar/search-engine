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
        inverted_idx_on_file[token].extend(docs_freq[token])
    return inverted_idx_on_file


def addTokens(token_freq, doc_id, file_mod):
    if doc_id != '':
        for c in token_freq.keys():
            merge_maps(settings.buffer_dict[c], token_freq[c], doc_id)
    
    if file_mod == settings.batch_size-1:
        for c in settings.buffer_dict.keys():
            file_name = "dump/" + c + ".json" 
            inverted_idx_on_file = settings.read_json(file_name)
            inverted_idx_on_file = merge_files(inverted_idx_on_file, settings.buffer_dict[c])
            settings.write_json(file_name, inverted_idx_on_file, 'w')
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


def add_doc_freq(keys):
    for key in keys:
        if not settings.doc_freq[key]:
            settings.doc_freq[key] = 0
        else:
            settings.doc_freq[key] += 1


if __name__ == "__main__":
    settings.init()
    read_chunks("dump/chunks/webpages.zip")