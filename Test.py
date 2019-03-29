# -*- coding:utf-8 -*-
import sys
from parse.Hchstudio import exports as Hchstudio
from NetUtils import NetUtils

url = Hchstudio.get("url")
title = Hchstudio.get("title")

# 抓取数据，保存至本地
def req():
    if url:
        response = NetUtils.get(url)
        with open(title + '.html', 'w', encoding='utf-8') as f:
            f.write(response)
        print(url, "网页抓取完毕")
    else:
        pass

def getContent():
    with open(title + '.html', 'r', encoding='utf-8') as f:
        return f.read()
    return ""

if __name__ == '__main__':
    # req()
    parser = Hchstudio.get("parser")
    print(parser(getContent()))
    