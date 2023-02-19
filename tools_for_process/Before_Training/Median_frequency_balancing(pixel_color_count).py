#!/usr/bin/env python
# coding: utf-8


from PIL import Image
import os



i = 1
j = 1
x = 0 #表示pixel為紅色的數量
y = 0 #表示pixel為黑色的數量

path = input('Input your path of trainset: ')
path = path.replace('\\', '/') + '/'

img_file = os.listdir(path)
picture_amount = len(img_file)

for p in range(picture_amount): #首先匯入圖片
    name = '%d-1_Color.png'%(p+1)
    img = Image.open(path + name)

    width = img.size[0]#圖片寬度
    height = img.size[1]#圖片長度
    
    for i in range(width):#遍歷所有寬度的pixel
        for j in range(height):#遍歷所有長度的pixel
            data = (img.getpixel((i, j)))#取得該圖片指定位置的pixel
            if (data > 0):#pixel的值大于 0 = 當pixel不為純黑色
                x += 1 #紅色計數+1
            else:
                y += 1 #黑色計數+1

print('num of labeled pixel: {}'.format(x))
print('num of background pixel: {}'.format(y))



all_pixel = width * height * picture_amount

fla = x/all_pixel
fba = y/all_pixel

median = 0.5

wla = median/fla
wba = median/fba



print('確認pixel總數: {}'.format(all_pixel))
print('確認屬於labeled之pixel數: {}'.format(all_pixel - y))
print('確認屬於background之pixel數: {}'.format(all_pixel - x))
print('label權重應調整為: {}'.format(wla))
print('background權重應調整為: {}'.format(wba))
