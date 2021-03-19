#!/usr/bin/env python3
import os
import sys
import requests

url = 'http://localhost/upload/'
path = 'supplier-data/images/'

image_dir = os.listdir(path)

for im in image_dir:
        if im.endswith('.jpeg'):
                with open(path + im, 'rb') as opened:
                        r = requests.post(url, files={'file': opened})
