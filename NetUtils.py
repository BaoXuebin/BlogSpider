# -*- coding:utf-8 -*-
import requests

class NetUtils(object):

    @staticmethod
    def get(url, encoding='utf-8'):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        response = requests.get(url, timeout=15, headers=headers)
        if response.encoding:
            return response.text.encode(response.encoding).decode(encoding)
        return response.content
