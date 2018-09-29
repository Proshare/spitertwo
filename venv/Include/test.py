# -*- coding: utf-8 -*-
import sys
import lxml
import requests
import codecs
import time
from lxml import etree, html
import tomd

reload(sys)
sys.setdefaultencoding('utf8')  # 设置默认编码格式为'utf-8'

if sys.stdout.encoding != 'UTF-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout, 'strict')
if sys.stderr.encoding != 'UTF-8':
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr, 'strict')


def http_get(url):
    print
    '请求地址：{}'.format(url)
    '''
    '''
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel …) Gecko/20100101 Firefox/58.0'}
    resp = requests.get(url, headers=headers)  # 请求
    print
    '请求完成'
    if not resp:
        print
        '无响应内容'
        return
    print
    '响应:\nencoding={}'.format(resp.encoding)  # 如果中文乱码，如果requests没有发现http headers中的charset
    resp.encoding = 'gb2312'  # 设置响应编码（gbk、utf-8、gb2312）
    txt = resp.text  # 获取响应的html内容
    print
    '原始：\n{}'.format(txt)
    print
    '响应:\nencoding={}'.format(resp.encoding)


http_get('http://baidu.com')
