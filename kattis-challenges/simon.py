
# The text file TreasureChestData.txt stores data for five questions, in the order of
# question, answer, points.
# For example, the first three lines of the file are for the first question:
# 2*2 question
# 4 answer
# 10 points
# Write program code for the procedure, readData() to:
# • read each question, answer and points from the text file
# • create an object of type TreasureChest for each question
# • declare an array named arrayTreasure of type TreasureChest
# • append each object to the array
# • use exception handling to output an appropriate message if the file is not found.
f = open("TreasureChestData.txt", "r")
line_count = 0
for line in f:
    if line != "\n":
        line_count += 1
print(f.readline())
print(line_count)
