import math

# 입력받기
N = int(input())  # 가로수의 수
trees = [int(input()) for _ in range(N)]  # 각 가로수의 위치

# 각 가로수 간의 간격 구하기
distances = []
for i in range(1, N):
    distances.append(trees[i] - trees[i - 1])

# 모든 간격들의 최대공약수(GCD) 구하기
gcd_value = distances[0]
for i in range(1, len(distances)):
    gcd_value = math.gcd(gcd_value, distances[i])

# 필요한 가로수의 수 계산
# (가로수 간격 // GCD - 1) 만큼 추가로 심어야 할 가로수의 수 계산
result = 0
for distance in distances:
    result += (distance // gcd_value) - 1

# 결과 출력
print(result)