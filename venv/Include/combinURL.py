#这是给每个帖子加上没有的地址
import requests

from lxml import etree

def combinURL(url):
    html=requests.get(url)
    selector=etree.HTML(html.text);
    #通过xpath获取每个html后面url的后缀
    urlList=selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
    #在每个后缀后面加上百度的地址负责多线程抓取
    for i in range(len(urlList)):
        urlList[i]='https://tieba.baidu.com'+urlList[i]
    return urlList;

