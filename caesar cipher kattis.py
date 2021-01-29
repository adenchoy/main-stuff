import random
temp = []
numofQs = int(input("How many questions do you want?:\n"))


with open("questionTEST.txt", "r") as whole_file:
    for question in whole_file:
        temp = [question.split(" : ")]
        qArray = [x for x in temp[0::2]]
        aArray = [y for y in temp[1::2]]