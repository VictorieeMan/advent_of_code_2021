"""Advent of Code 2021 -- Day03"""
from AoC_2021 import *

print("Part One", "\n")
inputData = read_lines("AoC_day04_input.txt").split("\n")

print("inputData: ",inputData)

drawnNumbers = inputData[0]
drawnNumbers = [int(n) for n in drawnNumbers.split(",")]
print("drawnNumbers: ",drawnNumbers)

boardData = inputData[1:]
print("boardData: ",boardData)

### Process inputData
board = []
bingoBoards = []

#Structure boardData to boards and convert elements to integers
for line in boardData:
    if line == "":
        pass
    else:
        board.append([int(n) for n in line.split()])
        if len(board) == 5:
            bingoBoards.append(board)
            board = [] #Why does board.clear() give bingoBoards with three empty [] when the loop is finished?

print("bingoBoards: ",bingoBoards)

#Tuple each board number with a bool value (for drawn status)
tupleBoards = []

for board in bingoBoards:
    tempBoard = []

    for line in board:
        tempLine = []

        for element in line:
            element = (element, False)
            tempLine.append(element)
        tempBoard.append(tempLine)
    
    tupleBoards.append(tempBoard)

print("tupleBoards: ",tupleBoards)

### Draw numbers and check winners

def bingoCheck(board=[]):
    bingoStatus = False

    def lineCheck(board=[]):
        #line check
        for line in board:
            lineScore = 0
            for element in line:
                if element[1]:
                    lineScore += 1
                else:
                    #Only perfect lineScore accepted for Bingo
                    break
            if lineScore == 5:
                return True
                break
        return False
    
    bingoStatus = lineCheck(board)

    if bingoStatus == False:
        flipedBoard = matrixTranspose(board) #So that columns can be checked as rows
        bingoStatus = lineCheck(flipedBoard)
    
    return bingoStatus

def boardUpdate(board,numberDrawn):
    for lineNr in range(0,len(board)):
        for elementNr in range(0,len(board[lineNr])):
            if board[lineNr][elementNr] == (numberDrawn,False):
                board[lineNr][elementNr] = (numberDrawn,True)
                break
        else:
            continue
        break
                
print(drawnNumbers)
for number in drawnNumbers:
    print(number)
    for boardNr in range(0,len(tupleBoards)):
        boardUpdate(tupleBoards[boardNr],number)
        status = bingoCheck(tupleBoards[boardNr])
        print(boardNr,status)
        if status == True:
            winData = [boardNr, number] # The winner board and it's final number
            break
    else:
        continue
    break

# Summing up the unmarked numbers
unmarkedSum = 0
for line in tupleBoards[winData[0]]:
    for element in line:
        if element[1] == False:
            unmarkedSum += element[0]

print(unmarkedSum*winData[1])

print("Part Two")

print(drawnNumbers)
victoryBoards = []
for number in drawnNumbers:
    print(number)
    for boardNr in range(0,len(tupleBoards)):
        if boardNr not in victoryBoards:
            boardUpdate(tupleBoards[boardNr],number)
            status = bingoCheck(tupleBoards[boardNr])
            print(boardNr,status)
            if status == True:
                winData = []
                winData.append([boardNr, number]) # The winner board and it's final number
                victoryBoards.append(boardNr)
"""
            if True:
                break
    else:
        continue
    break
"""

# Summing up the unmarked numbers
unmarkedSum = 0
lastWinBoard = winData[-1][0]
for line in tupleBoards[lastWinBoard]:
    for element in line:
        if element[1] == False:
            unmarkedSum += element[0]

print(unmarkedSum*winData[-1][1])