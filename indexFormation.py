def addTokens(token_freq, file_no):
    zfile_name = ''
    f_name = str(token[0])+''
    with zipfile.ZipFile(zfile_name) as z:
        for f_name in z.namelist():
            f = open(f_name, a)
            for token in token_freq:
                f.write(token+":"+token_freq[token]+':'fine_no+'\n')
            f.close()
