#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:52:39 2021

@author: isiodos
"""


from PIL import Image
import numpy as np

import constants as con
import golden_ratio as gr

def rule_of_thirds(dims = con.get_dim()):
    
    my_width, my_heigh, my_ratio  = dims
    
    # init array 
    line_spots = np.zeros((my_heigh, my_width), dtype=np.uint8)
    
    # 1st vertical
    spot = int(my_width/3)
    line_spots[:, spot-con.LINE_SIZE: spot+con.LINE_SIZE] = 1
    
    # 2nd vertical
    spot = int((2*my_width)/3)
    line_spots[:, spot-con.LINE_SIZE: spot+con.LINE_SIZE] = 1
    

    # 1st horizontal
    spot = int(my_heigh/3)
    line_spots[spot-con.LINE_SIZE: spot+con.LINE_SIZE, :] = 1
    
    # 2nd horizontal
    spot = int((2*my_heigh)/3)
    line_spots[spot-con.LINE_SIZE: spot+con.LINE_SIZE: 1] = 1
    
    return 'rule_of_thirds', line_spots


def create_img(data_pack = rule_of_thirds()):
    
    name, spots_pack = data_pack
    
    my_width, my_heigh, my_ratio = con.get_dim()
    
    data = np.zeros((my_heigh, my_width,3), dtype=np.uint8)+255
    
    data[np.where(spots_pack == 1)]  = [0,0,255]
    data[np.where(spots_pack == 2)]  = [0,255,0]
    data[np.where(spots_pack == 3)]  = [255,0,0]
    data[np.where(spots_pack == 4)]  = [0,0,0]
    
    img = Image.fromarray(data)
    
    img_name_path = f'{con.MASTER_DIR}{name}_{my_ratio[0]}_{my_ratio[1]}.png'
    
    img.convert('RGBA')
    img.save(img_name_path)
    #img.show()

    
def combine_rulez(rulez = []):
    
    my_width, my_heigh, my_ratio = con.get_dim()
    
    line_spots = np.zeros((my_heigh, my_width), dtype=np.uint8)
    
    for e, rule in enumerate(rulez):
        line_spots += rule[1]*(e+1)
        
    return line_spots
    
    

rules = [gr.phi_grid(),
         rule_of_thirds()]

spots = combine_rulez(rules)

create_img(('kati', spots))









