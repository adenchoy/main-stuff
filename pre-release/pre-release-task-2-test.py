day = 0
time =  0
hourstay = 0
price = 0
check = ()
multipliers = [10,10,10,10,10,3,2]
maxstay = [2,2,2,2,2,4,8]
total = 0
pay = 0
def modcheck(freqcheck):
    if 11-((int(freqcheck[0])*5+int(freqcheck[1])*4+int(freqcheck[2])*3+int(freqcheck[3])*2)%11) == int(freqcheck[4]):
        check = 'y'
        return check
    else:
        check='n'
        return check
while True:
    while hourstay+time<24 and hourstay+time>=0:
        hourstay=0
        time=0
        while day > 7 or day < 1:
            day = int(input('what is the day? 1= monday 7=sunday'))
        while time < 7 or time > 24:
            time = int(input('what is the arrival time'))
        if time >15:
            while True:
                if hourstay + time <= 24 and hourstay>0:
                    break
                hourstay = int(input('how long are you intending to stay?(max until midnight)'))
        else:
            while True:
                if hourstay + time <= 24 and hourstay>0 and hourstay <= maxstay[day-1]:
                    break
                hourstay = int(input('how long are you intending to stay?'))
        if time<15:
            price = hourstay*multipliers[day-1]
        else:
            price = hourstay*2
        freq = input('Do you have a frequent parking number?')
        if freq in ['Yes','y','yes','Y']:
            freqcheck = input('Please input your frequent parking number.')
            check = modcheck(freqcheck)
        if check == 'y':
            if time<=15:
                price = price*0.9
                print(price)
            else:
                price = price*0.5
                print(price)
        else:
            print(price)
        while pay<=price:
            pay=float(input("please pay the price shown above."))
        total += pay
    print(total)
    total = 0
    if input("Would you like to end the program?") in ['y','Yes','Y','yes']:
        break
    else:
        continue