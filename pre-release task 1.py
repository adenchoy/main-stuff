day = 5
time=  0
hourstay = 0
price=0
while True:
    day = int(input('what is the day? 1= monday 7=sunday'))
    if day >7 or day < 1:
        print('error')
    else:
        while True:
            time = int(input('what is the arrival time'))
            if time > 0 and time <24:
                break
    break
if day >=1 and day <=5:
    while True:
        hourstay = int(input('how long are you intending to stay?'))
        if hourstay + time <= 24:
            break
    if time>15:
        price= hourstay*10
    else:
        price =hourstay*2
print(price)
    
    