import pickle
with open("practical.txt","r") as file:
    with open("changedpractical.txt","w") as newfile:
        delim = ""
        for line in file:
            
            if line[0:4] == "19.1":
                delim = "19.1"
            elif line[0:4] == "19.2":
                delim = "19.2"
            elif line[0:4] == "20.1":
                delim = "20.1"  
            elif line[0:4] == "20.2":
                delim = "20.2"
            data = delim+" "+line
            newfile.write(data)
class Point:
    def __init__(self,line,top):
        self.SylPoint = line
        self.Finished = False
        self.Topic = top
list= []

with open("changedpractical.txt","r") as f:
    for line in f:
            list.append(Point(line[4::],line[0:4]))
with open("191.pickle","wb") as y:
    for i in list:
        pickle.dump(i,y)
with open("191.pickle","rb") as z:
    for i in range(len(list)):
        test = pickle.load(z)
        print(test.Topic)
