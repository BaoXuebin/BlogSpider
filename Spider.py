# -*- coding:utf-8 -*-
import io
import sys
from NetUtils import NetUtils
from parse.PJBlog import parsePJBlog
from parse.ZiWenXie import parseZiWenXie
from parse.JackPuBlog import parseJackPuBlog
from parse.EnumsBlog import parseEnumsBlog
from parse.MaKaiQian import parseMaKaiQian
from parse.BYVoid import parseBYVoid
from parse.Chole import parseChole
from parse.YuanHeHe import parseYuanHeHe
from parse.Thankbabe import parseThankbabe
from parse.LittleWin import parseLittleWin
from Parse import parse

if __name__ == '__main__':
    blogActions = [
        # { 'url': 'https://www.pigjian.com/article', 'handler': parsePJBlog },
        # { 'url': 'https://www.ziwenxie.site/', 'handler': parseZiWenXie },
        # { 'url': 'http://www.jackpu.com/', 'handler': parseJackPuBlog },
        # { 'url': 'http://posts.enumsblog.com/list', 'handler': parseEnumsBlog },
        # { 'url': 'http://makaiqian.com/', 'handler': parseMaKaiQian },
        # { 'url': 'https://www.byvoid.com/blog/list', 'handler': parseBYVoid },
        # { 'url': 'http://www.chole.io/blog/archive.html', 'handler': parseChole },
        # { 'url': 'http://yuanhehe.cn/archives/', 'handler': parseYuanHeHe },
        # { 'url': 'https://blog.thankbabe.com/archive/', 'handler': parseThankbabe },
        { 'url': 'https://littlewin.wang/', 'handler': parseLittleWin }
    ]
    for blogAction in blogActions:
        print('+' + '--' * 20 + '+')
        try:
            response = NetUtils.get(blogAction.get('url'))
            parse(response.text, blogAction.get('handler'))
        except Exception as e:
            print(e)
            print(blogAction.get('url') + '访问失败')
    print('+' + '--' * 20 + '+')

    # response = NetUtils.get('https://littlewin.wang/')
    # with open('html.txt', 'w', encoding=response.encoding) as f:
    #     f.write(response.text)
