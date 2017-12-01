# -*- coding:utf-8 -*-
# https://blog.thankbabe.com/archive/
# 解析 SFLYQ 追逐全栈技术 的脚本
from bs4 import BeautifulSoup

base = 'https://blog.thankbabe.com/'

def parseThankbabe(content=""):
    page = dict()
    if not content:
        return page
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = 'SFLYQ_' + soup.title.string.replace('|', '')

    blogs = list()
    blogContainers = soup.find_all('div', 'left')
    for blogContainer in blogContainers:
        items = blogContainer.ul.find_all('li')
        for item in items:
            blog = dict()
            blog['id'] = item.a['href']
            blog['href'] = base + blog['id']
            blog['title'] = item.a.string
            blog['publishTime'] = item.time.string.replace('\n', '').strip()
            blog['author'] = 'YYQ'
            blogs.append(blog)
    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
