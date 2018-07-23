# 解析 https://www.byvoid.com/blog/list 的脚本
from bs4 import BeautifulSoup

title = 'BYVoid'
base = 'https://www.byvoid.com'
origin = 'https://www.byvoid.com/'

def parseBYVoid(content=""):
    page = dict()
    page['origin'] = origin
    if not content:
        return page
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    # 去除非法字符 |
    page['title'] = title

    blogs = list()
    blogContainer = soup.section.table
    if blogContainer:
        items = blogContainer.find_all('tr')
        for item in items:
            blog = dict()
            for td, index in zip(item.find_all('td'), range(2)):
                if index == 0:
                    blog['publishTime'] = td.string
                else:
                    blog['id'] = td.a['href'].split('/')[-1:][0]
                    blog['href'] = base + td.a['href']
                    blog['title'] = td.a.string
                    if td.a.next_sibling:
                        blog['count'] = td.a.next_sibling.replace(' - ', '')
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
