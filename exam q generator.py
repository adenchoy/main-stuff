number = -5
while True:
    for i in range(0,3):
        while number < 0:
            number = input("input a number >0")
        if number >10: 
            print("bigger than 10")
        elif number <10:
            print('less than 10')
        elif number == 10:
            print('equals 10')
    if number >15:
        print('number is bigger than 15')
    b   reak
    