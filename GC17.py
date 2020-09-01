freqcheck = input('')
if 11-((int(freqcheck[0])*10+int(freqcheck[1])*9+int(freqcheck[2])*8+int(freqcheck[3])*7+int(freqcheck[4])*6+int(freqcheck[5])*5+int(freqcheck[6])*4+int(freqcheck[7])*3+int(freqcheck[8])*2)%11) == int(freqcheck[9]):
    check = 'y'
print(check)