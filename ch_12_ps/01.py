'''
The following code was witten by me-
try:
    with open('1.txt') as f:
        pass
    with open('2.txt') as f:
        pass
    with open('3.txt') as f:
        pass
except Exception as e :
    print("One of these files do not exist", e)

'''

# See the following code -
def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found...")
        

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")