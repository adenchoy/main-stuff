day = 0
time =  0
hourstay = 314134
price = 0
check = ()
multipliers = [10,10,10,10,10,3,2]
maxstay = [2,2,2,2,2,4,8]
def modcheck(freqcheck):
    if 11-((int(freqcheck[0])*5+int(freqcheck[1])*4+int(freqcheck[2])*3+int(freqcheck[3])*2)%11) == int(freqcheck[4]):
        check = 'y'
    return check
while day > 7 or day < 1:
    day = int(input('what is the day? 1= monday 7=sunday'))
while time < 7 or time > 24:
    time = int(input('what is the arrival time'))
while True:
    if hourstay + time < 24 and hourstay <= maxstay[day-1]:
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