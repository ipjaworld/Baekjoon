import sys

fibonachi = [ 0, 1 ]

def getFibonachi(i, N):
    if i == N:
        print(fibonachi[N])
        return
    newFibonachi = fibonachi[i] + fibonachi[i+1]
    fibonachi.append(newFibonachi)
    getFibonachi(i+1, N)

def getAnswer():
    input = sys.stdin.read
    N = int(input())
    getFibonachi(0, N)

getAnswer()