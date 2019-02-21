from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib
import collections


def generateTokens(input_string):
    temp_token = input_string.split(' ')
    parse = []
    for temp in temp_token:
        parse.append(temp.encode('ascii', 'ignore'))

    Token = []
    for word in parse:
        temp = ''
        for c in word:
            if(c.isdigit() or c.isalpha()):
                temp += c.lower()
            elif(temp != ''):
                Token.append(temp)
                temp = ''
        Token.append(temp)
    if(temp != ''):
        Token.append(temp)
        temp = ''
    return Token


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)


def parserMain(path):
    html = urllib.request.urlopen(path).read()
    page_string = text_from_html(html)

    Token = generateTokens(page_string)

    token_frequency = collections.Counter(Token)

    if('' in token_frequency):
        del token_frequency['']
    return token_frequency