import sys
import math

# 에라토스테네스의 체로 1,000,000까지의 소수를 미리 구하는 함수
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
                
    return is_prime

# 소수 여부를 미리 구함
MAX_LIMIT = 1000000
is_prime = sieve_of_eratosthenes(MAX_LIMIT)

# 골드바흐 파티션을 구하는 함수
def get_goldbach_partition(n):
    count = 0
    for i in range(2, n // 2 + 1):  # i는 두 소수 중 작은 값
        if is_prime[i] and is_prime[n - i]:
            count += 1
    return count

# 입력 받기
input = sys.stdin.read
data = input().splitlines()

# 각 테스트 케이스 처리
T = int(data[0])  # 테스트 케이스의 수

for i in range(1, T + 1):
    N = int(data[i])
    result = get_goldbach_partition(N)
    print(result)