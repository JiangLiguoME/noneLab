#!/usr/bin/env python
# coding=utf-8

import serial
import time
import threading
import requests
import json

stm32=serial.Serial('/dev/ttyUSB0',9600)
url = "http://127.0.0.1:8080/upData"

class MCU():
    def __init__(self,serialObj):
        self.mcu=serialObj
        self.data=''
        self.command=''
        self.scanTime=0.5
        self.getDataState=False
        self.getCommandState=False
        self.transDataState=False
        self.transCommandState=False
        self.transDataUrl='http://49.140.231.111:8080/upData'
        self.getCommandUrl='http://49.140.231.111:8080/getCommand'

    def getCommand(self):
        while True:
            self.command=requests.get(self.getCommandUrl).content
            time.sleep(self.scanTime)


    def transCommand(self):
    #对数据编码,并向self.mcu传输数据
        while True:
            if self.command == '':
                continue
            else:
                self.mcu.write(self.command.encode())
                self.command = ''

    def transData(self):
    #接受字符串参数,并将其包装成字典后使用post方法上传到url中
        time.sleep(self.scanTime)
        dataTmp={}
        dataDic={}

        for i in range(len(data)):
            dataTmp[str(i)] = data[i]
        dataTmp['num'] = len(data)
        dataDic = json.dumps(dataTmp)

        a=requests.post(url,json=dataDic)
    #    print(a.content)

    def getData(self):
    #作用:接受并解析串口数据
    #实现:
    #   协议:   aa(开始标志) + data1 + '-' + data2 + '-' +...+ datan + '-' + ee(结束标志)
    #   解析:不断读取,读到 aa 后开始进入数据记录状态,
    #        进入数据记录状态后,直到读到ee,此间把所有数据全读入dataBytes中
    #        将dataBytes解码,以-分割,构造数据列表dataList,列表记录所有传感器数据
    #        将dataList上传至服务器
        self.getDataState=False
        self.data=''
        dataList=[]
        count=100

        while True:
            if self.getDataState is True:
                while self.getDataState:
                    dataTmp=self.mcu.read()
                    if dataTmp == b'e':
                        if self.mcu.read() == b'e':
                            self.data= self.data.split('-')
                            print(self.data)
                            if self.data[0] == '':
                                del self.data[0]
                            #上传数据至服务器的函数upData(data)
                            self.getDataState = False
                            self.data=''
                            break
                    else:
                        self.data=self.data + dataTmp.decode()
            else:
                if self.mcu.read() == b's':
                    if self.mcu.read() == b's':
                        self.getDataState = True



#t1=threading.Thread(target=transData)
#t2=threading.Thread(target=getData)
#t1.start()
#t2.start()
#t1.join()
#t2.join()
test=MCU(stm32)
test.getData()

