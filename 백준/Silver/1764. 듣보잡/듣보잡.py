import sys

input = sys.stdin.read
data = input().splitlines()

# N: 듣도 못한 사람 수, M: 보도 못한 사람 수
N, M = map(int, data[0].split())

# 듣도 못한 사람들을 set에 저장
not_heard = set(data[1:N+1])

# 보도 못한 사람들도 set에 저장
not_seen = set(data[N+1:N+1+M])

# 듣도 보도 못한 사람의 교집합을 구함
not_heard_and_seen = sorted(not_heard & not_seen)

# 결과 출력
print(len(not_heard_and_seen))
print("\n".join(not_heard_and_seen))