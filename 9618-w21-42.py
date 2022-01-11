def Unknown(X,Y):
    if X == Y:
        return 1
    elif X < Y:
        print(X+Y)
        return Unknown(X+1,Y)*2
    elif X > Y:
        print(X+Y)
        return Unknown(X-1,Y)//2

print("Call 1: 10, 15\n",Unknown(10,15))
print("Call 2: 10, 10\n",Unknown(10,10))
print("Call 3: 15, 10\n",Unknown(15,10))