n=int(input())
for i in range(n):
    test = input()
    if test[0:10] == "simon says":
        print(test[11::])
    else:
        print(' ')