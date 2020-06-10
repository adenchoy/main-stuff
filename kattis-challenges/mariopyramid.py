baseletter = str(input("Letter?: "))
basesize = int(input("What size would you like your pyramid to be?: "))
if basesize%2 != 0:
    for i in range(0,int((basesize+1)/2)):
        print(' '*(int((basesize-1)/2)))
        print(baseletter)