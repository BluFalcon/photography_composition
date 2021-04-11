#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:10:03 2021

@author: isiodos

no clue what worked in the end...
pip install opencv-python
sudo apt-get install python3-opencv
https://pypi.org/project/opencv-python/
"""

import golden_ratio as gr
import compositions
import constants
import numpy as np
import cv2


# open device 
n=0

while(n<5):

    print(n)
    try:
        cap = cv2.VideoCapture(n)
        ret, frame = cap.read()
        temp_dims = frame.shape
        break
    except:             
        cap.release()
        cv2.destroyAllWindows()

        # go to the next device
        n += 1


'''
for now found n manual :) 
'''

# get a frame
ret, frame = cap.read()
temp_dims = frame.shape

dims = constants.get_dim(height=temp_dims[0], width=temp_dims[1])


#  create lines
rules = [#gr.phi_grid(dims),
        #compositions.rule_of_thirds(dims),
        #gr.golden_triangles(dims),
        gr.golden_boxes(dims),
        ]



# combine them to one array
spots = compositions.combine_rulez(rules)



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    
    frame[np.where(spots[1] > 0)]  = [255,255,102]
    
    '''
    
    frame[np.where(spots[1] == 1)]  = [0,0,255]
    frame[np.where(spots[1] == 2)]  = [0,0,255]
    frame[np.where(spots[1] == 3)]  = [0,0,255]
    frame[np.where(spots[1] == 4)]  = [0,0,255]
    '''
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2XYZ)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

