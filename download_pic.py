import random
from urllib.request import urlretrieve
import os
import threading

# 下载300张验证码图片
url = 'http://www.moguproxy.com/proxy/validateCode/createCode?time={}'
# path = os.path.dirname(__file__) + '/origin_imgs/'  # 将下载的图片保存到当前目录下的origin_imgs文件夹中
path = 'D:\\EEEEEEEEEEEEEEEEEEEEEEEEEE\\origin_imgs\\'


# for i in range(1531878604000, 1531878604300):
#     urlretrieve(url.format(i), path + str(i)[-3:] + '.jpg')
#     print('成功下载 {} 张图片'.format(str(i)[-3:]))


def download_imgs(i):
    urlretrieve(url.format(i), path + str(i)[-3:] + '.jpg')
    print('成功下载 {} 张图片'.format(str(i)[-3:]))


thread_list = []

for i in range(1531878604000, 1531878604300):
    thread_list.append(threading.Thread(target=download_imgs, args=(i,)))


for th in thread_list:
    th.start()
    th.join()

print("300张图片全部下载完毕")