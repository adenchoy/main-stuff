
count = 1
counter = 0
for x in range(int(input())):
    a = [int(d) for d in input().split()]
    if a[2] == 1:
        print("YES")
    elif a[0]%2 != 0 and a[1]%2 !=0:
        print("NO") 
    else:
        n = int()
        while True:
            if a[0]%2 == 0:
                a[0]/= 2
                count+=1
            elif a[1]%2 == 0:
                a[1]/= 2
                count +=1
            if count >= a[2]-1:
                print("YES")
                break
            elif counter > a[2]:
                print("NO")
                break
            counter+=1