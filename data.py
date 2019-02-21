def read_text(zipfname):
    import zipfile
    import os
    with zipfile.ZipFile(zipfname) as z:
        for foldername in z.namelist():
            if not os.path.isdir(foldername):
                parser

