import time
import sys
import pymysql
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import xlwt
import xlrd
from openpyxl import Workbook
import sys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.17zixueba.com')

time.sleep(30)

# 从数据库中读取数据
con = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='video_crawl', charset='utf8')
cursor = con.cursor()
cursor.execute('select * from video_info')
data = cursor.fetchall()

print(data)
# 操作数据库的数据
for i in range(len(data)):
    r = data[i]
    id = r[0]
    url = r[2]
    is_crawl = r[7]
    if is_crawl is not None:
        print("该链接已经爬取。。。")
        continue
    else:
        print("【{}】准备id:{}提取：{}".format(i, id, url))
        new_tab_js = "window.open('" + url + "')"
        driver.execute_script(new_tab_js)
        all_handles = driver.window_handles
        driver.switch_to_window(all_handles[1])
        try:
            time.sleep(10)
            detail_fonts = driver.find_element_by_xpath(
                '//*[starts-with(@id,"postmessage_")]').find_elements_by_tag_name(
                'font')
            detail_text = []
            for index, f in enumerate(detail_fonts):
                if index % 2 == 1:
                    font_text = f.text
                    detail_text.append(font_text)

            video_detail = " ".join(detail_text)
            link_psw_obj = driver.find_elements_by_class_name('showhide')
            if len(link_psw_obj) == 2:
                link_psw = link_psw_obj[1].text
            elif len(link_psw_obj) == 1:
                link_psw = link_psw_obj[0].text
            else:
                link_psw = "该视频未回复"

            print(video_detail + " | " + link_psw)

            update_sql = "update video_info set video_detail='" + str(video_detail) + "', video_link_psw='" + str(link_psw) + "' where id='" + str(id) + "'"
            print("update_sql is:{}".format(update_sql))
            cursor.execute(update_sql)
            con.commit()

            driver.close()
            driver.switch_to_window(all_handles[0])
        except NoSuchElementException as e:
            print("提取出现异常:{}".format(e))

            driver.close()
            driver.switch_to_window(all_handles[0])

    # if i == 5:
    #     break

