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
    def __init__(self,line) -> None:
        self.SylPoint = line
        self.Finished = False
list= []
with open("changedpractical.txt","r") as f:
    for line in f:
        if line[0:4] == "19.1":
            list.append(str(line[4::].strip()))
            
with open("191.pickle","wb") as y:
    for i in list:
        pickle.dump(Point(i),y)
with open("191.pickle","rb") as z:
    for i in range(19):
        test = pickle.load(z)
        test.Finished = True
        print(test.Finished)
def updateTracker19():
    with open("191.pickle","rb") as z:
        for i in range(19):
          m= pickle.load(z)
          x = input("Have you finished",m,"?")
          if m == "yes":
              m.Finished = True
          pickle.dump(m,z)

updateTracker19()