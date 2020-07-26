import requests
from bs4 import BeautifulSoup
import re
import xlwt
import lxml
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}


def request_get_website(url):
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            resp.encoding = 'utf-8'
            return resp
    except requests.RequestException as e:
        print("requests 请求出现异常" + str(e))


def extract_url(bsp, video_type):
    video_url_list = bsp.find(id='threadlist').find_all('li')
    for item in video_url_list:
        # 获取包含视频地址的a
        item_a_name = item.find('h3').find('a').text
        item_a_href = item.find('h3').find('a').get('href')
        # 获取回复次数和浏览次数
        item_replysee = str(item.find(class_='xg1').string).split(' - ')
        item_reply = re.findall(r'\d+', item_replysee[0])[0]
        item_see = re.findall(r'\d+', item_replysee[1])[0]
        item_release = item.find_all('span')[0].string
        print(str(item_a_name) + ' || ' + str(item_a_href) + ' || ' + str(
            item_reply) + ' || ' + str(item_see) + ' || ' + str(item_release))

        global n
        video_sheet.write(n, 0, item_a_name)
        video_sheet.write(n, 1, item_a_href)
        video_sheet.write(n, 2, item_see)
        video_sheet.write(n, 3, item_reply)
        video_sheet.write(n, 4, item_release)
        video_sheet.write(n, 5, video_type)
        n = n + 1


category_name = ['python', 'hadoop', 'spark', '机器学习', '深度学习', 'tableau', 'stata', 'flume', 'sas', 'r', 'Tensorflow',
                 'matlab', 'spss', 'amos', 'django', 'pandas', '爬虫']

category_url = [
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233837&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233838&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233839&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233840&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233841&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233842&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233843&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233844&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233845&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233846&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233847&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233848&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233849&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233850&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233851&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233852&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=',
    'https://www.17zixueba.com/search.php?mod=forum&searchid=233853&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page='
]

pages = [10, 4, 3, 5, 3, 2, 1, 1, 2, 25, 1, 7, 2, 1, 1, 1, 2]


def main(url, video_type):
    resp = request_get_website(url)
    bsp = BeautifulSoup(resp.content, 'lxml')
    extract_url(bsp, video_type)
    time.sleep(5)


if __name__ == '__main__':
    # 构造存入的excel
    video_url = xlwt.Workbook(encoding='utf-8', style_compression=0)
    video_sheet = video_url.add_sheet('web前端', cell_overwrite_ok=True)
    video_sheet.write(0, 0, '视频名称')
    video_sheet.write(0, 1, '视频详情链接')
    video_sheet.write(0, 2, '视频评论量')
    video_sheet.write(0, 3, '视频访问量')
    video_sheet.write(0, 4, '视频发布时间')
    video_sheet.write(0, 5, '视频类别')
    n = 1

    # url = 'https://www.17zixueba.com/search.php?mod=forum&searchid=233867&orderby=lastpost&ascdesc=desc&searchsubmit=yes&page=1'
    # resp = request_get_website(url)
    # print(resp)
    # bsp = BeautifulSoup(resp.content, 'lxml')
    # extract_url(bsp, 'test')
    for index, cate in enumerate(category_name):
        for i in range(1, pages[index] + 1):
            url = category_url[index] + str(i)
            main(url, category_name[index])
    video_url.save('17自学吧.xls')
