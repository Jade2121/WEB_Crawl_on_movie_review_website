from bs4 import BeautifulSoup
import requests
import json

def get_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    try:
        html = requests.get(url,headers=headers)
        return html.text
    except requests.exceptions.RequestException:
        print(url,'请求失败')
#取得url,写完先去吃饭，饿死我了。






if __name__ == '__main__':
    urls = [f'https://movie.douban.com/people/181401162/wish?start={i*15}' for i in range(0,35)]
print(get_html(urls))
    # for url in urls:  
    #     html = get_html(url)
    #     books = parse_html(html)
    #     print_(books)