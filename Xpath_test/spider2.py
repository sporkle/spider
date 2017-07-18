#-*-coding:utf8-*-
from lxml import etree
import requests
import re
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

url = 'http://www.id97.com/movie/618808.html'

def get_info(url):
    html = requests.get(url)
    page_data = etree.HTML(html.text)
    #link1 = re.search('target="_blank"herf"(.*?)"',html,re.S)
    link = page_data.xpath('//*[@id="normalDown"]/div/table/tbody/tr[1]/td[2]/div/a/@id')
    #link = page_data.xpath('//*[@id="normalDown"]/div/table/tbody/tr[2]/td[2]/div/a/@id')
    link1 = page_data.xpath('/html/body/div[1]/div/div/div[1]/div[2]/text()')
    mm = page_data.xpath('//*[@id="normalDown"]/div/table/tbody/tr/td[2]/div/strong/text()')
    print link

get_info(url)