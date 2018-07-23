# -*- coding:utf-8 -*-
from Base import getSoup

title = "阮一峰的网络日志"
origin = "http://www.ruanyifeng.com"
url = "http://www.ruanyifeng.com/blog/"

# 解析 Ruanyifeng 的脚本
def parseRuanyifeng(content=""):
    page = dict()
    soup = getSoup(content)
    if soup:
        # 网页地址
        page['origin'] = origin
        # 页面标题
        page['title'] = title
        # 初始化博客列表集合
        blogs = list()
        # 获取最新的日志
        leastHeader = soup.find_all('div', 'asset-header')[0]
        leastFooter = soup.find_all('div', 'asset-footer')[0]
        first = dict()
        first['id'] = leastHeader.h2.a['href']
        first['href'] = leastHeader.h2.a['href']
        first['title'] = leastHeader.h2.a.string
        first['publishTime'] = leastFooter.abbr.string.split('日')[0].replace(' ', '') + '日'
        blogs.append(first)

        # 最近的日志
        items = soup.find('div', id='homepage').ul.find_all('li')
        for item in items:
            if item.span:
                blog = dict()
                blog['id'] = item.a['href']
                blog['href'] = item.a['href']
                blog['title'] = item.a.string
                blog['publishTime'] = item.span.string.split('日')[0].replace(' ', '') + '日'
                blogs.append(blog)

        page['blogs'] = blogs
        page['blogCount'] = len(blogs)
    return page

exports = {
    "url": url,
    "title": title,
    "parser": parseRuanyifeng
};