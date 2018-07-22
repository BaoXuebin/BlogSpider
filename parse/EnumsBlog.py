# http://posts.enumsblog.com/list
# 解析 ZiWenXie 的脚本
from bs4 import BeautifulSoup

base = 'http://posts.enumsblog.com/list'
origin = 'http://posts.enumsblog.com/'

def parseEnumsBlog(content=""):
    page = dict()
    if not content:
        return page
    page['origin'] = origin
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    # 去除非法字符 |
    page['title'] = soup.title.string.replace('|', '')

    blogs = list()
    blogContainers = soup.find_all('div', 'col-md-12 column corner-window shadow')
    for blogContainer in blogContainers:
        articles = blogContainer.find_all('div', 'col-md-12 column archive-cell')
        for article in articles:
            blog = dict()
            blog['id'] = article.a['href'].split('/')[-1:][0]
            blog['href'] = article.a['href']
            blog['title'] = article.a.string
            blog['publishTime'] = article.p.string
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
