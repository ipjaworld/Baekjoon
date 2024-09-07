def sieve_of_eratosthenes(n, k):
    is_prime = [True] * (n + 1)  # 0부터 n까지의 숫자에서 소수를 추적
    removed_count = 0  # 지운 숫자의 개수를 추적하는 변수

    for num in range(2, n + 1):  # 2부터 n까지의 숫자를 반복
        if is_prime[num]:  # 만약 num이 소수라면
            for multiple in range(num, n + 1, num):  # num의 배수를 지움
                if is_prime[multiple]:  # 배수가 아직 지워지지 않았다면
                    is_prime[multiple] = False  # 배수를 지움
                    removed_count += 1  # 지워진 숫자 카운트 증가
                    if removed_count == k:  # K번째로 지워졌다면
                        return multiple  # K번째 지워진 수 반환

n, k = map(int, input().split())
print(sieve_of_eratosthenes(n, k))