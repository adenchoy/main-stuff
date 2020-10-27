def search(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return 'not found'
arr = [i for i in input('').split()]
val = input('')
search(arr,val)