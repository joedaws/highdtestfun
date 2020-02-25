#!/usr/bin/python3
"""
file: gfunction.py

ONLY WORKS WITH TORCH TENSORS AT THE MOMENT

Implementation of g function

see https://www.sfu.ca/~ssurjano/gfunc.html

x is the input
|
----> is always of the size (N,d)
      where N is number of points and
      d is the dimension
"""

import torch

def init_a(d):
    """
    construct initial values of a
    where a is parameter of g-function
    """
    # initialize list 
    a = [0]*d
    
    for i in range(d):
        a[i] = (i+1 -2)/2

    return a

def g_function(x):
    """
    evaluate the g-function
    """
    # get dimension of points
    d = x.shape[1]

    # get parameters a
    a = init_a(d)

    # evaluate the function
    val = 1
    for i in range(d):
        val *= (torch.abs(4*x[:,i:i+1]-2) + a[i])/(1+a[i])

    return val

    
