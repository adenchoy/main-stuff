import random
import datetime
import string
def intgen():
    return random.randint(0,500)
letters_and_digits = string.ascii_letters + string.digits
def chargen():
    return random.choice(letters_and_digits)
def realgen():
    return random.uniform(0,500)
def boolgen():
    return bool(random.getrandbits(1))
def dategen():
    return datetime.date(random.randint(0,3000),random.randint(1,12),random.randint(1,31))
def stringgen():
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(random.randint(1,10))))
    return result_str
print(dategen())