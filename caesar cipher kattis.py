N = []
Nres =[]
for i in range(10):
    N.append(int(input()))
    Nres.append(N[i]%42)

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return unique_list
print(len(unique(Nres)))
    