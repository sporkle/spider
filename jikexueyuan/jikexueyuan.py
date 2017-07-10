#-*-coding:utf-8-*-
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u'begin to spider0.0 WoW'
#翻页功能
    def geturl(self,url,lastpage):
        now_page = int(re.search('pageNum=(\d+)', url, re.S).group(1))
        page_group = []
        for i in range(now_page, lastpage + 1):
            link = re.sub('pageNum=\d+', 'pageNum=%s' % i, url, re.S)
            page_group.append(link)
        return page_group
#得到网站的源代码
    def getsource(self,url):
        html = requests.get(url)
        return html.text

#抓取每个课程的信息
    def geteveryclass(self,source):
        everyclass = re.findall('(<li id=.*?</li>)', source, re.S)
        return everyclass

#保存从每个课程中提取出我们需要的信息
    def getinfo(self,everyclass):
        info = {}
        info['link'] = re.search('class="lesson-info-h2"><a href="//(.*?)" target',everyclass,re.S).group(1)
        info['title'] = re.search('class="lessonimg" title="(.*?)"',everyclass,re.S).group(1)
        info['content'] =re.search('style="height: 0px; opacity: 0; display: none;">\n\t\t\t(.*?)\t\t</p>',everyclass,re.S).group(1)
        timeandlevel = re.findall('<em>(.*?)</em>',everyclass,re.S)
        info['classlevel'] = timeandlevel[1]
        classtime1 = re.search('class="time-icon"></i><em>(.*?)\n\t\t\t\t\t\t(.*?)</em>',everyclass,re.S).group(1)
        classtime2 = re.search('class="time-icon"></i><em>(.*?)\n\t\t\t\t\t\t(.*?)</em>',everyclass,re.S).group(2)
        info['classtime'] = classtime1 + classtime2
        info['learnnum'] =re.search('"learn-number">(.*?)</em>',everyclass,re.S).group(1)
        return info
#把结果保存到info.txt文件中去
    def saveinfo(self,classinfo):
        f = open('info-17.txt',"a")
        for each in classinfo:
            f.write('title: ' + each['title'] + '\n')
            f.write('link: ' + each['link'] + '\n')
            f.write('content: ' + each['content'] )
            f.write('classtime: ' + each['classtime'] + '\n')
            f.write('classlevel: ' + each['classlevel'] + '\n')
            f.write('learnnum: ' + each['learnnum'] + '\n' + '\n')
        f.close()

if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_link = jikespider.geturl(url,95)
    for link in all_link:
        print u'正在处理页面： ' + link
        html = jikespider.getsource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass:
            info = jikespider.getinfo(each)
            classinfo.append(info)
    jikespider.saveinfo(classinfo)