import zipfile

def addTokens(token_freq, file_no):
    zfile_name = ''
    f_name = str(token[0])+''
    with zipfile.ZipFile(zfile_name) as z:
        for f_name in z.namelist():
            f = open(f_name, a)
            for token in token_freq:
                txt = token+":"+token_freq[token]+':'+file_no+'\\n'
                f.write(txt)
            f.close()
