from selenium import webdriver
import requests
from PIL import Image
import pytesseract
from io import BytesIO
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.itjc8.com/member.php?mod=logging&action=login")

# login_btn = driver.find_element_by_xpath('//*[@id="deanheader"]/div/div[4]/div/div/div/a[1]')
# login_btn.click()
#
# driver.refresh()

# username_input = driver.find_element_by_xpath('//*[@id="username_LyFgJ"]')
# password_input = driver.find_element_by_xpath('//*[@id="password3_LyFgJ"]')
# pic_vertify = driver.find_element_by_xpath('//*[@id="seccodeverify_cSo5i5kg"]')
# pic = driver.find_element_by_xpath('//*[@id="vseccode_cSo5i5kg"]/img')['src']
# print("pic is : {}".format(str(pic)))
# login_btn = driver.find_element_by_xpath('//*[@id="loginform_LyFgJ"]/div/div[6]/table/tbody/tr/td[1]/button/strong')
# username_input.send_keys('bayuedekui')
# password_input.send_keys('51392010mxzk@')
# pic_vertify.send_keys("1234")

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

pass

# login_btn = driver.find_element_by_name('loginsubmit').click()
