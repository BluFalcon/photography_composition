#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:52:39 2021

@author: isiodos
"""


from PIL import Image
import numpy as np
'''

w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()


# rules: name format directions ?
rules = {'of thrirds': 1}
'''

LN_SZ = 1
DEFAULT_WIDTH = 100
DEFAULT_RATIO = [4, 3]

MASTER_DIR = '../pictures/'



def get_dim(width=DEFAULT_WIDTH, ratio=DEFAULT_RATIO):

    # default 
    my_width = width
    my_ratio = ratio[0]/ratio[1]
    
    my_heigh = int(my_width/my_ratio)
    
    return my_width, my_heigh, ratio


def rule_of_thirds():
    
    my_width, my_heigh, my_ratio = get_dim()
    
    # init array 
    
    line_spots = np.zeros((my_heigh, my_width), dtype=np.uint8)
    
    # 1st vertical
    spot = int(my_width/3)
    line_spots[:, spot-LN_SZ: spot+LN_SZ] = 1
    
    # 2nd vertical
    spot = int((2*my_width)/3)
    line_spots[:, spot-LN_SZ: spot+LN_SZ] = 1
    

    # 1st horizontal
    spot = int(my_heigh/3)
    line_spots[spot-LN_SZ: spot+LN_SZ, :] = 1
    
    # 2nd horizontal
    spot = int((2*my_heigh)/3)
    line_spots[spot-LN_SZ: spot+LN_SZ: 1] = 1
    
    
    return line_spots

def create_img(name = 'rule_of_thirds', spots_pack=rule_of_thirds()):
    
    my_width, my_heigh, my_ratio = get_dim()
    
    data = np.zeros((my_heigh, my_width,3), dtype=np.uint8)+255
    
    data[np.where(spots_pack == 1)]  = [0,0,0]
    
    img = Image.fromarray(data)
    
    img_name_path = f'{MASTER_DIR}{name}_{my_ratio[0]}_{my_ratio[1]}.png'
    
    img.save(img_name_path)
    #img.show()

    



create_img()












