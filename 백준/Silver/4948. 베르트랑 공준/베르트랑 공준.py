def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime(n):
    if n == 0:
        return
    start = n + 1
    end = (n * 2) + 1
    count = 0
    for j in range(start, end):
        result = is_prime(j)
        if result == True:
            count = count + 1
    print(count)

import sys
input = sys.stdin.read
data = input().splitlines()

for i in range(len(data)):
    n = int(data[i])
    count_prime(n)