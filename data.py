import settings


def read_texts(zipfname):
    import zipfile
    import os
    import tokenizer
    import json
    files = 0
    with zipfile.ZipFile(zipfname) as z:
        for filename in z.namelist():
            if not filename[-1] == '/' and '.tsv' not in filename and '.json' not in filename:
                print('Reading File No:' +str(files))
                tokenizer.parserMain(z.read(filename), filename[filename.index("/")+1:], files%(settings.batch_size))
                files +=1 
            elif '.json' in filename:
                json_data = z.read(filename)
                settings.code2url = json.loads(json_data.decode("utf-8"))
                settings.write_json('dump/bookkeeping.json', settings.code2url, 'w')
    tokenizer.write_to_file()
    print(files)


if __name__ == "__main__":
    settings.init()
    read_texts("data/webpages.zip")
