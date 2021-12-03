#Shared functions

#Built in Python functions
# https://docs.python.org/3/library/functions.html

### Input functions

def read_lines(path):
    with open(path) as file:
        return file.read()

### Mathematical functions

# Arithmic Avreage
def avgArithm(x=[]):
    return sum(x)/len(x)

# Convert bin to dec list of ints
def binListToDecInt(x=[]):
    decNumb = 0
    powerIt = 0
    for i in reversed(x):
        decNumb += i*pow(2,powerIt)
        powerIt += 1
    return decNumb

#List vector size N
def listVector(n):
    vector = []
    while (n > 0):
        vector.append([])
        n -= 1
    return vector

#Transposes a list matrix
def matrixTranspose(inputMatrix=[]):
    return map(list,zip(*inputMatrix))

#Zero vector size N
def zeroVector(n):
    vector = []
    while (n > 0):
        vector.append(0)
        n -= 1
    return vector

### Other funcitons

def testImport():
    print("Import works fine!")