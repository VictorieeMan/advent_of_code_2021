inputMeasurs = []
#[199,200,208,210,200,207,240,269,260,263]#[1,2,3,2,3] # Ought to answer 3


with open("AoC_day01_input.txt") as inputFile:
    lines = inputFile.readlines()
    #count = 0
    for line in lines:
        #count += 1
        inputMeasurs.append(line)
        #print(count, " ", line)

n = len(inputMeasurs)


def incrementCount(inputList):
    n = len(inputList)
    increases = 0
    decrease = 0
    na = 0
    for i in range(0, n):
        if i != 0:
            if inputList[i-1] < inputList[i]:
                increases += 1
            elif inputList[i-1] > inputList[i]:
                decrease +=1
            else:
                na += 1
        else:
            na += 1
    print(increases, " ", decrease, " ", na)

print("\nPart One")
incrementCount(inputMeasurs)
#ANS 1393

#Part 2

print("\nPart Two")

processedData = []

for i in range(0,n-2):
    temp = int(inputMeasurs[i]) + int(inputMeasurs[i+1]) + int(inputMeasurs[i+2])
    processedData.append(temp)
    print(temp)

incrementCount(processedData)

print("\nTesting")
incrementCount([199,200,208,210,200,207,240,269,260,263])
incrementCount([1,2,3,2,3])
