# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:59:11 2022

@author: Meghanad Kayanattil
"""
import numpy as np
from math import dist
from scipy.interpolate import interp1d

def revolve(x, y, axis_loc = 'right', interpolation = True):
    """
    Produces 3D surface of revolution about an axis
    
    Input: x, y(float): cordinates of your intended 2d plot / function
           axis_loc(string): default - 'right', you can also provide 'left','up' and 'down'
           interpolation(bool): default - True; a simple linear interpolation is done on the
           data to increase the number of points by 5x
    
    """
    
    if interpolation == True:
        x, y = interpolation_fun(x,y)
    
    if axis_loc == 'right':
        x_ax = np.max(x)*np.ones(len(x))
        y_ax = y
        xout, yout, zout = plot_to_surf_along_y(x,y,x_ax,y_ax)
        return xout, yout, zout
    elif axis_loc == 'left':
        x_ax = np.min(x)*np.ones(len(x))
        y_ax = y
        xout, yout, zout = plot_to_surf_along_y(x,y,x_ax,y_ax)
        return xout, yout, zout
    elif axis_loc == 'down':
        x_ax =  x
        y_ax = np.min(y)*np.ones(len(y))
        xout, yout, zout = plot_to_surf_along_x(x,y,x_ax,y_ax)
        return xout, yout, zout
    elif axis_loc == 'up':
        x_ax =  x
        y_ax = np.max(y)*np.ones(len(y))
        xout, yout, zout = plot_to_surf_along_x(x,y,x_ax,y_ax)
        return xout, yout, zout
        
    
    

def interpolation_fun(x, y):
    
    n = 5*len(x)
    
    if mono_increase(x) == True:
        inter = interp1d(x, y, kind = 'linear')
        xnew = np.linspace(x[0], x[-1], n)
        ynew = inter(xnew)
        return xnew, ynew
    elif mono_increase(y) == True:
        inter = interp1d(y, x, kind = 'linear')
        ynew = np.linspace(y[0], y[-1], n)
        xnew = inter(ynew)
        return xnew, ynew
    else:
        raise ValueError('The interpolation function needs monotonically increasing values')
           
def mono_increase(x):   
     n = len(x)
    
     if all(x[i]<x[i+1] for i in range(0,n-1)):
         return True
     else:
         return False       
    
    
def plot_to_surf_along_y(x, y, x_ax, y_ax):
    """
    Produces a surface of revolution along y axis
    
    """
    
    n = len(x)
    
    angle = np.linspace(0, 2 * np.pi, n) 
    
    theta, zout = np.meshgrid(angle, y_ax)
    
    
    x_circ = np.zeros([n,n])
    y_circ = np.zeros([n,n])
    
    i=0
    for xi, yi, xl, yl in zip(x, y, x_ax, y_ax):
        p1 = [xi,yi]
        p2 = [xl, yl]
        
        r = dist(p1, p2)

        x_circ[i] = r* np.cos(angle)
        y_circ[i] = r* np.sin(angle)
        i+=1
        
    return x_circ, y_circ, zout


def plot_to_surf_along_x(x, y, x_ax, y_ax):
    """
    Produces a surface of revolution along x axis
    
    """
    
    n = len(x)
    
    angle = np.linspace(0, 2 * np.pi, n) 
    
    theta, xout = np.meshgrid(angle, x_ax)
    
    
    y_circ = np.zeros([n,n])
    z_circ = np.zeros([n,n])
    
    i=0
    for xi, yi, xl, yl in zip(x, y, x_ax, y_ax):
        p1 = [xi,yi]
        p2 = [xl, yl]
        
        r = dist(p1, p2)

        y_circ[i] = r* np.cos(angle)
        z_circ[i] = r* np.sin(angle)
        i+=1
        
    return xout, y_circ, z_circ