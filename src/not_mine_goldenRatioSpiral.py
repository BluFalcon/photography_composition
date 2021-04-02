#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:18:00 2021

@author: isiodos
"""

# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


def fibonachi_nums():
    # Program to display the Fibonacci sequence up to n-th term
    
    nterms = int(input("How many terms? "))
    
    # first two terms
    n1, n2 = 0, 1
    suma = 0
    count = 0
    
    # check if the number of terms is valid
    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           suma += n1
           print(f'{n1} {suma} {n1**2}')
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1


def fiboPlot(n):
	a = 0
	b = 1
	square_a = a
	square_b = b

	x = turtle.Turtle()
	x.speed(10)
    
	# Setting the colour of the plotting pen to blue
	x.pencolor("blue")

	# Drawing the first square
	x.forward(b * factor)
	x.left(90)
	x.forward(b * factor)
	x.left(90)
	x.forward(b * factor)
	x.left(90)
	x.forward(b * factor)

	# Proceeding in the Fibonacci Series
	temp = square_b
	square_b = square_b + square_a
	square_a = temp
    
	# Drawing the rest of the squares
	for i in range(1, n):
		x.backward(square_a * factor)
		x.right(90)
		x.forward(square_b * factor)
		x.left(90)
		x.forward(square_b * factor)
		x.left(90)
		x.forward(square_b * factor)

		# Proceeding in the Fibonacci Series
		temp = square_b
		square_b = square_b + square_a
		square_a = temp

	# Bringing the pen to starting point of the spiral plot
	x.penup()
	x.setposition(factor, 0)
	x.seth(0)
	x.pendown()

	# Setting the colour of the plotting pen to red
	x.pencolor("red")
    

	# Fibonacci Spiral Plot
	x.left(90)
	for i in range(n):
		print(b)
		fdwd = math.pi * b * factor / 2
		fdwd /= 90
		for j in range(90):
			x.forward(fdwd)
			x.left(1)
		temp = a
		a = b
		b = temp + b
    
	turtle.done()


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1

# Taking Input for the number of
# Iterations our Algorithm will run
n = int(input('Enter the number of iterations (must be > 1): '))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if n > 0:
	print("Fibonacci series for", n, "elements :")
	fiboPlot(n)
else:
	print("Number of iterations must be > 0")



