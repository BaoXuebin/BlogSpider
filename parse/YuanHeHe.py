# -*- coding:utf-8 -*-
# http://yuanhehe.cn/archives/
# 解析 yuanhehe' blog 的脚本
from bs4 import BeautifulSoup

base = 'http://yuanhehe.cn'

def parseYuanHeHe(content=""):
    page = dict()
    if not content:
        return page
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = soup.title.string.replace('|', '')

    blogs = list()
    blogContainer = soup.main
    if blogContainer:
        items = blogContainer.find_all('article')
        for item in items:
            blog = dict()
            blog['publishTime'] = item.div.time['content']
            blog['id'] = item.h2.a['href']
            blog['href'] = base + item.h2.a['href']
            blog['title'] = item.h2.span.string
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
