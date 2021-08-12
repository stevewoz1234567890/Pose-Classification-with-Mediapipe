# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 08:07:05 2021

@author: koala
"""
import cv2
vidcap = cv2.VideoCapture('C:\\Users\\koala\\skipping.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("C:\\Users\\koala\\frame1\\image_%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1