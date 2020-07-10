from PIL import Image
import os

path = os.path.dirname(__file__)
origin_path = 'D:\\FFFFFFFFFFFFFFFFFFFFFFFFFF\\origin_imgs\\'
new_path = 'D:\\FFFFFFFFFFFFFFFFFFFFFFFFFF\\clean_imgs\\'  # 用来存放处理好的图片

# 从100张图片中提取出字符样本
for image in os.listdir(origin_path)[:100]:
    im = Image.open(origin_path + image)
    width, height = im.size

    # 获取图片中的颜色，返回列表[(counts, color)...]
    color_info = im.getcolors(width * height)
    # 按照计数从大到小排列颜色，那么颜色计数最多的应该是背景，接下来排名2到6的则对应5个字符。
    sort_color = sorted(color_info, key=lambda x: x[0], reverse=True)

    # 根据颜色，提取出每一个字符，重新放置到一个新建的白色背景image对象上。每个image只放一个字符。
    char_dict = {}
    for i in range(1, 6):
        im2 = Image.new('RGB', im.size, (255, 255, 255))
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if im.getpixel((x, y)) == sort_color[i][1]:
                    im2.putpixel((x, y), (0, 0, 0))
                else:
                    im2.putpixel((x, y), (255, 255, 255))
        im2.save(new_path + str(i) + '-' + image.replace('jpg', 'tif'))
    print('成功处理图片{}'.format(image))