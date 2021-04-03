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
import math


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



'''
about drawing diagonials

https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm

use this

plotLineLow(x0, y0, x1, y1)
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0
        yi = -1
        dy = -dy
    end if
    D = (2 * dy) - dx
    y = y0

    for x from x0 to x1
        plot(x, y)
        if D > 0
            y = y + yi
            D = D + (2 * (dy - dx))
        else
            D = D + 2*dy
        end if

'''


def create_digonial_simple(x0, y0, x1, y1, line_spots):
    
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
        
    D = (2 * dy) - dx
    y = y0


    for x in range(x0, x1):

        try:
            line_spots[y,x] = 1
        except:
            break
        
        if D > 0:
            y = y + yi
            D = D + (2 * (dy - dx))
        else:
            D = D + 2*dy
    
    return line_spots


def create_digonial(x0, y0, x1, y1, line_spots):
    """
    https://github.com/encukou/bresenham/blob/master/bresenham.py
    
    Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    """
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        
        try:
            line_spots[ y0 + x*xy + y*yy, x0 + x*xx + y*yx,] = 1
        except:
            pass
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
        
    return line_spots
        
def phi_triangles(dims = con.get_dim()):
    
    my_width, my_heigh, my_ratio  = dims
    
    # init array 
    line_spots = np.zeros((my_heigh, my_width), dtype=np.uint8)
    
    # find diagonial spots for triangle
    p_w = int(my_width/3)
    p_h = int(my_heigh/3)
    
    
    #auto 8a ginei func ?
    
    # 1st diagonial # create_digonial(x0, y0, x1, y1, line_spots):
    line_spots = create_digonial(0, 0, my_width, my_heigh, line_spots)

    print(p_w)
    print(p_h)
    # triangle in left from line to up right corner
    line_spots  = create_digonial(p_w, p_h, 0, my_heigh, line_spots)

    # triangle in left from line to  down left corner
    line_spots  = create_digonial(2*p_w, 2*p_h, my_width, 0, line_spots)
    
    return 'trigwna', line_spots


