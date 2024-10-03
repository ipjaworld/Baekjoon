import sys

def getFactorial(N):
    result = 1
    pointer = int(N)
    while pointer:
        result  = result * pointer
        pointer = pointer - 1

    print(result)
    return

def getAnswer():
    input = sys.stdin.read
    data = input()
    getFactorial(data)

getAnswer()