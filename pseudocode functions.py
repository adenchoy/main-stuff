""" Making Pseudocode real. Create the Pseudocode in Python.
By the way this is NOT a nice way to name your definitions in Python, but it 
lets you get away with it.
pass lets me not code up the function. It's like on a quiz show.
"""

def LEFT(string,length):   
    # returns the left most characters of a string. 
    # I've done this one as an example.
    return string[0:length]

def RIGHT(string,length):
    return string[-length::]
print(RIGHT('aden',3))


def MID (string,start,end):
    return string[start-1:end-1]
    
    
def LENGTH (string):
    return(len(string))


def LCASE (string):
    newstring = ''
    for i in string:
        if i.islower():
            newstring+=i
    return newstring
    
def UCASE(string):
    newstring = ''
    for i in string:
        if i.isupper():
            newstring+=i
    return newstring
def TO_UPPER(string):
    return string.upper()

def TO_LOWER(string):
    return string.lower()
 
def NUM_TO_STRING(num):
    return str(num)

def STRING_TO_NUM(string):
    return int(string)

def INT(num):
    return int(num)

def ASC(char):
    return ascii(char)

# example function being called    
my_string = LEFT("hello",2)
print(my_string)

print('1, left')
print('2, right')
print('3, mid')
print('4, length')
print('5, lcase')
print('6, ucase')
print('7, to upper')
print('8, to lower')
print('9, num to string')
print('10, string to num')
print('11, int')
print('12, asc')

x,y,z,a = input('input which function you would like and which parameters would you like to pass through (num, param1, param2, param3) input 0s if param not needed').split()
if x == 1:
    print(LEFT(string(y),z))
elif x == 2:
    print(RIGHT(y,z))
elif x == 3:
    print(MID(y,z,a))
elif x == 4:
    print(LENGTH(y))
elif x == 5:
    print(LCASE(y))
elif x == 6:
    print(UCASE(y))
elif x == 7:
    print(TO_UPPER(y))
elif x == 8:
    print(TO_LOWER(y))
elif x == 9:
    print(NUM_TO_STRING(y))
elif x == 10:
    print(STRING_TO_NUM(y))
elif x == 11:
    print(INT(y))
elif x == 12:
    print(ASC(y))