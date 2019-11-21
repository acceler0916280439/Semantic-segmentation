#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from PIL import Image


# In[ ]:


path = input('Input your raw picture path: ')
origin_path = path.replace('\\', '/')

path2 = input('Input your target path: ')
target_path = path2.replace('\\', '/')

img_file = os.listdir(origin_path)
file_amount = len(img_file)


# In[ ]:


for i in range(file_amount):
    Input = Image.open(origin_path + img_file[i])
    Input.save(target_path + '%d-1_Color.png'%(i+1))
    print('Success to transform the picture name into %d-1_Color.png'%(i+1))
    
print('Finished!')

