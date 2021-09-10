import matplotlib.pyplot as plt
import math
x = [x for x in range(1,31)]
print(x)
y = [math.log(b) for b in x]
z = [b**2 for b in x]
a = [2**b for b in x]
c = [math.factorial(b) for b in x]
figure, axis = plt.subplots(2, 2)
axis[0, 0].plot(x, y)
axis[0, 0].set_title("Logarithmic Growth")
axis[0, 1].plot(x, z)
axis[0, 1].set_title("Quadratic Growth")
axis[1, 0].plot(x, a)
axis[1, 0].set_title("Exponential Growth")
axis[1, 1].plot(x, c)
axis[1, 1].set_title("Factorial Growth")
plt.show()
