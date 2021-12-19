import requests

# 热门研报
# type 1 最新
# type 2 近一周
# type 3 新财富分析师

page_num = 50
hot_new_url = "https://www.fupanyoudao.com/v1/api/report?page_num=%d&page_size=10&type=1"
hot_later_url = "https://www.fupanyoudao.com/v1/api/report?page_num=50&page_size=10&type=2"
hot_new_reseach_url = "https://www.fupanyoudao.com/v1/api/report?page_num=50&page_size=10&type=3"

# page_url = "https://www.fupanyoudao.com/v1/api/report?page_num=%d&page_size=10&type=1"

def GetDataFromUrl(_url):
    headers = { 
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'Referer': 'https://servicewechat.com/wxe04e1890bc944202/33/page-frame.html',
        'Host': 'www.fupanyoudao.com'
    }
    ret = requests.get(headers=headers, url=_url)
    return ret

def GetPageNum():
    page_url = hot_new_url % page_num
    print(page_url)
    ret = GetDataFromUrl(page_url)
    print(ret.content)

def GetPageContent():
    headers = { 
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'Referer': 'https://servicewechat.com/wxe04e1890bc944202/33/page-frame.html',
        'Host': 'www.fupanyoudao.com'
    }
    pass


if __name__ == '__main__':
    # 获取页数
    GetPageNum()