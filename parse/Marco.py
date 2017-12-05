# -*- coding:utf-8 -*-
# http://www.hanyuehui.site/get-articles?count=15&type=1
# 解析 Marco的个人博客 的脚本
# 直接解析接口，不需要 BeautifulSoup
import json

base = 'http://www.hanyuehui.site/article-detail/'

def parseMarco(content=""):
    page = dict()
    if not content:
        return page
    # 页面标题
    page['title'] = 'Marco的个人博客'
    blogs = list()

    result = json.loads(content)
    if result.get('status') == 1:
        articles = result.get('info').get('articles')
        for article in articles:
            blog = dict()
            blog['id'] = str(article.get('id'))
            blog['title'] = article.get('title')
            blog['href'] = base + str(article.get('id'))
            blog['count'] = str(article.get('views'))
            blog['publishTime'] = article.get('created_at')
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
