import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import xlwt
import xlrd

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.17zixueba.com')

time.sleep(30)

# 构造存入的excel
video_url = xlwt.Workbook(encoding='utf-8', style_compression=0)
video_sheet = video_url.add_sheet('17自学把', cell_overwrite_ok=True)
video_sheet.write(0, 0, '视频名称')
video_sheet.write(0, 1, '视频详情链接')
video_sheet.write(0, 2, '视频访问量')
video_sheet.write(0, 3, '视频评论量')
video_sheet.write(0, 4, '视频发布时间')
video_sheet.write(0, 5, '视频类型')
video_sheet.write(0, 6, '视频详情')
video_sheet.write(0, 7, '视频下载链接密码')
n = 1

# 读取excel
data = xlrd.open_workbook('17自学吧.xls')
table = data.sheet_by_index(0)
rows = table.nrows
cols = table.ncols

excel_list = []
for row in range(rows):
    if row > 0:
        row_value = table.row_values(row)
        excel_list.append(row_value)
        print(row_value[1])

# print(excel_list)
# 操作表格的数据
for i in range(len(excel_list)):
    r = excel_list[i]
    url = r[1]
    # url='https://www.17zixueba.com/forum.php?mod=viewthread&tid=1214&highlight=python'
    print("准备提取：{}".format(url))
    new_tab_js = "window.open('" + url + "')"
    driver.execute_script(new_tab_js)
    all_handles = driver.window_handles
    driver.switch_to_window(all_handles[1])
    try:
        time.sleep(5)
        detail_fonts = driver.find_element_by_xpath('//*[starts-with(@id,"postmessage_")]').find_elements_by_tag_name('font')
        detail_text = []
        for index, f in enumerate(detail_fonts):
            if index % 2 == 1:
                font_text = f.text
                detail_text.append(font_text)

        video_detail = " ".join(detail_text)
        link_psw_obj = driver.find_elements_by_class_name('showhide')
        if len(link_psw_obj)==2:
            link_psw=link_psw_obj[1].text
        else:
            link_psw=link_psw_obj[0].text


        print(video_detail + " | " + link_psw)

        video_sheet.write(n, 0, r[0])
        video_sheet.write(n, 1, r[1])
        video_sheet.write(n, 2, r[2])
        video_sheet.write(n, 3, r[3])
        video_sheet.write(n, 4, r[4])
        video_sheet.write(n, 5, r[5])
        video_sheet.write(n, 6, video_detail)
        video_sheet.write(n, 7, link_psw)
        n = n + 1

        driver.close()
        driver.switch_to_window(all_handles[0])
    except NoSuchElementException as e:
        print("提取出现异常:{}".format(e))
        video_sheet.write(n, 0, r[0])
        video_sheet.write(n, 1, r[1])
        video_sheet.write(n, 2, r[2])
        video_sheet.write(n, 3, r[3])
        video_sheet.write(n, 4, r[4])
        video_sheet.write(n, 5, r[5])
        video_sheet.write(n, 6, "提取异常")
        video_sheet.write(n, 7, "提取异常")
        n = n + 1
        driver.close()
        driver.switch_to_window(all_handles[0])


    print(i)
    # if i == 5:
    #     break

video_url.save('17自学吧detail.xls')
