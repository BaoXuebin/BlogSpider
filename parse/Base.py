# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

def getSoup(content=""):
    if content:
        return BeautifulSoup(content, 'html.parser')
    else:
        return None