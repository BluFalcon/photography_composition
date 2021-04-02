#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:27:38 2021

@author: isiodos
"""


import math
# import nupmy as np


LINE_SIZE = 1
DEFAULT_WIDTH = 1000
DEFAULT_RATIO = [16, 9]

MASTER_DIR = '../pictures/'



def get_dim(width=DEFAULT_WIDTH, ratio=DEFAULT_RATIO):

    # default 
    my_width = width
    my_ratio = ratio[0]/ratio[1]
    
    my_heigh = int(my_width/my_ratio)
    
    return my_width, my_heigh, ratio



def solve_quadratic(a,b,c):    
    # Solve the quadratic equation ax**2 + bx + c = 0
    '''
    a = 1
    b = 10
    c = -100
    '''
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    
    # find two solutions
    sol_1 = (-b-math.sqrt(d))/(2*a)
    sol_2 = (-b+math.sqrt(d))/(2*a)
    
    print(f'The solution are {sol_1} and {sol_2}')
    
    if sol_1 > 0 > sol_2:
        return int(sol_1)
    
    if sol_2 > 0 > sol_1:
        return int(sol_2)
    
    raise ValueError
    # return 'error'