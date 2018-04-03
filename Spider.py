# -*- coding:utf-8 -*-
import io
import sys
import time
sys.path.append('parse')
from NetUtils import NetUtils
from PJBlog import parsePJBlog
from ZiWenXie import parseZiWenXie
from JackPuBlog import parseJackPuBlog
from EnumsBlog import parseEnumsBlog
from MaKaiQian import parseMaKaiQian
from BYVoid import parseBYVoid
from Chole import parseChole
from YuanHeHe import parseYuanHeHe
from Thankbabe import parseThankbabe
from LittleWin import parseLittleWin
from Marco import parseMarco
from CoolShell import parseCoolShell
from Tuobaye import parseTuobaye
from Jilinwula import exports as Jilinwula
from Parse import parse

if __name__ == '__main__':
    blogActions = [
        # { 'url': 'https://www.pigjian.com/article', 'handler': parsePJBlog },
        { 'url': 'https://www.ziwenxie.site/', 'handler': parseZiWenXie },
        { 'url': 'http://www.jackpu.com/', 'handler': parseJackPuBlog },
        { 'url': 'http://posts.enumsblog.com/list', 'handler': parseEnumsBlog },
        { 'url': 'http://makaiqian.com/', 'handler': parseMaKaiQian },
        { 'url': 'https://www.byvoid.com/blog/list', 'handler': parseBYVoid },
        { 'url': 'http://www.chole.io/blog/archive.html', 'handler': parseChole },
        { 'url': 'http://yuanhehe.cn/archives/', 'handler': parseYuanHeHe },
        { 'url': 'https://blog.thankbabe.com/archive/', 'handler': parseThankbabe },
        { 'url': 'https://littlewin.wang/', 'handler': parseLittleWin },
        { 'url': 'http://www.hanyuehui.site/get-articles?count=15&type=1', 'handler': parseMarco },
        { 'url': 'https://coolshell.cn/', 'handler': parseCoolShell },
        { 'url': 'http://tuobaye.com/#blog', 'handler': parseTuobaye },
        { 'url': Jilinwula.get('url'), 'handler': Jilinwula.get('parser') },
    ]
    date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print('+' + '--' * 6 + date + '--' * 6 + '+')
    for blogAction in blogActions:
        try:
            content = NetUtils.get(blogAction.get('url'))
            parse(content, blogAction.get('handler'))
        except Exception as e:
            print(e)
            print(blogAction.get('url') + '访问失败')

    # response = NetUtils.get('http://tuobaye.com/#blog')
    # with open('html.txt', 'w', encoding='utf-8') as f:
    #     f.write(response)
