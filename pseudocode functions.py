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