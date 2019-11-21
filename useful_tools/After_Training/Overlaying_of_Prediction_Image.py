#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os


# In[2]:


# Overlaying_of_Prediction_Image

path = input('Input your image folder path: ')
path = path.replace('\\', '/') + '/'
img_file = os.listdir(path) #讀取整個資料夾該層的內容
img_amount = len(img_file) #用以計算資料夾中的圖片張數

for i in range(0, img_amount, 2): # 設定步長為2的原因:加疊兩張照片為一張
    if os.path.isfile(path + img_file[i][:-10] + '_overlay.png'):
        print('{}_overlay.png has already existed.'.format(img_file[i][:-10]))
        break
            
    elif i >= 100:
        buttom = path + img_file[i][:-10] + '_image.png'   # 重新命名圖片, 以方便迭代處理
        top = path + img_file[i][:-10] + '_prediction.png' # 重新命名圖片, 以方便迭代處理
        buttom = cv2.imread(buttom)
        top = cv2.imread(top)
        overlay_img = cv2.addWeighted(buttom, 0.7, top, 0.7, 0)
        cv2.imwrite(path + img_file[i][:-10] + '_overlay.png', overlay_img)
        print('Downloading {}_overlay.png: finished!'.format(img_file[i][:-10]))
        
    elif i>=10:
        buttom = path + img_file[i][:-10] + '_image.png'
        top = path + img_file[i][:-10] + '_prediction.png'
        buttom = cv2.imread(buttom)
        top = cv2.imread(top)
        overlay_img = cv2.addWeighted(buttom, 0.7, top, 0.7, 0)
        cv2.imwrite(path + img_file[i][:-10] + '_overlay.png', overlay_img)
        print('Downloading {}_overlay.png: finished!'.format(img_file[i][:-10]))
    
    else:
        buttom = path + img_file[i][:-10] + '_image.png'
        top = path + img_file[i][:-10] + '_prediction.png'
        buttom = cv2.imread(buttom)
        top = cv2.imread(top)
        overlay_img = cv2.addWeighted(buttom, 0.7, top, 0.7, 0)
        cv2.imwrite(path + img_file[i][:-10] + '_overlay.png', overlay_img)
        print('Downloading {}_overlay.png: finished!'.format(img_file[i][:-10]))
    
print('All finished!')


# In[ ]:




