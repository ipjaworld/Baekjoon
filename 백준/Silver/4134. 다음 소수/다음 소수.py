import math

# 소수 여부를 판별하는 함수
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# n보다 크거나 같은 가장 작은 소수를 찾는 함수
def next_prime(n):
    if n <= 2:
        return 2
    if n == 3:
        return 3
    # 짝수라면 다음 홀수부터 확인
    if n % 2 == 0:
        n += 1
    # 홀수에서 시작해 소수 찾기
    while not is_prime(n):
        n += 2
    return n

# 입력 처리
T = int(input())  # 테스트 케이스의 수
for _ in range(T):
    n = int(input())  # 각 테스트 케이스의 n 입력
    print(next_prime(n))
