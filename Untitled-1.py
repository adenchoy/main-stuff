
import datetime
def sort(nlist):
    done = False
    while not done:
        done = True
        for i in range(len(nlist)-1):
            if nlist[i] > nlist[i+1]:
                done = False
                nlist[i]=nlist[i+1]
#            print(nlist) #Fun to see how much print statements slow it down
    return nlist

start_time = datetime.datetime.now()
nlist = sort([4,1,7,3,9,4,2,6,7])
print(datetime.datetime.now()-start_time)
print(nlist)