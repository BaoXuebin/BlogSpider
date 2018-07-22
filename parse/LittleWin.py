# -*- coding:utf-8 -*-
# https://littlewin.wang/
# 解析 littlewin.wang - 琪中有不凡 | littlewin.wang 的脚本
from bs4 import BeautifulSoup

base = 'https://littlewin.wang'
origin = 'https://littlewin.wang/'

def parseLittleWin(content=""):
    page = dict()
    if not content:
        return page
    page['origin'] = origin
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = soup.title.string.replace('|', '')

    blogs = list()
    blogContainers = soup.find_all('div', 'list')
    for blogContainer in blogContainers:
        articles = blogContainer.find_all('div', 'article-card')
        for article in articles:
            blog = dict()
            blog['id'] = article.h2.a['href']
            blog['href'] = base + blog['id']
            blog['title'] = article.h2.a.string
            # 获取日期
            day, mon, year = '', '', ''
            for span in article.find_all('span'):
                clsName = ''
                if span.get('class'):
                    clsName = ''.join(span.get('class'))
                if clsName == 'date-day':
                    day = span.string
                elif clsName == 'date-month':
                    mon = span.string
                elif clsName == 'date-year':
                    year = span.string
                elif clsName == 'author':
                    blog['author'] = span.span.string
            blog['publishTime'] = year + '年' + mon + day + '日'
            blogs.append(blog)
    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
