#!/usr/bin/env python3
import os
import sys
from PIL import Image

path = 'supplier-data/images/'
image_dir = os.listdir(path)

for image in image_dir:
        if 'tiff' in image:
                file_name = os.path.splitext(image)[0]
                im = Image.open(path + image)
                im.convert('RGB').resize((600,400)).save(path + file_name + '.jpeg', 'JPEG')
