day = 0
time =  0
hourstay = 314134
price = 0
check = ()
multipliers = [10,10,10,10,10,3,2]
maxstay = [2,2,2,2,2,4,8]
add=0
def modcheck(freqcheck):
    if 11-((int(freqcheck[0])*5+int(freqcheck[1])*4+int(freqcheck[2])*3+int(freqcheck[3])*2)%11) == int(freqcheck[4]):
        check = 'y'
        return check
    else:
        check='n'
        return check
while True:
    day = int(input('what is the day? 1 = monday 7 = sunday'))
    if day <= 7 and day >= 1:
        break
    else:
        print('error')
while True:
    time = int(input('what is the arrival time'))
    if time > 7 and time <=24:
        break
    else:
        print('error')
if time >15:
    while True:
        if hourstay + time <= 24:
            break
        hourstay = int(input('how long are you intending to stay?(max until midnight)'))
else:
    while True:
        if hourstay + time <= 24 and hourstay <= maxstay[day-1]:
            break
        hourstay = int(input('how long are you intending to stay?'))
if time + hourstay>15:
    while add+time<=15 and add<hourstay:
        add+=1
    price=2+(add*multipliers[day-1])
if time+hourstay<15:
    price = hourstay*multipliers[day-1]
elif time>15:
    price =2
freq = input('Do you have a frequent parking number?')
if freq in ['Yes','y','yes','Y']:
    freqcheck = input('Please input your frequent parking number.')
    check = modcheck(freqcheck)
if check == 'y':
    if time<=15:
        price = price*0.9
        print(f'Your price is: {price}RM')
    else:
        price = price*0.5
        print(f'Your price is: {price}RM')
else:
    print(f'Your price is: {price}RM')