N = int(input())  # 점의 개수
points = []

# 좌표 입력 받기
for _ in range(N):
    x, y = map(int, input().split())  # 각 좌표를 정수로 변환하여 입력받기
    points.append((x, y))  # 튜플 형태로 리스트에 저장

# 좌표 정렬: 먼저 x를 기준으로, x가 같으면 y를 기준으로 정렬
points.sort(key=lambda point: (point[0], point[1]))

# 결과 출력
for point in points:
    print(point[0], point[1])