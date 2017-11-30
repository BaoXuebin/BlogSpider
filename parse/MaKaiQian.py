# 解析 http://makaiqian.com/ 的脚本
from bs4 import BeautifulSoup

base = 'http://makaiqian.com/'

def parseMaKaiQian(content=""):
    page = dict()
    if not content:
        return page
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    # 去除非法字符 |
    page['title'] = soup.title.string.replace('|', '')

    blogs = list()
    blogContainer = soup.main
    if blogContainer:
        articles = blogContainer.find_all('article')
        for article in articles:
            blog = dict()
            link = article.header.h2.a['href'].replace('/', '')
            blog['id'] = link
            blog['href'] = base + link
            blog['title'] = article.header.h2.a.string
            blog['author'] = article.footer.a.string.strip()
            blog['publishTime'] = article.footer.time['datetime']
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
