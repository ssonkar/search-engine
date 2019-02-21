import zipfile


def addTokens(token_freq, file_no):
    zfile_name = ''
    with zipfile.ZipFile(zfile_name) as z:
        for f_name in z.namelist():
            for token in token_freq:
                f_name = str(token[0])+''
                f = open(f_name, a)
                txt = token+":"+token_freq[token]+':'+file_no+'\\n'
                f.write(txt)
                f.close()