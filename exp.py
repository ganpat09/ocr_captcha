# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:59:14 2023

@author: pc
"""

# import base64 
# s = "data:image/jpg;base64, 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"

# base64_code = s.split("base64, ")[1]
# img_data = base64_code.encode()
# content = base64.b64decode(img_data)

# with open('captcha_imgs/x.jpg', 'wb') as fw:
#     fw.write(content)
# print(content)

from pathlib import Path
import os
import shutil

data_dir = Path("./captcha_imgs")


# Get list of all the images
images = sorted(list(map(str, list(data_dir.glob("*.jpg")))))
labels = [img.split(os.path.sep)[-1].split(".jpg")[0] for img in images ]
characters = set(char for label in labels for char in label)
 
print("Number of images found: ", len(images))
print("Number of labels found: ", len(labels))
print("Number of unique characters: ", len(characters))
print("Characters present: ", characters)

counter = 0
for img in images:
    name = img.split(os.path.sep)[-1].split(".jpg")[0]
    if "=" in name:
        shutil.move(img,f"captcha_with_label/{name}.jpg")
        counter += 1
        
print("Move file counter",counter)        
        