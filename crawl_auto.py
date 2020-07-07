from selenium import webdriver
import json
from selenium.webdriver import ChromeOptions

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "cookie": "Hm_lvt_699a3d1b7b93f495a71ea0f8664e333e=1591805872,1593099986,1594139388; 7sAp_2132_sid=NFVfbG; 7sAp_2132_noticeTitle=1; 7sAp_2132_saltkey=H0vx4X77; 7sAp_2132_lastvisit=1594137306; 7sAp_2132_sendmail=1; 7sAp_2132_seccode=1317.2ce5cb345f020419d5; 7sAp_2132_ulastactivity=2caaKbv%2BiOXR9B6t2%2B6me%2BLqFpk1euYW7l7NDg51Dp3HCqpOFTD%2F; 7sAp_2132_auth=f8e3tGVMocYWQwGb9BQDJEgkNn7kTnscnx%2FXfUJScQDDKaZkwnrQShcMcb7Hur46SfXDMznVNn55XNu7xdQgK7Fu7Q; 7sAp_2132_lastcheckfeed=24243%7C1594141182; 7sAp_2132_checkfollow=1; 7sAp_2132_lip=183.206.165.195%2C1594140632; 7sAp_2132_connect_is_bind=1; 7sAp_2132_nofavfid=1; 7sAp_2132_onlineusernum=119; 7sAp_2132_checkpm=1; 7sAp_2132_lastact=1594141203%09index.php%09; Hm_lpvt_699a3d1b7b93f495a71ea0f8664e333e=1594141205"
}

# cookie = str(headers.get('cookie'))
# cookie_list = cookie.split(';')
# cookie = {}
# for item in cookie_list:
#     ite = item.split('=')
#     cookie[ite[0]] = ite[1]
#
# f1 = open('cookie.txt', 'w')
# f1.write(json.dumps(cookie))

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=option)
driver.get("https://www.itjc8.com")

with open('cookie.txt', 'r', encoding='utf-8') as f:
    cookie_list = json.loads(f.read())

for c in cookie_list:
    driver.add_cookie(c)

# driver.add_cookie(cookie_list)

driver.refresh()

