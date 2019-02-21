def create_dump():
    from string import ascii_lowercase
    for c in ascii_lowercase:
        f = open("dump/"+c+".json", "w+")
        f.close()


def init():
    global code2url
    code2url = dict()
    create_dump()    