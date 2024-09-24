import math

def sieve_of_eratosthenes(M, N):
    # N까지의 소수 판별을 위한 배열
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아니므로 False 처리
    
    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(N)) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    
    # M 이상 N 이하의 소수 출력
    for i in range(M, N + 1):
        if is_prime[i]:
            print(i)

# 입력 받기
M, N = map(int, input().split())

# 소수 구하고 출력하기
sieve_of_eratosthenes(M, N)
