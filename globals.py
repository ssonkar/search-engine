import json
def create_dump():
    from string import ascii_lowercase
    for c in ascii_lowercase:
        file_name = "dump/"+c+".json"
        with open(file_name, 'w+') as file_new:
            json.dump({}, file_new)



def init():
    global code2url
    code2url = dict()
    create_dump()    