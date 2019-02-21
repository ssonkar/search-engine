import globals


def read_texts(zipfname):
    import zipfile
    import os
    import tokenizer
    import json
    import pprint
    files = 0
    with zipfile.ZipFile(zipfname) as z:
        for filename in z.namelist():
            if not filename[-1] == '/' and '.tsv' not in filename and '.json' not in filename:
                if files <3 :
                    print('Reading File ' + filename)
                    tokenizer.parserMain(z.read(filename), filename[filename.index("/")+1:])
                    files +=1 
            elif '.json' in filename:
                json_data = z.read(filename)
                globals.code2url = json.loads(json_data.decode("utf-8"))


if __name__ == "__main__":
    globals.init()
    read_texts("data/webpages.zip")
