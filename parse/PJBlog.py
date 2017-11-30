# 解析 PJBlog 的脚本
from bs4 import BeautifulSoup

def parsePJBlog(content=""):
    page = dict()
    if not content:
        return page
    # 获取 soup 对象
    soup = BeautifulSoup(content, 'html.parser')
    # 页面标题
    page['title'] = soup.title.string

    blogs = list()
    blogContainers = soup.find_all('div', 'container list')
    for blogContainer in blogContainers:
        for media in blogContainer.find_all('div', 'media'):
            blog = dict()
            a = media.h6.a
            # 博客 id
            blog['id'] = a['href'].split('/')[-1:][0]
            # 博客标题
            blog['title'] = a.string.replace('\n', '')
            # 博客地址
            blog['href'] = a['href']
            infos = media.find_all('div', 'info')
            if len(infos) > 0:
                info = infos[0]
                for i in info.find_all('i'):
                    clsAttr = ''.join(i.get('class'))
                    if clsAttr == 'ion-person':
                        # 作者
                        blog['author'] = i.next_sibling.replace('\n', '')
                    elif clsAttr == 'ion-clock':
                        # 发布时间
                        blog['publishTime'] = i.next_sibling.replace('\n', '').replace('\xa0,\xa0', '')
                    elif clsAttr == 'ion-ios-eye':
                        # 浏览次数
                        blog['count'] = i.next_sibling.replace('\n', '')
            blogs.append(blog)

    # 所有博客列表
    page['blogs'] = blogs
    page['blogCount'] = len(blogs)
    return page
