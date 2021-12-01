#Shared functions

### Input

def read_lines(path):
    with open(path) as file:
        return file.read()