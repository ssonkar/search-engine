import globals  

def read_texts(zipfname):
    import zipfile
    import os
    import tokenizer
    import json
    import pprint
    with zipfile.ZipFile(zipfname) as z:
        for filename in z.namelist():
            if not filename[-1]=='/' and '.tsv' not in filename and '.json' not in filename:
                print('Reading File '+ filename)
                #freq = tokenizer.parserMain(z.read(filename))
            elif '.json' in filename:
                json_data = z.read(filename)
                globals.code2url = json.loads(json_data.decode("utf-8"))
                print(globals.code2url)
      

if __name__ == "__main__":
    globals.init
    read_texts("data/webpages.zip")