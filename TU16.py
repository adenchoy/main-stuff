money = 129.00
print(f"RM{money}")


numcol1 = [5, 10, 15]
numcol2 = [3,6,9]
numcol3 = [2,4,8]

print("\n Multiples of 5    Multiples of 3    Multiples of 2")
for i in range(3):
    print(f" {numcol1[i]:<15} {numcol2[i]:<15} {numcol3[i]:<15}")

number = int(input("what number would you like to convert"))
print(f"Binary: {number:b}\nHexadecimal: {number:x}\nDecimal: {number:d}")