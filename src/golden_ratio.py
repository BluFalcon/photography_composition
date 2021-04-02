#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 18:30:26 2021

@author: isiodos
"""

'''
some maths !!!

What golden ratio rule is ?

φ = 1.61803398875
the end :)

So...
For any a,b numbers then a/b = (a+b)/a =  φ

How to find φ if you only have a or b or (a+b)?
Easy !

A trick I personaly thought (add tears of happiness) and probably many others...

So the problem I needed to solve is that I have a+b as my image width dimension,
and I need a and b to draw the lines.

we know that
a/b =(a+b)/a 
we extend to  c/a = (c+a)/c where c = a+b

solving we get a^2 + a*c + c^2 = 0
where the c is known !!! is my width

so if c = 10
a = 6.18  --> 6

c = a+b = 10 = 6+b -> b =4


'''

# import complex math module
import constants as con
import numpy as np



def phi_grid(dims = con.get_dim()):
    
    my_width, my_heigh, my_ratio  = dims
    
    
    phi_width = con.solve_quadratic(1,my_width,-my_width**2)

    phi_height = con.solve_quadratic(1,my_heigh,-my_heigh**2)
    
    # init array 
    line_spots = np.zeros((my_heigh, my_width), dtype=np.uint8)
    
    # 1st vertical
    spot = int(phi_width)
    line_spots[:, spot-con.LINE_SIZE: spot+con.LINE_SIZE] = 1
    
    # 2nd vertical
    spot = int(my_width-phi_width)
    line_spots[:, spot-con.LINE_SIZE: spot+con.LINE_SIZE] = 1
    

    # 1st horizontal
    spot = int(phi_height)
    line_spots[spot-con.LINE_SIZE: spot+con.LINE_SIZE, :] = 1
    
    # 2nd horizontal
    spot = int(my_heigh-phi_height)
    line_spots[spot-con.LINE_SIZE: spot+con.LINE_SIZE: 1] = 1
    
    return 'phi_grid', line_spots
    
    