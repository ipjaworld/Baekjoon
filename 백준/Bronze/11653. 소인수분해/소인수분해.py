def prime_factorization(n):
    # 1은 소인수분해 결과가 없으므로 아무것도 출력하지 않음
    if n == 1:
        return
    
    # 2부터 시작하여 n의 소인수를 구함
    factor = 2
    while factor * factor <= n:  # factor의 제곱이 n보다 작거나 같을 때까지
        while n % factor == 0:  # n이 factor로 나누어떨어질 때
            print(factor)  # 소인수 출력
            n //= factor  # n을 factor로 나눔
        factor += 1  # 다음 인수로 넘어감
    
    # 마지막으로 남은 수가 소수일 경우 출력
    if n > 1:
        print(n)

# 입력 받기
N = int(input())
prime_factorization(N)