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


def create_img(data_pack = rule_of_thirds(), flip =False):
    
    name, spots_pack = data_pack
    
    if flip:
        print('flip')
        spots_pack = np.rot90(spots_pack)
        spots_pack = np.rot90(spots_pack)
    
    my_width, my_heigh, my_ratio = con.get_dim()
    
    data = np.zeros((my_heigh, my_width,3), dtype=np.uint8)+255
    
    data[np.where(spots_pack == 1)]  = [0,0,255]
    data[np.where(spots_pack == 2)]  = [0,255,0]
    data[np.where(spots_pack == 3)]  = [255,0,0]
    data[np.where(spots_pack > 3)]  = [200,200,150]
    
    img = Image.fromarray(data)
    
    img_name_path = f'{con.MASTER_DIR}{name}_{my_ratio[0]}_{my_ratio[1]}.png'
    
    img.convert('RGBA')
    img.save(img_name_path)
    img.show()
    
    # return spots_pack

    
def combine_rulez(rulez = [],flip =0):
    
    dims = rulez[0][1].shape
    
    for rule in rulez[1:]:
        assert dims == rule[1].shape

    line_spots = np.zeros(dims, dtype=np.uint8)
    
    for e, rule in enumerate(rulez):
        
        tmp_rule = rule[1]
        tmp_rule = tmp_rule[::-1]
        if flip:
            print('flip')
            tmp_rule = np.rot90(tmp_rule)
            tmp_rule = np.rot90(tmp_rule)
        
        line_spots += tmp_rule*(e+1)
        
    return 'comb', line_spots
    



def draw_rules_to_img(img_name = "P1430428.JPG"):
    
    # lol  without copy we get  WRITEABLE : False   - and could not acces the item
    ar_im = np.asarray(Image.open(img_name)).copy()
    
    
    # ar_im.flags #  to get flags of array
    
    temp_dims = ar_im.shape
    
    dims = con.get_dim(height=temp_dims[0], width=temp_dims[1])

    rules = [gr.phi_grid(dims),
            rule_of_thirds(dims),
            gr.golden_triangles(dims),
            gr.golden_boxes(dims),
           ]
    
    spots = combine_rulez(rules)
    
    ar_im[np.where(spots[1] > 0)]  = [255,255,102]
    
    
    
    img = Image.fromarray(ar_im)
    
    #img_name_path = f'{con.MASTER_DIR}{name}_{my_ratio[0]}_{my_ratio[1]}.png'
    
    img.convert('RGBA')
    #img.save(img_name_path)
    
    
    new_dims = con.get_dim(width=1000, ratio=dims[2])
    new_im = img.resize(new_dims[:2])
    new_im.show()


#
draw_rules_to_img()


'''
rules = [gr.phi_grid(),
        rule_of_thirds(),
        gr.golden_triangles(),
        gr.golden_boxes(),
       ]

'''

#spots = combine_rulez(rules)



#spots = gr.golden_boxes()
#create_img(spots)#, flip=True)









