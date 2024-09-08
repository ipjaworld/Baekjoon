# 풀이, 이 과정의 역함수는 존재하지 않으므로 가장 작은 분해합을 알기 위해서는
# 1부터 해당하는 N까지의 숫자를 검증해야만 한다

# 1의 자리, 10의자리부터 해서 분해합인지 검증하는 함수
def isBunHaeHab(val):
    # val과 그 자리수의 합을 구함
    result = val + sum(map(int, str(val)))  # 숫자를 문자열로 변환 후, 각 자리수를 더함
    return result

# N의 가장 작은 생성자를 구하는 함수
def getBunHaeHab(N):
    for n in range(1, N):  # 1부터 N-1까지의 모든 숫자에 대해
        if isBunHaeHab(n) == N:  # 해당 숫자의 분해합이 N과 같으면
            return n  # 그 숫자를 반환
    return 0  # 생성자가 없는 경우 0 반환

n = int(input())  # 자연수 N 입력
print(getBunHaeHab(n))  # 결과 출력