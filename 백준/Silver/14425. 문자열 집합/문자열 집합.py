# 문자열의 개수 N과 M을 입력 받음
N, M = map(int, input().split())

# 집합 S를 만들어서 N개의 문자열을 저장
N_Set = set()
for _ in range(N):
    N_Set.add(input().strip())  # 집합에 문자열 추가

# 검사할 문자열 리스트에서 집합에 포함된 문자열을 카운트
count = 0
for _ in range(M):
    if input().strip() in N_Set:
        count += 1

# 결과 출력
print(count)