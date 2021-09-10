import datetime


def timed_proc():
    while True:
        x = input("Write the lazy fox jumped over the brown dog:\n")
        if x == 'the lazy fox jumped over the brown dog':
            break
        else:
            print("You didn't write it properly. Try Again!")




start_time = datetime.datetime.now()
timed_proc()  
time_taken = datetime.datetime.now()-start_time  
print("It took you", time_taken, "to write the lazy fox jumped over the brown dog",)
