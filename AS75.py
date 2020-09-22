denary = input("input denary number")
bcdlist =[]
for i in range(int(denary)):
    bcdlist.append(bin(int(denary[i+1])))
