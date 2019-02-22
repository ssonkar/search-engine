import searchForTokens


query = ''
search_results = searchForTokens.process_query(query)
for i, x in enumerate(search_results):
    print(i+1+' '+x+'\n')
