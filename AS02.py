def search(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return ('found in position',i)
    return 'not found'
arr = [i for i in input('').split()]
val = input('')
print(search(arr,val))