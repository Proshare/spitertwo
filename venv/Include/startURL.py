# 这是启动爬取爬虫页面
import combinURL
import downloadDIR
import re

print("输入贴吧地址")
url = input('')
if not url:
    print("没有地址输入正在使用默认地址(baidu壁纸吧)")
    url = 'https://tieba.baidu.com/f?kw=%E5%A3%81%E7%BA%B8&ie=utf-8'
page = ''
while True:
    print("输入要下载的帖子个数")
    page = input()
    page = int(page)

    print("正在下载图片")
    ArticleLinks = combinURL.combinURL(url)
    downloadDIR.downloadDIR(ArticleLinks, page)
    print("下载完成")
