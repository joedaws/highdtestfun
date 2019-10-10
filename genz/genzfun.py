#!/usr/bin/python3
"""
file: genzfun.py

Implementation of Genz functions

x is the input
|
----> is always of the size (N,d)
      where N is number of points and
      d is the dimension
"""


import numpy as np
import torch

def continuous(x,a=None,u=None):
    N = x.shape[0]
    d = x.shape[1]
    
    # numpy or torch?
    t = x.__class__
    
    if t == np.ndarray:
        if a == None:
            a = 5*np.ones(d)
        if u == None:
            u = 0.5*np.ones(d)
        # compute the genz function
        y = np.exp(-np.sum(np.multiply(a,np.abs(x-u)),axis=1).reshape((N,1)))
        
    elif t == torch.Tensor:
        if u == None:
            u = 0.5*torch.ones(1,d)
        if a == None:
            a = 5*torch.ones(1,d)
        y = torch.exp(-torch.sum(torch.mul(a,torch.abs(x-u)),dim=1).reshape((N,1)))

    return y

def corner_peak(x):
    return

def disccontinuous(x):
    return

def gaussian_peak(x):
    return

def osciallatory(x):
    return

def product_peak(x):
    return

if __name__ == "__main__":
    xn = np.random.uniform(-1,1,size=(10,6))
    xt = torch.tensor(xn,dtype=torch.float)

    print(continuous(xn))
    print(continuous(xt))

