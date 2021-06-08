from bs4 import BeautifulSoup
import requests
import re
import json
import random
import time
import pandas as pd

'''
定义get函数，取得HTML文件并伪装爬虫。
1. 代码执行前暂停0.1s
2. 随机一个文件头出来（User-Agent）
取得html文件
'''

def get_html(url):

    time.sleep(0.1)
    my_headers = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
                    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
                    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ']
    headers = {'user-agent': random.choice(my_headers)}
    try:    
        html = requests.get(url,headers=headers)
        return html.text
    except requests.exceptions.RequestException:
        print(url,'请求失败')


#写完先去吃饭，饿死我了。


'''
重头戏，爬虫的处理
首先对down下来的网页进行分析，找到需要爬取的数据
使用正则表达式和re提取数据
'''

def parse_html(html):
    
    # title = re.findall('<em>(.*?)</em>',html,re.S)
    # del(title[0])
    # return title

    pattern = '''<em>(.*?)</em>.*?<li class="intro">(.*?)</li>'''
    informations = re.findall(pattern,str(html),re.S)
    return(informations)
    



if __name__ == '__main__':
    #urls = [f'https://movie.douban.com/people/181401162/wish?start={i*15}' for i in range(0,35)]
     urls = 'https://movie.douban.com/people/181401162/wish?start=0'
html = get_html(urls)
list=parse_html(html)
name=["title","intro"]
test=pd.DataFrame(columns=name,data=list)
print(test)
test.to_csv('C:/Users/han/Desktop/Douban_Crawl/testcsv.csv',encoding='utf-8-sig')


