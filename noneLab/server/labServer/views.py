from django.shortcuts import render,HttpResponse
import os
import base64
from django import forms

#image为存储图片信息的列表,存储编码后的图像

image=[1]
getImgStates=False
transImgStates=False

class soundForm(forms.Form):
    soundData=forms.CharField()


class imgForm(forms.Form):
    data=forms.CharField()


#将image中存储的数据解码后取出,并传输给请求对象
#注意:此处并未验证请求者身份
def transImg(request,):
    transImgStates=False
    img=base64.b64decode(image[0])
    print(img)


#    while True:
#        if getImgStates==False:
#            continue
#        else:
#            img=image[0]
#            transImgStates=True
#            break

#    return HttpResponse(img)
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


