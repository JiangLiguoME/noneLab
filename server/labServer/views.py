# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse
import os
import base64
from django import forms
import json

#image为存储图片信息的列表,存储编码后的图像
#command为存储命令的列表,第一项为命令是否更新标志,为true表示已更新,否则表示未更新
image=[1]
commandData=[False,'0']
getImgStates=False
transImgStates=False


class soundForm(forms.Form):
    soundData=forms.CharField()


class imgForm(forms.Form):
    data=forms.CharField()


class commandForm(forms.Form):
    command=forms.CharField()


#class dataForm(forms.Form):
#    data=forms.CharField()

#将image中存储的数据解码后取出,并传输给请求对象
#注意:此处并未验证请求者身份
def transImg(request,):
    transImgStates=False
    img=base64.b64decode(image[0])
    return HttpResponse(img,content_type="image/jpg")


#接收图像的函数,接收采用base64编码的图像,变量名为data
#接收到图像后,将其存储到image[0]中,不解码
def getImg(request):
    getImgStates=False
    if request.method == 'POST':
        form=imgForm(request.POST)
        if form.is_valid():
            image[0]=request.POST['data']
    getImgStates=True
    return HttpResponse(request.POST)


#发送声音的函数
def getSound(request,news_id):
    rootDir=os.getcwd()
    imagepath =rootDir+'/sound/'+str(news_id)+'.wav'

    with open(imagepath,"rb") as f:
        image_data=f.read()

    return HttpResponse(image_data,content_type="audio/wav") #注意旧版的资料使用mimetype,现在已经改为content_type


def getCommand(request):
#isGot为得到手机请求后给手机的反馈
#   1代表得到手机命令
#   0代表未接受到手机命令
    global commandData
    isGot=0

    if request.method == 'POST':
        form=commandForm(request.POST)
        if form.is_valid():
            commandData[1]=form.cleaned_data['command']
            isGot=1
            commandData[0]=True

    print(commandData)
    return HttpResponse(isGot)


def transCommand(request):
    global commandData
    print(commandData)
    if commandData[0] == True:
        commandData[0] = False
        return HttpResponse(commandData[1])
    else:
        return HttpResponse('')


def getData(request):
    data =json.loads(request.body.decode())
    print(data)
    #for i in data:
    #    print(i)
    #    print(data[i])
    return HttpResponse('Succeed to receive your data!')
