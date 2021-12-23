import requests
import json

from fpdata import *
from Middleware import *
# 热门研报
# type 1 最新
# type 2 近一周
# type 3 新财富分析师

page_num = 50


# 第一个tab页面 热门研报
# 近24小时
hot_new_url = "https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=%d&type=1"
# 近一周
hot_later_url = "https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=10&type=2"
# 新财富分析师
hot_new_reseach_url = "https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=10&type=3"

# 第二个页面 看涨预期
more_money_url = "https://www.fupanyoudao.com/v1/api/report/stock_expect?page_num=1&page_size=%d"

# 第三个tab页面 最新
# 最新数据
new_reseach_url = "https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=%d&type=0"

# 第四个tab页面 全部
# 个股研报
stock_reseach_url = "https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=%d&type=4"

# 行业
industry_reseach_url = "https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=%d&type=6"

# 策略
strategy_reseach_url = "https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=%d&type=5"

# 宏观
macro_reseach_url = "https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=%d&type=7"

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

def GetStockResearch():
    # https://www.fupanyoudao.com/v1/api/report?page_num=1&page_size=10&type=4
    page_url = stock_reseach_url % (1, 599)
    print(page_url)
    ret = GetDataFromUrl(page_url)  

    json_root = json.loads(ret.content)
    for json_data in json_root["data"]:
        # print(json_data["id"] + "  " + json_data["title"] + "  " + json_data["source_id"])
        data = fpdata(json_data)
        insert_data("fpyd_stock", data.toArray())

def GetStrategyResearch():
    page_url = strategy_reseach_url % (1, 621)
    print(page_url)
    ret = GetDataFromUrl(page_url)  

    json_root = json.loads(ret.content)
    for json_data in json_root["data"]:
        # print(json_data["id"] + "  " + json_data["title"] + "  " + json_data["source_id"])
        data = fpdata(json_data)
        insert_data("fpyd_strategy", data.toArray())

def GetIndustryResearch():
    page_url = industry_reseach_url % (1, 1449)
    print(page_url)
    ret = GetDataFromUrl(page_url)  

    json_root = json.loads(ret.content)
    for json_data in json_root["data"]:
        # print(json_data["id"] + "  " + json_data["title"] + "  " + json_data["source_id"])
        data = fpdata(json_data)
        insert_data("fpyd_industry", data.toArray())

if __name__ == '__main__':
    # 获取页数
    # total = GetResNum()

    GetIndustryResearch()

