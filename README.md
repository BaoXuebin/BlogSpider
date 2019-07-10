关注了几个博主的个人博客，每次查看太麻烦，遂写此程序查看博主的更新状况。

> Python 对我还是太陌生啊。

关注的博客列表：

- [Jack Pu's Blog (蒲小花的博客－ポーのブログ)](http://www.jackpu.com/)
- [BYVoid](https://www.byvoid.com/)
- [SFLYQ](https://blog.thankbabe.com/)
- [小麻雀](http://makaiqian.com/)
- [yuanhehe' blog](http://yuanhehe.cn/)
- [littlewin.wang - 琪中有不凡 | littlewin.wang](https://littlewin.wang/)
- [酷 壳 - CoolShell](https://coolshell.cn/)
- [拓跋的前端客栈](http://tuobaye.com/#blog)
- [吉林乌拉](http://jilinwula.com/)
- [阮一峰的网络日志](http://www.ruanyifeng.com/blog/)
- [阿里中间件团队博客](http://jm.taobao.org/)
- [代码星冰乐](http://www.hchstudio.cn/)

依赖库

- `requests`
- `BeautifulSoup4`

第一次执行 `python Spider.py` 时，会拉取网站所有博客内容，并缓存至 `cache` 目录下。之后执行，则会比对这些缓存，列出更新内容。

运行效果图：

![https://raw.githubusercontent.com/BaoXuebin/BlogSpider/master/image/run.png](https://raw.githubusercontent.com/BaoXuebin/BlogSpider/master/image/run.png)
