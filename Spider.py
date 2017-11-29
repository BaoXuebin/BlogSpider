from NetUtils import NetUtils

if __name__ == '__main__':
    result = NetUtils.request('https://www.pigjian.com/article')
    # 写入文件
    file_object = open('html.txt', 'wb')
    file_object.write(result.get('content'))
    file_object.close()
