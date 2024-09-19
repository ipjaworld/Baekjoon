import sys
import math

# GCD(최대공약수)를 이용해 LCM(최소공배수)를 구하는 함수
def getLeastCommonMultiple(a, b):
    a = int(a)
    b = int(b)
    gcd = math.gcd(a, b)  # 최대공약수 구하기
    lcm = (a * b) // gcd  # 두 수의 곱을 최대공약수로 나눔
    print(lcm)  # 최소공배수 출력
    return lcm

def getAnswer():
    input = sys.stdin.read
    data = input().splitlines()

    temp = data[0].split()
    getLeastCommonMultiple(temp[0], temp[1])

getAnswer()