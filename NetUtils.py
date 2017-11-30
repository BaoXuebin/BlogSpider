# -*- coding:utf-8 -*-
import ssl
from urllib import request

class NetUtils(object):

    @staticmethod
    def request(url):
        req = request.Request(url)
        # 伪装浏览器
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)    Chrome/53.0.2785.101 Safari/537.36')
        # 请求 url
        error = None
        result = None
        context = ssl._create_unverified_context()
        with request.urlopen(req, timeout=10, context=context) as f:
            if f.status == 200:
                try:
                    result = f.read()
                except Exception as e:
                    error = 'error' + 'UnicodeEncodeError'
            else:
                error = 'error: ' + f.status
        return { 'error': error, 'content': result };
