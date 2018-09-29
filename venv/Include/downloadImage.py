#这是下载图片的

import requests
from lxml import etree
import urllib

def downloadImage(url):

    html=requests.get(url)
    # page =urllib.request.urlopen(url)
    # html=page.read()
    #html = html.decode('utf-8')  # python3

    print(html)

    selector=etree.HTML(html.text)

    print(selector)

    img_url_list = selector.xpath('//*[@class="BDE_Image"]/@src')

    print(img_url_list)

    pic_name=0
    for i in img_url_list:
        urllib.request.urlretrieve(i,"pic_%s.jpg"%pic_name)
        pic_name +=1

