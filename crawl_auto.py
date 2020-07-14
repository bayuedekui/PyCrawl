from selenium import webdriver
import json
from selenium.webdriver import ChromeOptions
import xlwt
import requests
from bs4 import BeautifulSoup
import time
import lxml

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}


# 去网站获取get请求
def request_get_website(url):
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            print("get success")
            resp.encoding = 'utf-8'
            return resp
    except requests.RequestException as e:
        return '请求出现异常：' + str(e)


# 构造存入的excel
video_url = xlwt.Workbook(encoding='utf-8', style_compression=0)
video_sheet = video_url.add_sheet('web前端', cell_overwrite_ok=True)
video_sheet.write(0, 0, '视频名称')
video_sheet.write(0, 1, '视频详情链接')
video_sheet.write(0, 2, '视频访问量')
video_sheet.write(0, 3, '视频评论量')
video_sheet.write(0, 4, '视频发布时间')
video_sheet.write(0, 5, '视频发布时间')
n = 1


def extract_url(bsp, video_type):
    list = bsp.find(id='threadlisttableid').find_all('th')
    for item in list:
        item_a = item.find('a')
        item_i = item.find(class_='y')
        if item_a and item_i:
            if item_a.get('href') != 'javascript:void(0);':
                item_name = item_a.string
                item_url = item_a.get('href')
                item_see = item_i.find(class_='dean_view').string
                item_reply = item_i.find(class_='dean_reply').string
                item_release = item_i.find(class_='dean_ftdate').string
                print(str(item_name) + ' | ' + str(
                    item_url) + ' | ' + item_see + ' | ' + item_reply + ' | ' + item_release)
                global n
                video_sheet.write(n, 0, item_name)
                video_sheet.write(n, 1, item_url)
                video_sheet.write(n, 2, item_see)
                video_sheet.write(n, 3, item_reply)
                video_sheet.write(n, 4, item_release)
                video_sheet.write(n, 5, video_type)
                n = n + 1


def main(url, video_type):
    resp = request_get_website(url)
    bsp = BeautifulSoup(resp.content, 'lxml')
    extract_url(bsp, video_type)
    time.sleep(5)


if __name__ == '__main__':
    url_list = ['https://www.itjc8.com/forum-36-page.html',
                'https://www.itjc8.com/forum-43-page.html',
                'https://www.itjc8.com/forum-38-page.html',
                'https://www.itjc8.com/forum-38-page.html',
                'https://www.itjc8.com/forum-60-page.html',
                ]
    pages_list = [14, 17, 7, 3, 5]
    name_list = ['web前端.xls', 'java视频教程.xls', 'python视频教程.xls', '微信开发视频教程.xls', '大数据云计算.xls']
    for index, pa in enumerate(pages_list):
        for i in range(1, pa):
            url = url_list[index].split('page')[0] + str(i) + url_list[index].split('page')[1]
            print("开始{}第{}页数提取{}".format(name_list[index], i, url))
            main(url, str(pages_list[index]).split('.')[0])

        video_url.save(name_list[index])
        n = 1
