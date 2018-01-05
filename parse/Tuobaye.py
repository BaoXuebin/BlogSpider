# -*- coding:utf-8 -*-
# http://tuobaye.com/#blog
# 解析 拓跋的前端客栈 的脚本
from bs4 import BeautifulSoup

def parseTuobaye(content=""):
    page = dict()
    if not content:
        return page
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = soup.title.string.replace('|', '').replace('\n', '').strip()

    blogs = list()
    blogContainers = soup.find_all('ol', 'post-list')
    for blogContainer in blogContainers:
        if blogContainer:
            items = blogContainer.find_all('li')
            for item in items:
                blog = dict()
                blog['publishTime'] = item.time.string
                blog['id'] = item.h2.a['href']
                blog['href'] = 'http://tuobaye.com/' + item.h2.a['href']
                blog['title'] = item.h2.a.string
                blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
