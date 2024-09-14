N = int(input())  # 점의 개수
members = []

# 좌표 입력 받기
for _ in range(N):
    x, y = map(str, input().split())  # 각 좌표를 정수로 변환하여 입력받기
    members.append((int(x), y))  # 튜플 형태로 리스트에 저장

# 좌표 정렬: 먼저 x를 기준으로, x가 같으면 y를 기준으로 정렬
members.sort(key=lambda member: (member[0]))

# 결과 출력
for member in members:
    print(member[0], member[1])