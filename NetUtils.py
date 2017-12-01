# -*- coding:utf-8 -*-
import requests

class NetUtils(object):

    @staticmethod
    def get(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        return requests.get(url, timeout=10, headers=headers)
