# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 05:59:56 2020

@author: deepa
"Math Adventures with Python" Peter Farrel
"""
from math import sqrt
#range of x-values
global xmin,xmax,ymin,ymax,rangex,rangey
xmin=-2
xmax=2
#range of y values
ymin=-2
ymax=2

#calculate the range
rangex=xmax-xmin
rangey=ymax-ymin


def setup():
    global xdcl,yscl
    size(600,600)
    noStroke()
    xscl=float(rangex)/width
    yscl=float(rangey)/height
    
    
    
def magnitude(z):
    return int((sqrt(z[0]**2+z[1]**2)))
def cAdd(a,b):
    """Adds two complex numbers"""
    return [a[0]+b[0],a[1]+b[1]]
def cMult(u,v):
    """Returns the product of two complex numbers"""
    return[u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]
def draw():
    
    
    #origin in center
    translate(width/2,height/2);
    #translate() is a method which moves the grid itself
    #go over all x's and y's on the grid
    for x in range(width):
        for y in range(height):
            x=[(xmin+x*xscl),(ymin+y*yscl)]
            #put it into the madelbroth funtiion
            col=mandelbrot(z,100)
            #if mandelbrot returns 0
            if col==100:
                fill(0) 
                #make the rectangle black
            else:
                fill(255) #make the rectangle white
                #draw a tiny rectangle
                rect(x,y,1,1)
def mandelbrot(z,num):
    """runs the process num times"""
    """and returns the diverge count"""
    count=0
    #define z1 as z
    z1=z
    #iterate num times
    while count<=num:
        #check for divergence
        if magnitude(z1)>2.0:
            #return the step it diverged on
            return count
        #iterate z
        z1=cAdd(cMult(z1,z1),z)
        count+=1
        # if z hasnt diverged by the end
        return num
    
mandelbrot(1,10)
                

