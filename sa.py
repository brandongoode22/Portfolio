#!/usr/bin/env python3

import SumofGaussians as SG
import sys
import numpy as np
from math import e


seed = int(sys.argv[1])
D = int(sys.argv[2])
N = int(sys.argv[3])


np.random.seed(seed)

sog = SG.SumofGaussians(D,N)


epsilon = 1e-8
T = 1e-40
delta_T = 1e-45
X = np.empty((0, D))

for i in range(D):
    X = np.append(X, 10.0*np.random.ranf())
    
gX = sog.Eval(X)

unchanged = 0
for j in range(10000):
    cur_gX = 0
    gX = sog.Eval(X)
    cur_gX = gX
    for i in range(D):
        temp = np.copy(X)

        Y = temp[i] + np.random.uniform(-0.1, 0.1)
        
        if(Y > 0 and Y < 10):
            np.put(temp, i, Y)
            gY = sog.Eval(temp)
        
            
           
            if gY > gX:
                unchanged = 0
                X = np.copy(temp)
                cur_gX = gY
            elif np.random.ranf() <= e**((gY - gX)/T):
                unchanged = 0
                X = np.copy(temp)
                cur_gX = gY
            else:
                unchanged += 1
       
    T = T - delta_T
    print(' '.join(map(str,X)), cur_gX)
    if unchanged > 100:
        break

       