# https://www.ziwenxie.site/
# 解析 ZiWenXie 的脚本
from bs4 import BeautifulSoup

origin = 'https://www.ziwenxie.site/'

def parseZiWenXie(content=""):
    page = dict()
    if not content:
        return page
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = soup.title.string

    blogs = list()
    blogContainer = soup.find(id='wrapper')
    if blogContainer:
        articles = blogContainer.find_all('article')
        for article in articles:
            blog = dict()
            blog['publishTime'] = article.time.a.string
            blog['id'] = article.h1.a['href']
            blog['href'] = 'https://www.ziwenxie.site' + article.h1.a['href']
            blog['title'] = article.h1.a.string
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    page['origin'] = origin
    return page
