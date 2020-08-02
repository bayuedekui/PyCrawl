import pymysql
import xlrd

name_list = ['17自学吧.xls']

data_file = []


# 提取数据入库
def extract_data(file_name):
    table = xlrd.open_workbook(file_name).sheet_by_index(0)
    row = table.nrows
    for r in range(row):
        if r > 0:
            data_file.append(table.row_values(r))


for name in name_list:
    extract_data(name)
print(data_file)

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='video_crawl', charset='utf8')

for row in data_file:
    cur = conn.cursor()
    sql = "insert into video_info(video_name,video_url,video_visit,video_reply,video_release,video_type) values('{}','{}','{}','{}','{}','{}')".format(
        row[0], row[1], row[2], row[3], row[4], row[5])
    cur.execute(sql)
    cur.close()

# cur = conn.cursor()
# sql = 'select * from video_info'
# cur.execute(sql)
# res = list(cur.fetchall())
# print(res[0][2])

# conn.commit()
conn.close()
