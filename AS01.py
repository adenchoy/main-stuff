
def bubbleSort(arr): 
    l = len(arr) 
    i = 0
    while i < l:
        j=0
        while j<l-1:
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j+=1
        i+=1
    return arr

print(bubbleSort([64, 34, 25, 12, 22, 11, 90] ))