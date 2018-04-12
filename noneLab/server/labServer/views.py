from django.shortcuts import render,HttpResponse
import os
import base64
from django import forms

image=[1]

class soundForm(forms.Form):
    soundData=forms.CharField()


class imgForm(forms.Form):
    image=forms.CharField()


class imgFile(forms.Form):
    imageFile=forms.FileField()
# Create your views here.
def transImg(request,imageId):
    filePath=os.getcwd() + '/labServer/image/' + str(imageId) + '.jpg'

    with open(filePath,"rb") as f:
        img=f.read()

    return HttpResponse(img,content_type="image/png")

def recevSound(request):
    form = soundForm(request.POST)

    soundData = form.cleaned_data['soundData']
    filePath=os.getcwd + '/sound/test.wav'
    with open(filePath,"wb+") as f:
        f.write(soundData)

    return HttpResponse('save ok!')


def getImg(request):
    if request.method == 'POST':
        filePath=os.getcwd() + '/labServer/image/' + '10.png'
        image[0]=request.POST['image']
        image[0]=base64.b64decode(image[0])
        print(image[0])
        with open(filePath,"wb+") as f:
            f.write(image[0])
        form=imgForm(request.POST)
        if form.is_valid():
            print(image)

    return HttpResponse(request.POST)


