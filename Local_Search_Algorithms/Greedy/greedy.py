#!/usr/bin/env python3

import SumofGaussians as SG
import sys
import numpy as np


seed = int(sys.argv[1])
D = int(sys.argv[2])
N = int(sys.argv[3])


np.random.seed(seed)

sog = SG.SumofGaussians(D,N)


epsilon = 1e-8

X = np.empty((0, D))

for i in range(D):
    X = np.append(X, 10.0*np.random.ranf())
    
for i in range(D):
    print(X[i], end=' ')
gX = sog.Eval(X)
print(gX)



count = 0

while True:
    gX = sog.Eval(X)
    cur_gX = gX
    for i in range(D):
        der = sog.Deriv(X)
        temp_first = np.copy(X)
        temp_second = np.copy(X)

        first = X[i] + 0.01 * der[i]
        second = X[i] - 0.01 * der[i]
    

        np.put(temp_first, i, first)
        first_gX = sog.Eval(temp_first)

        np.put(temp_second, i, second)
        second_gX = sog.Eval(temp_second)

        if first_gX > gX and first_gX >= second_gX:
            X = np.copy(temp_first)
            cur_gX = first_gX
                  
        elif second_gX > gX and second_gX > first_gX:
            X = np.copy(temp_second)
            cur_gX = second_gX
    
    count += 1
    print(' '.join(map(str,X)), cur_gX)
    if count >= 10000 or abs(gX - cur_gX) < epsilon:
        break
