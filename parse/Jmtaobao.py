# -*- coding:utf-8 -*-
from Base import getSoup

title = "阿里中间件团队博客"
origin = "http://jm.taobao.org"
url = "http://jm.taobao.org"

# 解析 Jmtaobao 的脚本
def parseJmtaobao(content=""):
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
        articles = soup.find_all('article')
        for article in articles:
            blog = dict()
            header = article.find('header')
            blog['id'] = header.h1.a['href']
            blog['href'] = origin + header.h1.a['href']
            blog['title'] = header.h1.a.string.strip()
            blog['publishTime'] = header.time.string.strip()
            blogs.append(blog)

        page['blogs'] = blogs
        page['blogCount'] = len(blogs)
    return page

exports = {
    "url": url,
    "title": title,
    "parser": parseJmtaobao
}