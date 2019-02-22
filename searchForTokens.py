import tokenizer
import settings
import zipfile

def search_main(query):
    zfile_name = ''
    result_code = []
    f_name = str(query[0])+''
    with zipfile.ZipFile(zfile_name) as z:
        for f_name in z.namelist():
            searchfile = open(f_name,'r')
            for line in searchfile:
                if(query in line):
                    temp = line.split(':')
                    result_code.append(temp[2])
    searchfile.close()
    result_urls = []
    for code in result_code:
        result_urls.append(settings.code2url[code])
    

    
