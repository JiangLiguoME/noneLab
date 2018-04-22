#!/usr/bin/env python
# coding=utf-8

import cv2
import base64
import time
import os
import sys
import pyaudio,wave
import time,datetime
import wave2
import threading
try:
    import requests
except IOError:
    print("Failed to import the lib requests!Trying to install it ... ")
    os.system("pip install requests")
    print("Installing the package requests...")



class transImg():
#视频传输的类:  通过opencv采集图像,使用post方法将base64编码后的图像传输到指定网址
#               初始化参数cam为选定的摄像头,url为要提交的网址,frameNum为帧数,默认5帧
#               data为字典类型,'data'键中存放的键值即为数据
#               readState与tranState为采集与传输的标志位,为false表示正在进行
#
#               catchImg为捕捉图像数据的方法
#               postImg为传输数据的方法
#               run使捕捉与传输一直进行

    def __init__(self,cam,url,frameNum=5):
        self.cam=cam
        self.readState=False
        self.tranState=False
        self.data={}
        self.frameNum=frameNum

    def catchImg(self):
        self.readState=False
        rat,frame=self.cam.read()
        cv2.imwrite("tmp.jpg",frame)
        #cv2.imshow("catch",frame)
        cv2.waitKey(1)

        with open("tmp.jpg","rb+") as f:
            self.image=f.read()
        print("Succeed to catch the image!")
        self.readState=True
        self.data['data']=base64.b64encode(self.image)

    def postImg(self,reqTime=1):
        self.tranState=False
        count=0

        while count<10:
            try:
                req=requests.post(url,self.data)
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("Connecting to the server ...")
                time.sleep(reqTime)
                count=count+1
                continue

            if req.status_code==200:
                self.tranState=True
                print("Succeed to transport image data!")
                break
        else:
            print("Failed to connect to the server!Quiting ...")
            sys.exit()

    def run(self,condition=True):
        while condition:
            self.catchImg()
            self.postImg()
            time.sleep(1/self.frameNum)

#url="http://118.190.148.154:8080/image"
if __name__=="__main__":
    url="http://49.140.219.113:80/upImage"
    thing1 = threading.Thread(target=wave2.getSound_s)
    thing1.start()
    cam=cv2.VideoCapture(0)
    cam1=transImg(cam,url,frameNum=12)
    cam1.run()

