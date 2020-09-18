#Create a program that will be able to crack a piece 
#of code when given the ciphertext and the shift. 
#It must also be able to then encrypt messages as well. 
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def decode(plain,shift):
    decoded = ""
    text = plain.lower()
    for lettersintext in text:
        if lettersintext == " ":
            decoded+=" "
        else:
            for i in range(len(letter)):
                if letter[i] == lettersintext:
                    decoded += letter[i-shift]
                    break
    return decoded
    
print(decode(str(input("input encoded text: ")),int(input("input shift number: "))))

def encode(plain,shift):
    cipher = ""
    text1 = plain.lower()
    for lettersintext in text1:
        if lettersintext == " ":
            cipher+=" "
        else:
            for i in range(len(letter)):
                if letter[i] == lettersintext:
                    cipher += letter[i+shift]
                    break
    return cipher
    
print(encode(str(input("input text: ")),int(input("input shift number: "))))
    