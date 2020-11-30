with open("if.txt",'r') as rudyard:
    totalrud=0
    for line in rudyard:
        if "if" in line.lower():
            totalrud +=1

print(totalrud)
with open("mam.txt",'r') as mam:
    totalmam = 0
    for line in mam:
        if "if" in line.lower():
            totalmam += 1

print(totalmam)
if totalmam > totalrud:
    with open('mam.txt','a') as mam:
        mam.write(f'{totalmam}')
else:
    with open('if.txt','a') as rud:
        rud.write(f'\n{totalrud}')
