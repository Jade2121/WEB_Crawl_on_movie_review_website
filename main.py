from bs4 import BeautifulSoup
import requests
import re
import json
import random
import time

def get_html(url):

    time.sleep(0.1)
###代码执行前暂停0.1s,防止反爬虫

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
    headers = {
        'user-agent': random.choice(my_headers)
    }
###反反爬虫措施，随机一个文件头出来  

    try:    
        html = requests.get(url,headers=headers)
        return html.text
    except requests.exceptions.RequestException:
        print(url,'请求失败')
###取得url

#写完先去吃饭，饿死我了。


###开始写爬虫
def parse_html(html):
    '''Parse the HTML and extract the information you need'''
    
    title = re.findall('<em>(.*?)</em>',html,re.S)
    del(title[0])
    return title

    








if __name__ == '__main__':
#    urls = [f'https://movie.douban.com/people/181401162/wish?start={i*15}' for i in range(0,35)]
    urls = 'https://movie.douban.com/people/181401162/wish?start=0'
html = get_html(urls)
print(parse_html(html))


    # for url in urls:  
    #     html = get_html(url)
    #     books = parse_html(html)
    #     print_(books)