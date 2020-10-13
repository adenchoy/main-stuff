NXY = input().split()
N = int(NXY[2])
X = int(NXY[0])
Y = int(NXY[1])



for i in range(1,int(N)+1):
    if i%Y == 0 and i%X == 0:
        print("FizzBuzz")
    elif i%Y == 0 and i%X !=0:
        print('Buzz')
    elif i%Y != 0 and i%X == 0:
        print('Fizz')
    else:
        print(i)