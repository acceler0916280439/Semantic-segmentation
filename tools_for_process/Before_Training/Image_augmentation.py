#!/usr/bin/env python
# coding: utf-8



from PIL import Image
import os



# 讀取圖像
path = input('Input your picture file path: ')
picture_path = path.replace('\\', '/') + '/'

filedir = os.listfir(picture_path)
picture_amount = len(filedir)

# 以下3種圖片處理方式，將增加3倍的資料量 = 原本資料量的4倍
for i in range(picture_amount):
    
    img = Image.open('{}{}-1_Color.png'.format(picture_path, '%d'%(i+1))) # 資料夾中的第一張圖片名稱: 1-1_Color.png
    
    # 圖像左右反轉並保存
    result1 = img.transpose(Image.FLIP_LEFT_RIGHT)
    result1.save('{}{}-1_Color.png'.format(picture_path, '%d'%(i + 1 + picture_amount*1)) ) # 擴增的第一張圖片名稱
    
    # 左右反轉後再上下反轉並保存
    #result1 = im.transpose(Image.FLIP_LEFT_RIGHT)
    result2 = result1.transpose(Image.FLIP_TOP_BOTTOM)
    result2.save('{}{}-1_Color.png'.format(picture_path, '%d'%(i + 1 + picture_amount*2)))
    
    # 圖像上下反轉並保存
    result3 = img.transpose(Image.FLIP_TOP_BOTTOM)
    result3.save('{}{}-1_Color.png'.format(picture_path, '%d'%(i + 1 + picture_amount*3)))

print('Done!')
