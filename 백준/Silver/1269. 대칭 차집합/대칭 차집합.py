import sys

def getAnswer ():
    input = sys.stdin.read
    data = input().splitlines()

    # 집합 A 원소의 갯수 N, 집합 B 원소의 갯수 M
    N, M = map(int, data[0].split())
    arrayA = set(data[1].split())
    arrayB = set(data[2].split())

    arrayAPlusB = sorted( arrayA | arrayB ) 
    arrayAnB = sorted( arrayA & arrayB )

    print(len(arrayAPlusB) - len(arrayAnB))

getAnswer()