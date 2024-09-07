points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

def find_fourth_point(points):
    # X좌표와 Y좌표를 따로 저장
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    
    # X좌표에서 빈도수 1인 좌표 찾기
    for x in x_coords:
        if x_coords.count(x) == 1:
            x4 = x
            break
    
    # Y좌표에서 빈도수 1인 좌표 찾기
    for y in y_coords:
        if y_coords.count(y) == 1:
            y4 = y
            break
    
    return (x4, y4)

fourth_point = find_fourth_point(points)
print(fourth_point[0], fourth_point[1])