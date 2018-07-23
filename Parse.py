import io
import sys
import json

from DB import insertByBatch

# 修改 windows 输出乱码，改变标准输出的默认编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
#
# # 获取数据
# f = open('html.txt', 'r', encoding='utf8')
# content = f.read()
# f.close()

def diffJson(page):
    try:
        with open('cache/' + page.get('title') + '.json', 'r') as f:
            oldPage = json.load(f)
            oldBlogIds = [ blog.get('id') for blog in oldPage.get('blogs') ]
            newBlogIds = [ blog.get('id') for blog in page.get('blogs') ]
            diffIds = []
            for id in newBlogIds:
                if id not in oldBlogIds:
                    diffIds.append(id)
                else:
                    break;
            # diffIds = [ id for id in newBlogIds if id not in oldBlogIds ]
            return [ blog for blog in page.get('blogs') if blog.get('id') in diffIds ]
    except:
        return page.get('blogs')

# 缓存 json 至本地
def cacheJson(page):
    with open('cache/' + page.get('title') + '.json', 'w') as f:
        json.dump(page, f)

def log(title, diff):
    length = len(diff)
    if length > 0:
        print('访问', title, ', ^-^ 博主又发布了', length, '篇博客:')
        for blog, i in zip(diff, range(length)):
            line = blog.get('title')
            if blog.get('publishTime'):
                line += ' [' + blog.get('publishTime') + ']'
            if blog.get('count'):
                line += ' [' + blog.get('count') + '次浏览]'
            if blog.get('comment'):
                line += ' [' + blog.get('comment') + '条评论]'
            print(i + 1, line)
    else:
        print('访问', title, ', 博主很懒，没有任何更新 :(')

# 输入爬取的文本内容
# 输出包含该页面信息的字典对象
def parse(content, handler):
    page = handler(content)
    title = page.get('title')
    origin = page.get('origin')
    # 页面数据比对，获取更新博客列表
    diff = diffJson(page)
    # 持久化
    # insertByBatch(diff, title, origin)
    # 输出数据内容
    log(title, diff)
    # 缓存页面数据
    cacheJson(page)