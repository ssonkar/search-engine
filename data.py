def read_texts(zipfname):
    import zipfile
    import os
    import tokenizer
    with zipfile.ZipFile(zipfname) as z:
        for filename in z.namelist():
            if not filename[-1]=='/' :
                print('Reading File '+ filename)
                freq = tokenizer.parserMain(z.read(filename))
                print(freq)

        

if __name__ == "__main__":
    read_texts("data/webpages.zip")