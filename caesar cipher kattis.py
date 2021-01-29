import random
temp = []
qArray = []
aArray =[]
numofQs = int(input("How many questions do you want?:\n"))


with open("questionTEST.txt", "r") as whole_file:
    for line in whole_file:
        q = line.split(" : ")
        print(q)
        
