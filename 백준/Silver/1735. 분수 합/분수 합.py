import sys
import math

# GCD(최대공약수)를 이용해 LCM(최소공배수)를 구하는 함수
def getGcd(a, b):
    gcd = math.gcd(a, b)  # 최대공약수 구하기
    return gcd

def getAnswer():
    input = sys.stdin.read
    data = input().splitlines()

    firstLine = data[0].split()

    secondLine = data[1].split()

    afterSon = int(firstLine[0]) * int(secondLine[1]) + int(firstLine[1]) * int(secondLine[0])
    afterMom = int(firstLine[1]) * int(secondLine[1])
    
    gcd = getGcd(afterSon, afterMom)

    print(str( int( afterSon / gcd) ) + ' ' + str( int(afterMom / gcd) ))

getAnswer()