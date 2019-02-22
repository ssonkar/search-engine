import json

def create_dump():
    from string import ascii_lowercase
    for c in ascii_lowercase:
        file_name = "dump/"+c+".json"
        f= open(file_name, 'w+')
        f.close()
        with open(file_name, 'w') as file_new:
            json.dump(dict(), file_new)
            file_new.close()

def reset_buffer():
    from string import ascii_lowercase
    for c in ascii_lowercase:
        buffer_dict[c] = dict()

def init():
    global buffer_dict
    global code2url
    code2url = dict()
    buffer_dict = dict()
    reset_buffer()
    create_dump()  
    global batch_size
    batch_size = 250  