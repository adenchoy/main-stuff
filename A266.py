from matplotlib.pyplot import ylabel, plot, show, xlabel, title
import math
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [math.log(b) for b in x]
z = [b**2 for b in x]
a = [2**b for b in x]
c = [math.factorial(b) for b in x]
plot(x, c, 'b')
xlabel('Inputs')
ylabel('Steps')
title('Constant Complexity')
show()
