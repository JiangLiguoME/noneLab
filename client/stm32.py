#!/usr/bin/env python
# coding=utf-8

import serial
import time
import threading
import requests
import json

stm32=serial.Serial('/dev/ttyUSB0',9600)
print(stm32.isOpen())
url = "http://127.0.0.1:8080/upData"

def transData():
    while True:
        data='hello'
        data=data.encode()
        stm32.write(data)


def upData(data):
#接受字符串参数,并将其包装成字典后使用post方法上传到url中
    time.sleep(0.5)
    dataTmp={}
    dataDic={}

    for i in range(len(data)):
        dataTmp[str(i)] = data[i]
    dataTmp['num'] = len(data)
    dataDic = json.dumps(dataTmp)

    a=requests.post(url,json=dataDic)
#    print(a.content)

def getData():
#作用:接受并解析串口数据
#实现:
#   协议:   aa(开始标志) + data1 + '\n' + data2 + '\n' +...+ datan + '\n' + ee(结束标志)
#   解析:不断读取,读到 aa 后开始进入数据记录状态,
#        进入数据记录状态后,直到读到ee,此间把所有数据全读入dataBytes中
#        将dataBytes解码,以\n分割,构造数据列表dataList,列表记录所有传感器数据
#        将dataList上传至服务器
    getDataState=False
    dataBytes=b''
    dataList=[]
    count=100
    while True:

        if getDataState is True:
            while getDataState:
                dataTmp=stm32.read()
#                print(dataTmp)
                if dataTmp == b'e':
                    if stm32.read() == b'e':
                        data= dataBytes.decode().split('\n')
                        print(data)
                        if data[0] == '':
                            del data[0]
                        upData(data)
                        getDataState = False
                        dataBytes=b''
                        break
                else:
                    dataBytes=dataBytes + dataTmp

        else:
            if stm32.read() == b's':
                if stm32.read() == b's':
                    getDataState = True



#t1=threading.Thread(target=transData)
#t2=threading.Thread(target=getData)
#t1.start()
#t2.start()
#t1.join()
#t2.join()
getData()

