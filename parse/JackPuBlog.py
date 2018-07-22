# http://www.jackpu.com/
# 解析 ZiWenXie 的脚本
from bs4 import BeautifulSoup

base = 'http://www.jackpu.com/'
origin = 'http://www.jackpu.com/'

def parseJackPuBlog(content=""):
    page = dict()
    if not content:
        return page
    page['origin'] = origin
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = soup.title.string

    blogs = list()
    blogContainer = soup.find(id='content')
    if blogContainer:
        articles = blogContainer.find_all('article')
        for article in articles:
            blog = dict()
            blog['id'] = article.header.h2.a['href']
            blog['href'] = base + article.header.h2.a['href']
            blog['title'] = article.header.h2.a.string
            blog['publishTime'] = article.header.time['datetime']
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
