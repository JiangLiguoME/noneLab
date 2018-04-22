#!/usr/bin/env python
# coding=utf-8

import requests
import time

url='http://127.0.0.1:8080/getCommand'

while True:
    data=requests.get(url)
    if data.content is not b'':
        print(data.content)
    time.sleep(0.1)

