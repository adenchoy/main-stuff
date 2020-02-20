day = 0
time =  0
hourstay = 314134
price = 0
check = ()
multipliers = [10,10,10,10,10,3,2]
maxstay = [2,2,2,2,2,4,8]
def modcheck(freqcheck):
    if 11-((int(freqcheck[0])*5+int(freqcheck[1])*4+int(freqcheck[2])*3+int(freqcheck[3])*2)%11) == int(freqcheck[4]):
        return True
    else:
        return False
while day > 7 or day < 1:
    day = int(input('what is the day? 1= monday 7=sunday: \n'))
while time < 7 or time > 24:
    time = int(input('what is the arrival time: \n'))
if time >15:
    while True:
        if hourstay + time <= 24:
            break
        hourstay = int(input('how long are you intending to stay?(max until midnight)\nHow long in hours?: '))
else:
    while True:
        if hourstay + time <= 24 and hourstay <= maxstay[day-1]:
            break
        hourstay = int(input('how long are you intending to stay?\nHow long in hours?: '))
if time<=15:
    price = hourstay*multipliers[day-1]
elif time>15:
    price= 2
freq = input('Do you have a frequent parking number?(Y/N)')
if freq.upper()==('Y'):
    freqcheck = input('Please input your frequent parking number.\nPlease enter: ')
    while True:
        if modcheck(freqcheck):
            if time<=15:
                price = price*0.9
                print(f'Your price is: {price}RM')
                break
            else:
                price = price*0.5
                print(f'Your price is: {price}RM')
                break
        else:
            if input('Number invalid, discount not applied.\nWould you like to retry? Y/N').upper == 'Y':
                continue
            else:
                break

if freq.upper()==('N'):
    print('Discount will not be applied, please apply for a frequent parking account for up to a 50percent discount!')
    print(f'Your price is: {round(price,2)}RM')
