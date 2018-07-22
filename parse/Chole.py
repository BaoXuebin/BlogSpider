# -*- coding:utf-8 -*-
# http://www.chole.io/blog/archive.html
# 解析 猫叔の杂记 · 手帐 的脚本
from bs4 import BeautifulSoup

origin = 'http://www.chole.io/blog/'

def parseChole(content=""):
    page = dict()
    if not content:
        return page
    page['origin'] = origin
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = soup.title.string.replace('|', '')

    blogs = list()
    blogContainer = soup.article
    if blogContainer:
        items = blogContainer.find_all('li', 'article-item')
        for item in items:
            blog = dict()
            blog['publishTime'] = item.span.string
            blog['id'] = item.a['href']
            blog['href'] = 'http://www.chole.io/blog/' + item.a['href']
            blog['title'] = item.a.string
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
