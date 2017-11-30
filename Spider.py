# -*- coding:utf-8 -*-
from NetUtils import NetUtils
from parse.PJBlog import parsePJBlog
from parse.ZiWenXie import parseZiWenXie
from parse.JackPuBlog import parseJackPuBlog
from parse.EnumsBlog import parseEnumsBlog
from parse.MaKaiQian import parseMaKaiQian
from parse.BYVoid import parseBYVoid
from Parse import parse

if __name__ == '__main__':
    blogActions = [
        { 'url': 'https://www.pigjian.com/article', 'handler': parsePJBlog },
        { 'url': 'https://www.ziwenxie.site/', 'handler': parseZiWenXie },
        { 'url': 'http://www.jackpu.com/', 'handler': parseJackPuBlog },
        { 'url': 'http://posts.enumsblog.com/list', 'handler': parseEnumsBlog },
        { 'url': 'http://makaiqian.com/', 'handler': parseMaKaiQian },
        { 'url': 'https://www.byvoid.com/blog/list', 'handler': parseBYVoid }
    ]
    for blogAction in blogActions:
        print('+' + '--' * 20 + '+')
        try:
            content = NetUtils.request(blogAction.get('url')).get('content')
            parse(content, blogAction.get('handler'))
        except:
            print(blogAction.get('url') + '访问超时')
    print('+' + '--' * 20 + '+')
