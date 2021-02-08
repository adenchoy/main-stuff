import random
temp = []
qArray = []
aArray =[]
ansArray = []
array =[]
score = 0
temparray = []
numofQs = int(input("How many questions do you want?:\n"))


with open("questionTEST.txt", "r") as whole_file:
    for line in whole_file:
        q = line.split(" : ")
        qArray.append(q[0])
        aArray.append(q[1].strip("\n"))
with open("answers.txt", "r") as file:
    for line in file:
        ansArray.append(line.strip('\n'))

for i in range(numofQs):
    qNum = random.randint(0,len(qArray)-1)
    print(qArray[qNum])
    temparray = ansArray[:]
    temp=ansArray.pop(qNum)
    array = random.sample(ansArray,3)
    if aArray[qNum] == 'A':
        array.insert(0,temp)
    elif aArray[qNum] == 'B':
        array.insert(1,temp)
    elif aArray[qNum] == 'C':
        array.insert(2,temp)
    elif aArray[qNum] == 'D':
        array.insert(3,temp)
    print(*array, sep=', ')
    answer = input("Input a,b,c, or d:\n")
    if answer == aArray[qNum]:
        print("Good job!\n+100!")
        score+=100
    else:
        print("Nice try, the correct answer was:\n",ansArray[qNum])
    ansArray = temparray[:]
with open("scores.txt","w") as file:
    file.write(str(score))

