def Unknown(X,Y):
    if X == Y:
        return 1
    elif X < Y:
        print(X+Y)
        return Unknown(X+1,Y)*2
    elif X > Y:
        print(X+Y)
        return Unknown(X-1,Y)//2



def IterativeUnknown(X,Y):
    if X > Y:
        temp = X
        temp1 = Y
        while X !=Y:

            print(X+Y)
            X-=1
        return int(2**(temp1-temp))
    elif X<Y:
        temp = X
        temp1 = Y
        while X !=Y:
            
            print(X+Y)
            X+=1
        return int(2**(temp1-temp))
    else:
        return 1
print("Return value: 10, 15\n",IterativeUnknown(10,15))
print("Return value: 10, 10\n",IterativeUnknown(10,10))
print("Return value: 15, 10\n",IterativeUnknown(15,10))