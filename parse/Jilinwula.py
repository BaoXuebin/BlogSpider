# -*- coding:utf-8 -*-
from Base import getSoup

title = "吉林乌拉"
origin = "http://jilinwula.com/"
url = "http://jilinwula.com/archives"

# 解析 ZiWenXie 的脚本
def parseJilinwula(content=""):
    page = dict()
    soup = getSoup(content)
    if soup:
        page['origin'] = origin
        # 页面标题
        page['title'] = title
        # 初始化博客列表集合
        blogs = list()
        items = soup.find_all('div', 'item-label')
        for item in items:
            href = item.div.a['href']
            _title = item.div.a.string
            if _title:
                blog = dict()
                blog['id'] = href
                blog['href'] = href
                blog['title'] = _title
                blog['publishTime'] = item.find_all('div', 'item-meta-date')[0].string.replace('发布于 ', '')
                blogs.append(blog)
            
        page['blogs'] = blogs
        page['blogCount'] = len(blogs)
    return page

exports = {
    "url": url,
    "title": title,
    "parser": parseJilinwula
};