#!/usr/bin/env python
# coding=utf-8

import requests
import base64
from PIL import Image
import cv2
import time

url="http://0.0.0.0:8080/image"
count=0
num=0
startTime=time.time()
while 1:
    num=num+1
    data=requests.get(url).content
    filePath=str(count)+'.jpg'
    with open(filePath,"wb+") as f:
        f.write(data)
    img=cv2.imread(filePath)
    cv2.imshow('test',img)
    cv2.waitKey(100)
    if time.time()-startTime >= 5:
        print(num)




