import requests
from lxml import etree

url='https://movie.douban.com/subject/3097572/?from=showing'

r=requests.get(url).text

s=etree.HTML(r)
print(s.xpath('//div[@class="comment"]/p/span/text()'))

