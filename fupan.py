import requests
import json

from fpdata import *
from Middleware import *
# 热门研报
# type 1 最新
# type 2 近一周
# type 3 新财富分析师

page_num = 50
hot_new_url = "https://www.fupanyoudao.com/v1/api/report?page_num=%d&page_size=%d&type=1"
hot_later_url = "https://www.fupanyoudao.com/v1/api/report?page_num=50&page_size=10&type=2"
hot_new_reseach_url = "https://www.fupanyoudao.com/v1/api/report?page_num=50&page_size=10&type=3"

# detail_base_url + source ID
detail_base_url = "https://www.fupanyoudao.com/v1/api/report/report_detail?source_id=%s"

# page_url = "https://www.fupanyoudao.com/v1/api/report?page_num=%d&page_size=10&type=1"

def GetDataFromUrl(_url):
    headers = { 
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'Host': 'www.fupanyoudao.com'
    }
    ret = requests.get(headers=headers, url=_url)
    return ret

def GetResNum():
    page_url = hot_new_url % page_num
    print(page_url)
    ret = GetDataFromUrl(page_url)
    
    print(ret.content)

    geturl = json.loads(ret.content)
    total = geturl["total"]
    print(total)

def GetPageContent():
    # headers = { 
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    #     'Referer': 'https://servicewechat.com/wxe04e1890bc944202/33/page-frame.html',
    #     'Host': 'www.fupanyoudao.com'
    # }
    page_url = hot_new_url % (1, 411)
    print(page_url)
    ret = GetDataFromUrl(page_url)  

    json_root = json.loads(ret.content)
    fplist=[]
    for json_data in json_root["data"]:
        # print(json_data["id"] + "  " + json_data["title"] + "  " + json_data["source_id"])
        data = fpdata(json_data)
        insert_data("fpyd_hot", data.toArray())
        # fplist.append(data)
    

    # insert_data("fpyd_stock", aa.toArray())


if __name__ == '__main__':
    # 获取页数
    # total = GetResNum()

    GetPageContent()

