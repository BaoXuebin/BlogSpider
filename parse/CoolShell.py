# -*- coding:utf-8 -*-
# https://coolshell.cn/
# 解析 酷壳 - CoolShell.cn 的脚本
from bs4 import BeautifulSoup
import re

origin = 'https://coolshell.cn/'
p = re.compile(r'\d+')

def parseCoolShell(content=""):
    page = dict()
    page['origin'] = origin
    if not content:
        return page
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = soup.title.string.replace('|', '')

    blogs = list()
    articles = soup.find_all('article')
    for article in articles:
        blog = dict()
        blog['publishTime'] = article.time.string.strip()
        blog['id'] = article.a['href']
        blog['href'] = article.a['href']
        blog['title'] = article.a.string
        blog['author'] = article.find('span', 'author').string
        blog['comment'] = ''.join(p.findall(article.find('a', 'comments-link').string))
        blog['count'] = ''.join(p.findall(article.find('i', 'fa fa-users').next_sibling))
        blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
