def get_triangle_circumference(a, b, c):
    # 세 막대 중 가장 긴 변을 찾고 나머지 두 변을 구한다
    if a >= b and a >= c:
        longest = a
        side1 = b
        side2 = c
    elif b >= a and b >= c:
        longest = b
        side1 = a
        side2 = c
    else:
        longest = c
        side1 = a
        side2 = b
    
    # 삼각형이 성립하지 않으면 가장 긴 변을 줄인다
    if longest >= side1 + side2:
        longest = side1 + side2 - 1
    
    # 세 변의 합을 반환 (둘레)
    return longest + side1 + side2

# 입력 받기
a, b, c = map(int, input().split())

# 함수 호출 및 결과 출력
circumference = get_triangle_circumference(a, b, c)
print(circumference)