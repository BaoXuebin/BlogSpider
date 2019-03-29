# -*- coding:utf-8 -*-
from parse.Base import getSoup

title = "代码星冰乐"
origin = "http://www.hchstudio.cn"
url = "http://www.hchstudio.cn/"

# 解析 Hchstudio 的脚本
def parseHchstudio(content=""):
    page = dict()
    soup = getSoup(content)
    if soup:
        # 网页地址
        page['origin'] = origin
        # 页面标题
        page['title'] = title
        # 初始化博客列表集合
        blogs = list()

        # 最近的日志
        articles = soup.find_all('div', 'post')
        for article in articles:
            blog = dict()
            blog['id'] = article.h1.a.string.strip()
            blog['title'] = article.h1.a.string.strip()
            blog['href'] = origin + article.h1.a['href']
            blog['publishTime'] = article.find('span', 'post-meta').string.strip()
            blog['author'] = article.find('a', id='authorH').string.strip()
            blogs.append(blog)

        page['blogs'] = blogs
        page['blogCount'] = len(blogs)
    return page

exports = {
    "url": url,
    "title": title,
    "parser": parseHchstudio
}