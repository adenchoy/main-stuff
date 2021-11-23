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
