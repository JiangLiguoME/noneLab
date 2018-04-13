#!/usr/bin/env python
# coding=utf-8

import cv2
import base64
import time
import os


try:
    import requests
except IOError:
    print("Failed to import the lib requests!Trying to install it ... ")
    os.system("pip install requests")
    print("Installing the package requests...")



class transImg():
    def __init__(self,url):
        self.cam=cv2.VideoCapture(0)
        self.readState=False
        self.tranState=False
        self.data={}

    def catchImg(self):
        self.readState=False
        rat,self.frame=self.cam.read()
        cv2.imwrite("tmp.jpg",self.frame)

        with open("tmp.jpg","rb+") as f:
            self.image=f.read()
        print("Succeed to catch the image!")
        self.readState=True
        self.data['data']=base64.b64encode(self.image)

    def postImg(self):
        self.tranState=False
        count=0

        while count<3:
            req=requests.post(url,self.data)
            if req.status_code==200:
                self.tranState=True
                print("Succeed to transport image data")
                break


#url="http://118.190.148.154:8080/image"
url="http://0.0.0.0:8080/upImage"
cam1=transImg(url)

while 1:
    cam1.catchImg()
    try:
        cam1.postImg()
        time.sleep(0.2)
    except KeyboardInterrupt:
        os.exit()
    except:
        continue


