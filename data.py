def read_texts(zipfname):
    import zipfile
    import os
    with zipfile.ZipFile(zipfname) as z:
        for foldername in z.namelist():
            if not os.path.isdir(foldername):
                print('Reading File '+ foldername)

        

if __name__ == "__main__":
    read_texts("data/webpages.zip")
    

