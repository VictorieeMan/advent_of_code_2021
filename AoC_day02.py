"""Advent of Code 2021 -- Day02"""
from AoC_2021 import *

print("Part One", "\n")
inputData = read_lines("AoC_day02_input.txt").split("\n")

#Starting position of the submarine
xPos = 0
yPos = 0 #Measuring depth

#Taking directions
for line in inputData:
    line = line.split()
    line[1] = int(line[1])

    if line[0] == "forward":
        xPos += line[1]
    elif line[0] == "down":
        yPos += line[1] #Increases depth
    elif line[0] == "up":
        yPos -= line[1] #Decrases depth
    else:
        print("Something wrong in taking directions...")

print(xPos, " ", yPos)
print(xPos*yPos)

print("\n\n","Part Two", "\n")

#Starting position of the submarine
xPos = 0
yPos = 0 #Measuring depth
aimP = 0

#Taking directions
for line in inputData:
    line = line.split()
    units = int(line[1])

    if line[0] == "forward":
        xPos += units
        yPos += aimP*units
    elif line[0] == "down":
        aimP += units
    elif line[0] == "up":
        aimP -= units
    else:
        print("Something wrong in taking directions...")

print(xPos, " ", yPos)
print(xPos*yPos)