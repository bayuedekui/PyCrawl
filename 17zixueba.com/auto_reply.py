import selenium
import time
from selenium import webdriver
import random
import xlrd
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.17zixueba.com')

# 人工完成登录
time.sleep(30)


def new_tab(url):
    new_tab_js = "window.open('" + url + "')"
    driver.execute_script(new_tab_js)
    # 切换当前句柄
    all_handles = driver.window_handles
    driver.switch_to_window(all_handles[1])

    # 实现自动回复
    try:
        locked = driver.find_element_by_class_name('locked')
        try:
            driver.find_element_by_link_text('回复').click()
            time.sleep(5)
            replu_list = ['台上一分钟，台下十年功', '课程不错，谢谢楼主', '多接触新鲜事物，新鲜思想。。。', '习惯形成性格，性格决定命运。。。']
            rnd = random.randint(0, 3)
            driver.find_element_by_xpath('//*[@id="postmessage"]').send_keys(replu_list[rnd])
            driver.find_element_by_xpath('//*[@id="postsubmit"]/span').click()
            time.sleep(5)
            driver.close()
            driver.switch_to_window(all_handles[0])
        except NoSuchElementException as e:
            print("出错：{}".format(e))
            driver.close()
            driver.switch_to_window(all_handles[0])
    except NoSuchElementException as e:
        # 表示已经回复过了，继续下一个
        print("访问结果：{}:::该页面已回复".format(url))
        driver.close()
        driver.switch_to_window(all_handles[0])


if __name__ == '__main__':
    url_list = []
    data = xlrd.open_workbook('17自学吧.xls')
    table = data.sheet_by_index(0)
    rows = table.nrows
    cols = table.ncols
    for r in range(rows):
        if r > 0:
            url_list.append(table.cell(r, 1).value)

    # print(url_list)

    for i in range(0, len(url_list)):
        try:
            print("开始访问：{}".format(url_list[i]))
            new_tab(url_list[i])
        except RuntimeError as e:
            print(e)

