def addTokens(token_freq,file_no):
    for token in token_freq:
        file_name = 'token[0]'
        f = open(file_name,a)
        f.write(token+":"+token_freq[token]+':'fine_no+'\n')
        f.close




