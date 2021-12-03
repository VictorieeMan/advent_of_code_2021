"""Advent of Code 2021 -- Day03"""
from AoC_2021 import *

print("Part One", "\n")
inputData = read_lines("AoC_day03_input.txt").split("\n")

#Rate parameters
gamRate = 0
epsRate = 0

# Structuring the data into a matrix
dataMatrix = []
for line in inputData:
    lineVector = [char for char in line]
    lineVector = [int(i) for i in lineVector]
    dataMatrix.append(lineVector)

#Transposing the data
dataMatrixT = map(list,zip(*dataMatrix))
columnMode = []
columnAvg = []

#Calculating the mode value of each column
for vector in dataMatrixT:
    a = avgArithm(vector)
    b = round(a)
    print(b,a)
    columnAvg.append(a)
    columnMode.append(b)

def funcColumnMode(inputMatrix=[], setting = 1):
#Calculating the mode value of each column
    columnMode = []
    columnAvg = []
    for vector in inputMatrix:
        a = avgArithm(vector)
        if a == 0.5:
            b = 1
        else:
            b = round(a)
        #print(b,a)
        columnAvg.append(a)
        columnMode.append(b)

        print(columnMode, columnAvg)
    
    if setting == 0:
        output = columnAvg
    else:
        output = columnMode

    return output

print(columnMode)

#Converts bin to dec
powerIt = 0
for i in reversed(columnMode):
    gamRate += i*pow(2,powerIt)
    powerIt += 1

powerIt = 0
for i in reversed(columnMode):
    i = (i+1) % 2
    epsRate += i*pow(2,powerIt)
    powerIt += 1

print(gamRate, epsRate)
print(gamRate*epsRate)

print("Part Two", "\n")

#Rate parameters
oxyRate = 0
co2Rate = 0

#Searching for OxyRate
tempData = dataMatrix

colNr = 0
while(True):
    rowNr = 0
    keepRow = []
    unwanted = []
    tempColAvg = funcColumnMode(matrixTranspose(tempData))

    for row in tempData:
        if row[colNr] == tempColAvg[colNr]:
            keepRow.append(rowNr)
        rowNr += 1
    colNr += 1
    
    keepers = []
    for index in keepRow:
        keepers.append(tempData[index])
    
    tempData = keepers
    print(len(tempData))
    print(tempData)
    if len(tempData) == 1:
        break

oxyRate = binListToDecInt(tempData[0])
print(oxyRate)

#Searchgin for co2Rate
tempData = dataMatrix

colNr = 0
while(True):
    rowNr = 0
    keepRow = []
    unwanted = []
    tempColAvg = funcColumnMode(matrixTranspose(tempData))

    for row in tempData:
        if row[colNr] != tempColAvg[colNr]:
            keepRow.append(rowNr)
        rowNr += 1
    colNr += 1
    
    keepers = []
    for index in keepRow:
        keepers.append(tempData[index])
    
    tempData = keepers
    print(len(tempData))
    print(tempData)
    if len(tempData) == 1:
        break

co2Rate = binListToDecInt(tempData[0])
print(co2Rate)

print(oxyRate,co2Rate)
print(oxyRate*co2Rate)

"""Previous Attempt"""
"""
#Rating the rows after commonness
rowRating = zeroVector(len(dataMatrix))
lostRounds = listVector(len(dataMatrix))
rowNr = 0
for row in dataMatrix:
    rowRate = 0
    for i in range(0,len(columnMode)):
        if row[i] == columnMode[i]:
            rowRate += 1
        else:
            lostRounds[rowNr].append(i)
        rowRating[rowNr] += rowRate
    rowNr += 1

# Find index of max() and min()
maxRowRating = max(rowRating)
minRowRating = min(rowRating)

print(binListToDecInt(dataMatrix[rowRating.index(maxRowRating)]))
print(binListToDecInt(dataMatrix[rowRating.index(minRowRating)]))
"""