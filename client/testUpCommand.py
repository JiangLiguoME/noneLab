#!/usr/bin/env python
# coding=utf-8

import requests

data={'command':1}
url='http://127.0.0.1:8080/command'

while True:
    data['command']=input()
    print(data)
    requests.post(url,data)
