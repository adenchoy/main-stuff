import random
rand = []
for i in range(0,50):
    rand.append(random.randint(0,100))
print(rand)
print(sum(rand)/len(rand), max(rand), min(rand))