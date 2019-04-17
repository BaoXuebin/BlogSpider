# -*- coding:utf-8 -*-
from parse.Base import getSoup

title = "CodeSheep程序羊"
origin = "https://www.codesheep.cn"
url = "https://www.codesheep.cn/archives/"

# 解析 codesheep.cn 的脚本
def parseTemplate(content=""):
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
        articles = soup.find_all('div', 'content')
        for article in articles:
            blog = dict()
            blog['id'] = article.h1.a['href']
            blog['href'] = origin + article.h1.a['href']
            blog['title'] = article.h1.a.string.strip()
            blog['publishTime'] = article.time.string.strip()
            blogs.append(blog)

        page['blogs'] = blogs
        page['blogCount'] = len(blogs)
    return page

exports = {
    "url": url,
    "title": title,
    "parser": parseTemplate
}