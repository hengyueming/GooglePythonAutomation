#!/usr/bin/env python3
import os
import sys
import requests
import json

url = 'http://localhost/fruits/'
path = 'supplier-data/descriptions/'
descriptions = os.listdir(path)

for info in descriptions:
        if info.endswith('.txt'):
                with open(path + info, 'r') as file:
                        data = file.read().split('\n')
                        image_names = os.path.splitext(info)[0]
                        fruits = {'name': data[0].strip(), 'weight': int(data[1].strip(' lbs')), 'description': data[2].strip(), 'image_name': image_names  + '.jpeg'}
                        r = requests.post(url, json=fruits)
                        r.raise_for_status()
                        print(data[0] + ': ' + data[2] + 'already uploaded to:' + r.request.url)
