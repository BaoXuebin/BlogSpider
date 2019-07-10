# -*- coding:utf-8 -*-
import io
import sys
import time

from NetUtils import NetUtils
from Parse import parse
from parse.PJBlog import parsePJBlog
from parse.JackPuBlog import parseJackPuBlog
from parse.MaKaiQian import parseMaKaiQian
from parse.BYVoid import parseBYVoid
from parse.YuanHeHe import parseYuanHeHe
from parse.Thankbabe import parseThankbabe
from parse.LittleWin import parseLittleWin
from parse.Marco import parseMarco
from parse.CoolShell import parseCoolShell
from parse.Tuobaye import parseTuobaye
from parse.Jilinwula import exports as Jilinwula
from parse.Ruanyifeng import exports as Ruanyifeng
from parse.Jmtaobao import exports as Jmtaobao
# 代码星冰乐
from parse.Hchstudio import exports as Hchstudio
# 程序羊
from parse.CodeSheep import exports as CodeSheep

if __name__ == '__main__':
    blogActions = [
        { 'url': 'http://www.jackpu.com/', 'handler': parseJackPuBlog },
        { 'url': 'http://makaiqian.com/', 'handler': parseMaKaiQian },
        { 'url': 'https://www.byvoid.com/blog/list', 'handler': parseBYVoid },
        { 'url': 'http://yuanhehe.cn/archives/', 'handler': parseYuanHeHe },
        { 'url': 'https://blog.thankbabe.com/archive/', 'handler': parseThankbabe },
        { 'url': 'https://littlewin.wang/', 'handler': parseLittleWin },
        { 'url': 'https://coolshell.cn/', 'handler': parseCoolShell },
        { 'url': 'http://tuobaye.com/#blog', 'handler': parseTuobaye },
        { 'url': Jilinwula.get('url'), 'handler': Jilinwula.get('parser') },
        { 'url': Ruanyifeng.get('url'), 'handler': Ruanyifeng.get('parser') },
        { 'url': Jmtaobao.get('url'), 'handler': Jmtaobao.get('parser') },
        { 'url': Hchstudio.get('url'), 'handler': Hchstudio.get('parser') },
        { 'url': CodeSheep.get('url'), 'handler': CodeSheep.get('parser') }
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