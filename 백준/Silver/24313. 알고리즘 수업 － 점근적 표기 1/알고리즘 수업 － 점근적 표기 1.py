def is_big_o(a1, a0, c, n0):
    for n in range(n0, 101):
        f_n = a1 * n + a0
        g_n = c * n
        if f_n > g_n:
            return 0
    return 1

# 입력 받기
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# 결과 출력
print(is_big_o(a1, a0, c, n0))