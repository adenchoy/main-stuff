
import numpy as np
n,k = input().split()
x = np.ones((int(n),int(k)))
x = np.zeros((int(n),int(k)),dtype=str)
x[x==''] = '.'
x[1::2,::2] = '*'
x[::2,1::2] = '*'
print(x)