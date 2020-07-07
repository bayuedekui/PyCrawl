from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.itjc8.com/member.php?mod=logging&action=login")

# login_btn = driver.find_element_by_xpath('//*[@id="deanheader"]/div/div[4]/div/div/div/a[1]')
# login_btn.click()
#
# driver.refresh()

username_input = driver.find_element_by_xpath('//*[@id="username_LyFgJ"]')
password_input = driver.find_element_by_xpath('//*[@id="password3_LyFgJ"]')
pic_vertify = driver.find_element_by_xpath('//*[@id="seccodeverify_cSo5i5kg"]')
pic = driver.find_element_by_xpath('//*[@id="vseccode_cSo5i5kg"]/img')['src']
print("pic is : {}".format(str(pic)))
login_btn = driver.find_element_by_xpath('//*[@id="loginform_LyFgJ"]/div/div[6]/table/tbody/tr/td[1]/button/strong')
username_input.send_keys('bayuedekui')
password_input.send_keys('51392010mxzk@')
pic_vertify.send_keys("1234")

login_btn.click()
