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

def corner_peak(x,a=None):
    N = x.shape[0]
    d = x.shape[1]
    
    # numpy or torch?
    t = x.__class__

    if t == np.ndarray:
        if a == None:
            a = 5*np.ones(d)
        
        # compute corner peak
        y = np.ones((N,1))
        for i in range(0,d):
            y += a[i]*x[:,i:i+1]

        y = np.power(y,-d-1)

    elif t ==  torch.Tensor:
        if a == None:
            a = 5*torch.ones(d)
        
        # compute the corner peak
        y = torch.ones(N,1)
        for i in range(0,d):
            y += a[i]*x[:,i:i+1]

        y = torch.pow(y,-d-1)

    return y 

def discontinuous(x,a=None,u=None):
    N = x.shape[0]
    d = x.shape[1]
    
    # numpy or torch?
    t = x.__class__

    if t == torch.Tensor:
        x = x.detach().numpy()

    if a == None:
        a = 5*np.ones(d)
    if u == None:
        u = 0.5*np.ones(d)
    
    # compute corner peak
    y = np.zeros((N,1))
    for i in range(0,d):
        y += a[i]*np.piecewise(x[:,i:i+1], [x[:,i:i+1] > u[i]],[1,0])

    print()
    y = np.exp(np.piecewise(y, [y > 0],[1,0]))

    if t == np.ndarray:
        return y

    elif t ==  torch.Tensor:
        y = torch.tensor(y,dtype=torch.float)
        return y
    else:
        raise TypeError 

def gaussian_peak(x):
    return

def oscillatory(x):
    return

def product_peak(x):
    return

if __name__ == "__main__":
    xn = np.random.uniform(-1,1,size=(10,6))
    xt = torch.tensor(xn,dtype=torch.float)
    
    # testing genz funs
    print("=<><><><><><><><><><><><>=")
    print("Testing:     fn continuous")
    print("=<><><><><><><><><><><><>=")
    print(continuous(xn))
    print(continuous(xt))
    print("OKAY\n")
    
    print("=<><><><><><><><><><><><>=")
    print("Testing:    fn corner_peak")
    print("=<><><><><><><><><><><><>=")
    print(corner_peak(xn))
    print(corner_peak(xt))
    print("OKAY\n")
    
    print("=<><><><><><><><><><><><>=")
    print("Testing:  fn discontinuous")
    print("=<><><><><><><><><><><><>=")
    print(discontinuous(xn))
    print(discontinuous(xt))
    print("OKAY\n")


