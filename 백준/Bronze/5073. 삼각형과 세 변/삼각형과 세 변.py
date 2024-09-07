# 삼각형과 세 변
# 10101 과 비슷한 느낌이 드는 문제
# 여기서는 각도가 아니라 변의 길이를 통해 구한다.

def get_triangle_type(sides):
    a, b, c = sorted(sides)  # 세 변의 길이를 오름차순으로 정렬
    # 삼각형 성립 조건 확인
    if a + b <= c:
        return 'Invalid'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'

while True:
    # 세 변의 길이 입력 받기
    sides = list(map(int, input().split()))
    
    # 종료 조건 (0 0 0)
    if sides == [0, 0, 0]:
        break
    
    # 삼각형 유형 출력
    result = get_triangle_type(sides)
    print(result)