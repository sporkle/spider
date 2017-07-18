# -*- coding:utf8 -*-

from lxml import etree
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


url = 'http://www.id97.com/'

def get_info(url):
    html = requests.get(url)
    page_data = etree.HTML(html.text)
    link = page_data.xpath('//*[@id="normalDown"]/div/table/tbody/tr[1]/td[3]/a/@href')
    return link

def get_link(url):
    html = requests.get(url)
    page_data = etree.HTML(html.text)
    info = {}
    info['link'] = str(page_data.xpath('/html/body/div[1]/div/div/div[1]/div[2]/text()'))
    #info['mm'] = str(page_data.xpath('/html/body/div[1]/div/div/div[1]/h1/text()'))
    info['mm'] = re.search('style="font-size:14px;padding:10px;">(.*?)</h1>',html.text,re.S).group(1)
    print info['mm']
    return info

#保存信息
def saveinfo(info):
       f = open('97movies7-18-1.txt','a')
       for each in info:
            f.writelines('link: ' + each['link'] + '\n')
            f.writelines('mm: ' + each['mm'] + '\n' + '\n')
       f.close()

def get_movies_link(url):
    wb_data = requests.get(url)
    selector = etree.HTML(wb_data.text)
    link = selector.xpath('/html/body/div[1]/div[2]/div[3]/div/div/div/a/@href')
    classinfo = []
    for each in link:
        #info = requests.get(each)
        print 'get:' + each
        test_url = get_info(each)
        for one in test_url:
            urls = url + one
            test = get_link(urls)
            classinfo.append(test)

    saveinfo(classinfo)


get_movies_link(url)