#!/usr/bin/python
import os

TAG = 'vu/qr:1.0.0'
MNT = '/results'
DIR = os.path.abspath('./')

os.system('cd src && docker build -t {} .'.format(TAG))

print("### RUNNING DOCKERIZED QR ###")
print(DIR, MNT)
os.system('docker run -v {}:{} {} ./main.py -D{}'.format(DIR, MNT, TAG, MNT))
