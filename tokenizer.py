from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import collections


def generateTokens(input_string):
    Token = []
    temp = ''
    for c in input_string:
        if(c.isdigit() or c.isalpha()):
            temp += c.lower()
        elif(temp != ''):
            Token.append(temp)
            temp = ''
    if(temp != ''):
        Token.append(temp)
    return Token


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def formTokenLists(raw_list):
    raw_list_temp = []
    for i in raw_list:
        raw_list_temp.append(i.get_text())
    out = []
    for k in raw_list_temp:
        out.extend(generateTokens(k))
    out = list(set(out))
    return out

def heuristics():
    pass


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)

    title = formTokenLists(soup.find_all('title'))
    headers_1_3 = formTokenLists(soup.find_all(['h1', 'h2', 'h3']))
    headers_4_6 = formTokenLists(soup.find_all(['h4', 'h5', 'h6']))
    body = formTokenLists(soup.find_all('body'))
    return u" ".join(t.strip() for t in visible_texts)


def parserMain(path):
    # html = urllib.request.urlopen(path).read()
    f = open(path)
    page_string = text_from_html(f)

    Token = generateTokens(page_string)

    token_frequency = collections.Counter(Token)

    if('' in token_frequency):
        del token_frequency['']