def solve_equations(a, b, c, d, e, f):
    # 분모 계산 (a * e - b * d)
    denominator = a * e - b * d
    if denominator == 0:
        raise ValueError("해가 유일하지 않습니다.")  # 유일한 해가 없는 경우를 처리

    # x와 y 계산
    x = (c * e - b * f) // denominator
    y = (a * f - d * c) // denominator
    return x, y

a, b, c, d, e, f = map(int, input().split())

# 결과 출력
x, y = solve_equations(a, b, c, d, e, f)
print(x, y)