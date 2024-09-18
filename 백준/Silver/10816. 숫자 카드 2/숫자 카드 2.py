import sys

how_many_times = {}

# 상근이가 가지고 있는 숫자 카드 수와 카드 리스트
ownNum = int(sys.stdin.readline().strip())
ownCards = sys.stdin.readline().split()

# 주어진 숫자 카드 수와 카드 리스트
givenNum = int(sys.stdin.readline().strip())
givenCards = sys.stdin.readline().split()

# 상근이가 가진 카드의 개수를 카운트
for card in ownCards:
    if card in how_many_times:
        how_many_times[card] += 1
    else:
        how_many_times[card] = 1

# 주어진 카드에 대해 상근이가 몇 개 가지고 있는지 출력
result = []
for card in givenCards:
    result.append(how_many_times.get(card, 0))

# 결과 출력
print(' '.join(map(str, result)))