import json

import pymysql
from selenium import webdriver
from PIL import Image
import time
import chaojiying
import random

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.itjc8.com/member.php?mod=logging&action=login")

# 获取用户名输入框
username_input = driver.find_element_by_name('username').send_keys('bayuedekui')
# 获取密码输入框
psw_input = driver.find_element_by_name('password').send_keys('51392010mxzk@')
time.sleep(10)
# 截下整个屏幕
driver.save_screenshot('D:\\login_printscreen.png')
# 找到验证码图片元素
vertify_pic = driver.find_element_by_xpath("//*[starts-with(@id, 'vseccode_')]/img")

location = vertify_pic.location
size = vertify_pic.size  # 获取验证码的长宽
rangle = (int(location['x'] + 156), int(location['y']) + 130, int(location['x'] + 156 + size['width'] + 20),
          int(location['y'] + 130 + size['height'] + 16))  # 写成我们需要截取的位置坐标
i = Image.open("D:\\login_printscreen.png")  # 打开截图
frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
frame4.save('D:\\login_save.png')  # 保存我们接下来的验证码图片 进行打码

# 调用超级鹰接口实现验证码识别
chaojiying_util = chaojiying.Chaojiying_Client('bayuedekui', '123456', '906415')
img = open('D:\\login_save.png', 'rb').read()
vertify_code = chaojiying_util.PostPic(img, '1902')

print(vertify_code.get('pic_str'))
# 获取验证码输入框
vertify_code_input = driver.find_element_by_xpath("//*[starts-with(@id,'seccodeverify_')]")
vertify_code_input.send_keys(vertify_code.get('pic_str'))

# 点击登录
login_btn = driver.find_element_by_name('loginsubmit').click()

# time.sleep(60)
# # 选择今日心情
# driver.find_element_by_xpath('//*[@id="ng"]/center/img').click()
# # 设置个随机数组，里面存放几句今日想说
arr = ['好好学习，天天向上daydayup', '台上一分钟，台下十年功', '宝剑锋从磨砺出，梅花香自苦寒来', '谦虚使人进步，骄傲使人落后']
rnd = random.randint(0, 3)
# driver.find_element_by_xpath('//*[@id="todaysay"]').send_keys(arr[rnd])
# # 点击签到
# driver.find_element_by_xpath('//*[@id="qiandao"]/p/button').click()

# 保存cookie
cookie_list = driver.get_cookies()
# print("cookie is:{}".format(cookie))

# 将cookie写入文件
# with open('cookie.txt', 'w', encoding='utf-8') as f:
#     f.write(str(cookie))

# 读取数据库存储的信息
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='video_crawl', charset='utf8')
cur = conn.cursor()
sql = 'select * from video_info'
cur.execute(sql)
data_file = list(cur.fetchall())
cur.close()

# 将所有的未回复的全部自动化回复
for row in data_file:
    url = row[2]
    print("即将开始访问：{}".format(url))
    # 设置cookie
    js = window.open('http://www.wlzhys.com','_self','')
    print(js)
    driver.execute_script(js)
    # for coo in cookie_list:
    #     print(str(coo))
    #     driver.add_cookie(coo)
    # time.sleep(10)
    # driver.refresh()

    reply_btn = driver.find_element_by_xpath("//*[starts-with(@id,'postmessage_')]/div/a")
    if reply_btn is not None:
        reply_btn.click()
        time.sleep(20)
        reply_input = driver.find_element_by_xpath('//*[@id="postmessage"]').send_keys(arr[rnd])
        reply_vertify_code = driver.find_element_by_xpath('//*[starts-with(@id,"seccodeverify_"]').click()
        time.sleep(10)
        # 截图
        driver.save_screenshot('D:\\reply_printscreen.png')
        reply_vertify_location = reply_vertify_code.location
        print("验证码大小为：{}".format(size))
        rangle = (int(reply_vertify_location['x'] + 20), int(reply_vertify_location['y']) + 40,
                  int(reply_vertify_location['x'] + 20 + size['width'] + 20),
                  int(reply_vertify_location['y'] + 40 + size['height'] + 16))  # 写成我们需要截取的位置坐标
        i = Image.open("D:\\reply_printscreen.png")  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save('D:\\reply_save.png')  # 保存我们接下来的验证码图片 进行打码
        break
