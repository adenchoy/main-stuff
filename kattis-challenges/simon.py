n=int(input())
for i in range(n):
    test = input()
    simon = test[0:10]
    if simon.lower() == "simon says":
        print(test[11::])
    else:
        print(' ')