import io
import sys
from bs4 import BeautifulSoup

# 修改 windows 输出乱码，改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# 获取数据
f = open('html.txt', 'r', encoding='utf8')
content = f.read()
f.close()

soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())
