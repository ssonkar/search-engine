def read_texts(zipfname):
    import zipfile
    import os
    import tokenizer
    with zipfile.ZipFile(zipfname) as z:
        for filename in z.namelist():
            if not os.path.isdir(filename):
                print('Reading File '+ filename)
                with z.open(filename) as f:
                    freq = tokenizer.parserMain(f)

        

if __name__ == "__main__":
    read_texts("data/webpages.zip")