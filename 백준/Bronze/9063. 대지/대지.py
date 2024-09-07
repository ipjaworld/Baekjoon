# 메인 함수
def get_square_area(number, points):
    # number가 0일 경우 넓이는 무조건 0
    if number == 0:
        return 0
    
    # X좌표와 Y좌표를 따로 저장
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    # X좌표에서 최대값 찾기
    x_max = max(x_coords)

    # X좌표에서 최소값 찾기
    x_min = min(x_coords)

    # Y좌표에서 최대값 찾기
    y_max = max(y_coords)

    # Y좌표에서 최소값 찾기
    y_min = min(y_coords)

    return ( ( x_max - x_min ) * ( y_max - y_min) )

# 점 갯수
number=int(input())
# 점들의 좌표
points = []
for _ in range(number):
    x, y = map(int, input().split())
    points.append((x, y))

result = get_square_area(number, points)
print(result)