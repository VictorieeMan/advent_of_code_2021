#Shared functions

### Input functions

def read_lines(path):
    with open(path) as file:
        return file.read()

### Other funcitons

def testImport():
    print("Import works fine!")